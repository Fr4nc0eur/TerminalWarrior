"""Game Engine and State Management"""

import time
from typing import Dict, Optional
try:
    from .filesystem import VirtualFilesystem
    from .commands import CommandInterpreter, CommandResult
    from .puzzles import PuzzleManager, PuzzleStatus
except ImportError:
    from filesystem import VirtualFilesystem
    from commands import CommandInterpreter, CommandResult
    from puzzles import PuzzleManager, PuzzleStatus


class GameState:
    """Manages game state"""
    
    def __init__(self):
        self.filesystem = VirtualFilesystem()
        self.interpreter = CommandInterpreter(self.filesystem)
        self.puzzle_manager = PuzzleManager()
        self.start_time = time.time()
        self.game_active = True
        self.command_history = []
        self.puzzle_context = {}
    
    def reset(self) -> None:
        """Reset game state"""
        self.filesystem = VirtualFilesystem()
        self.interpreter = CommandInterpreter(self.filesystem)
        self.puzzle_manager = PuzzleManager()
        self.start_time = time.time()
        self.game_active = True
        self.command_history = []
        self.puzzle_context = {}
    
    def get_elapsed_time(self) -> int:
        """Get elapsed time in seconds"""
        return int(time.time() - self.start_time)
    
    def add_command_history(self, command: str, result: CommandResult) -> None:
        """Add command to history"""
        self.command_history.append({
            "command": command,
            "success": result.success,
            "output": result.output,
            "error": result.error
        })


class GameEngine:
    """Main game engine"""
    
    STORY_INTRO = r"""
/////////////////////////////////////////////////////////////////////////////
//                 **HACKER TERMINAL SIMULATOR**                         //
/////////////////////////////////////////////////////////////////////////////
|
| **ROLE:** You are a security researcher testing penetration skills.
| **GOAL:** Navigate the filesystem and solve hacking challenges
|           using real Linux commands. Complete all objectives.
|
+-------------------------------------------------------------+
|               **MISSION OBJECTIVES: THE SIX PHASES**        |
+-------------------------------------------------------------+
| **Welcome, agent. Your mission:**                           |
| 1. Find hidden credentials in log files                     |
| 2. Escalate privileges                                      |
| 3. Discover system configurations                           |
| 4. Bypass security restrictions                             |
| 5. Establish persistence mechanisms                         |
| 6. Demonstrate complete system compromise                   |
|                                                             |
+-------------------------------------------------------------+
| **SYSTEM PROMPT:**                                          |
| Type 'help' for command list, 'hint' for puzzle help, or    |
| 'status' for progress. Let's begin...                       |
\_____________________________________________________________/
"""
    def __init__(self):
        self.state = GameState()
        self.running = False
    
    def reset_game(self) -> None:
        """Reset the game"""
        self.state.reset()
    
    def execute_command(self, command_line: str) -> CommandResult:
        """Execute a command and update game state"""
        # Check for meta commands
        if command_line.lower() == "exit":
            self.state.game_active = False
            return CommandResult(True, "Goodbye!")
        
        if command_line.lower() == "hint":
            return self._handle_hint()
        
        if command_line.lower() == "status":
            return self._handle_status()
        
        if command_line.lower() == "puzzles":
            return self._handle_show_puzzles()
        
        if command_line.lower().startswith("solve "):
            puzzle_id = command_line[6:].strip()
            return self._handle_solve_puzzle(puzzle_id)
        
        # Execute regular command
        result = self.state.interpreter.execute(command_line)
        self.state.add_command_history(command_line, result)
        
        # Update puzzle context based on commands
        self._update_puzzle_context(command_line, result)
        
        # Check for puzzle completion
        self._check_puzzle_completion()
        
        return result
    
    def _handle_hint(self) -> CommandResult:
        """Handle hint request"""
        current = self.state.puzzle_manager.current_puzzle
        if not current:
            return CommandResult(False, error="No active puzzle. Use 'puzzles' to see available challenges.")
        
        puzzle = self.state.puzzle_manager.get_puzzle(current)
        if not puzzle:
            return CommandResult(False, error="Puzzle data not found.")
        hint_num = len([h for h in puzzle.hints if h.revealed])
        
        hint_text = puzzle.get_hint(hint_num)
        if hint_text:
            return CommandResult(True, f"💡 Hint: {hint_text}")
        else:
            return CommandResult(False, error="No more hints available for this puzzle.")
    
    def _handle_status(self) -> CommandResult:
        """Handle status request"""
        progress = self.state.puzzle_manager.get_progress()
        elapsed = self.state.get_elapsed_time()
        
        status = f"""
═══════════════════════════════════════════════════
                    GAME STATUS
═══════════════════════════════════════════════════
User: {self.state.filesystem.current_user}
Location: {self.state.filesystem.get_path(self.state.filesystem.current_dir)}
Elapsed Time: {elapsed} seconds

Progress: {progress['completed']}/{progress['total']} puzzles completed
Score: {progress['score']} points
Completion: {progress['percentage']:.1f}%

Current Directory: {self.state.filesystem.get_path(self.state.filesystem.current_dir)}
═══════════════════════════════════════════════════"""
        
        return CommandResult(True, status)
    
    def _handle_show_puzzles(self) -> CommandResult:
        """Show available puzzles"""
        puzzles = self.state.puzzle_manager.puzzles
        output = []
        output.append("\n═══════════════════════════════════════════════════")
        output.append("                   CHALLENGES")
        output.append("═══════════════════════════════════════════════════")
        
        for pid, puzzle in puzzles.items():
            status_icon = "✓" if puzzle.status == PuzzleStatus.COMPLETED else "○"
            difficulty = "⭐" * puzzle.difficulty
            output.append(f"\n[{status_icon}] {puzzle.title} {difficulty}")
            output.append(f"    ID: {puzzle.puzzle_id}")
            output.append(f"    {puzzle.description}")
            output.append(f"    Objectives: {', '.join(puzzle.objectives[:2])}...")
        
        output.append("\n═══════════════════════════════════════════════════")
        output.append("\nUse 'solve <puzzle_id>' to activate a puzzle")
        
        return CommandResult(True, "\n".join(output))
    
    def _handle_solve_puzzle(self, puzzle_id: str) -> CommandResult:
        """Activate a puzzle"""
        if self.state.puzzle_manager.start_puzzle(puzzle_id):
            puzzle = self.state.puzzle_manager.get_puzzle(puzzle_id)
            if puzzle:
                return CommandResult(True, f"Puzzle activated: {puzzle.title}\n\n{puzzle.description}\n\nObjectives:\n" + 
                                   "\n".join(f"- {obj}" for obj in puzzle.objectives))
            else:
                return CommandResult(False, error=f"Puzzle '{puzzle_id}' not found.")
        else:
            return CommandResult(False, error=f"Puzzle '{puzzle_id}' not found or already completed.")
    
    def _update_puzzle_context(self, command: str, result: CommandResult) -> None:
        """Update puzzle context based on command execution"""
        if not result.success:
            return
        
        # Track various puzzle-related actions
        if "grep" in command and "password" in command.lower():
            if "hidden_flag" in result.output or "flag" in result.output:
                self.state.puzzle_context["found_password"] = True
        
        if "sudo cat /etc/shadow" in command:
            self.state.puzzle_context["read_shadow"] = True
        
        if "find" in command and ".conf" in command:
            self.state.puzzle_context["config_files_found"] = result.output.count('\n') + 1
        
        if "chmod" in command and "777" in command:
            self.state.puzzle_context["perms_changed"] = True
        
        if "cut" in command and "/etc/passwd" in command:
            self.state.puzzle_context["decoded"] = True
        
        if "chmod" in command and "755" in command and "backdoor" in command:
            self.state.puzzle_context["backdoor_created"] = True
    
    def _check_puzzle_completion(self) -> None:
        """Check if current puzzle is completed"""
        current = self.state.puzzle_manager.current_puzzle
        if not current:
            return
        
        puzzle = self.state.puzzle_manager.get_puzzle(current)
        if puzzle and puzzle.validate_solution(self.state.puzzle_context):
            elapsed = self.state.get_elapsed_time()
            score = self.state.puzzle_manager.complete_puzzle(current, elapsed)
            try:
                print(f"\nPuzzle completed! Score: {score} points")
            except UnicodeEncodeError:
                print(f"\n[OK] Puzzle completed! Score: {score} points")
            self.state.puzzle_manager.current_puzzle = None
    
    def check_win_condition(self) -> bool:
        """Check if player has won"""
        return self.state.puzzle_manager.is_complete()
    
    def get_final_score(self) -> int:
        """Get final score"""
        return self.state.puzzle_manager.total_score
    
    def get_game_state(self) -> GameState:
        """Get current game state"""
        return self.state
