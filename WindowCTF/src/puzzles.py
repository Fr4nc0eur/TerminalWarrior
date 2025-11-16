"""Puzzle and Challenge System"""

from typing import List, Dict, Optional, Callable
from dataclasses import dataclass
from enum import Enum


class PuzzleStatus(Enum):
    """Puzzle completion status"""
    LOCKED = "locked"
    AVAILABLE = "available"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


@dataclass
class Hint:
    """Hint for a puzzle"""
    text: str
    revealed: bool = False


class Puzzle:
    """Represents a single puzzle/challenge"""
    
    def __init__(self, puzzle_id: str, title: str, description: str, 
                 objectives: List[str], hints: List[str], validator: Callable,
                 difficulty: int = 1):
        self.puzzle_id = puzzle_id
        self.title = title
        self.description = description
        self.objectives = objectives
        self.hints = [Hint(h) for h in hints]
        self.validator = validator
        self.difficulty = difficulty
        self.status = PuzzleStatus.AVAILABLE
        self.hints_used = 0
        self.score = 0
        self.completion_time = 0
    
    def validate_solution(self, context: Dict) -> bool:
        """Validate if puzzle is solved"""
        return self.validator(context)
    
    def get_hint(self, hint_num: int) -> Optional[str]:
        """Get a hint"""
        if hint_num < len(self.hints):
            self.hints[hint_num].revealed = True
            self.hints_used += 1
            return self.hints[hint_num].text
        return None
    
    def complete(self, time_taken: int) -> int:
        """Mark puzzle as completed and calculate score"""
        self.status = PuzzleStatus.COMPLETED
        self.completion_time = time_taken
        # Score = base difficulty * 100 - hints_used * 10 - time_penalty
        self.score = max(0, (self.difficulty * 100) - (self.hints_used * 10) - (time_taken // 10))
        return self.score


class PuzzleManager:
    """Manages all puzzles in the game"""
    
    def __init__(self):
        self.puzzles: Dict[str, Puzzle] = {}
        self.completed_puzzles: List[str] = []
        self.current_puzzle: Optional[str] = None
        self.total_score = 0
        self._initialize_puzzles()
    
    def _initialize_puzzles(self) -> None:
        """Initialize all puzzles"""
        
        # Puzzle 1: Find the password
        def validate_find_password(context):
            return context.get("found_password") == True
        
        puzzle1 = Puzzle(
            "find_password",
            "Find the Hidden Password",
            "A password is hidden in one of the log files. Use grep to search for it.",
            [
                "Look in the /tmp directory for log files",
                "Use grep with the pattern 'password' to find hints",
                "Check /tmp/log.txt"
            ],
            [
                "Start by navigating to /tmp",
                "Use: grep 'password' /tmp/log.txt",
                "The password contains 'flag'"
            ],
            validate_find_password,
            difficulty=1
        )
        
        # Puzzle 2: Read protected file
        def validate_read_protected(context):
            return context.get("read_shadow") == True
        
        puzzle2 = Puzzle(
            "read_protected",
            "Read Protected File",
            "The /etc/shadow file contains important information, but only root can read it. Use sudo to elevate privileges.",
            [
                "Use sudo to run commands with root privileges",
                "Try: sudo cat /etc/shadow"
            ],
            [
                "You need root privileges to read /etc/shadow",
                "Use the sudo command: sudo cat /etc/shadow",
                "This simulates privilege escalation"
            ],
            validate_read_protected,
            difficulty=2
        )
        
        # Puzzle 3: Find all configuration files
        def validate_find_config(context):
            count = context.get("config_files_found", 0)
            return count >= 2
        
        puzzle3 = Puzzle(
            "find_config",
            "Locate Configuration Files",
            "Find all configuration files (.conf or .config) on the system using the find command.",
            [
                "Use find to search for files",
                "Search for files with specific patterns"
            ],
            [
                "Use find from the root directory: find / -name '*.conf' -o -name '*.config'",
                "Look in /etc for configuration files"
            ],
            validate_find_config,
            difficulty=2
        )
        
        # Puzzle 4: Change file permissions
        def validate_chmod(context):
            return context.get("perms_changed") == True
        
        puzzle4 = Puzzle(
            "permission_escalation",
            "Escalate File Permissions",
            "Change file permissions to make a read-only file writable, then modify its contents.",
            [
                "Use chmod to change permissions",
                "Make a file writable"
            ],
            [
                "chmod is the change mode command",
                "777 permissions mean full access",
                "Try: chmod 777 /home/player/secret.txt"
            ],
            validate_chmod,
            difficulty=3
        )
        
        # Puzzle 5: Decode information
        def validate_decode(context):
            return context.get("decoded") == True
        
        puzzle5 = Puzzle(
            "decode_info",
            "Decode Hidden Information",
            "Use text processing commands to extract and decode information from files.",
            [
                "Combine grep, cut, and other text tools",
                "Work with /etc/passwd to find user information"
            ],
            [
                "Use grep to find user entries in /etc/passwd",
                "Use cut to extract specific fields",
                "Try: grep 'player' /etc/passwd | cut -d: -f1,3,6"
            ],
            validate_decode,
            difficulty=3
        )
        
        # Puzzle 6: Create backdoor
        def validate_backdoor(context):
            return context.get("backdoor_created") == True
        
        puzzle6 = Puzzle(
            "create_backdoor",
            "Establish Persistence",
            "Create a backdoor by adding a new user account or creating executable in a startup location.",
            [
                "Create a file in /tmp with executable permissions",
                "Use echo and chmod together"
            ],
            [
                "Create a script: echo '#!/bin/bash' > /tmp/backdoor.sh",
                "Make it executable: chmod 755 /tmp/backdoor.sh",
                "This represents planting a backdoor"
            ],
            validate_backdoor,
            difficulty=4
        )
        
        # Add puzzles to manager
        for puzzle in [puzzle1, puzzle2, puzzle3, puzzle4, puzzle5, puzzle6]:
            self.puzzles[puzzle.puzzle_id] = puzzle
    
    def get_puzzle(self, puzzle_id: str) -> Optional[Puzzle]:
        """Get a puzzle by ID"""
        return self.puzzles.get(puzzle_id)
    
    def get_available_puzzles(self) -> List[Puzzle]:
        """Get all available puzzles"""
        return [p for p in self.puzzles.values() if p.status in [PuzzleStatus.AVAILABLE, PuzzleStatus.IN_PROGRESS]]
    
    def start_puzzle(self, puzzle_id: str) -> bool:
        """Start a puzzle"""
        puzzle = self.get_puzzle(puzzle_id)
        if puzzle and puzzle.status != PuzzleStatus.COMPLETED:
            puzzle.status = PuzzleStatus.IN_PROGRESS
            self.current_puzzle = puzzle_id
            return True
        return False
    
    def complete_puzzle(self, puzzle_id: str, time_taken: int) -> int:
        """Complete a puzzle and return score"""
        puzzle = self.get_puzzle(puzzle_id)
        if puzzle:
            score = puzzle.complete(time_taken)
            self.total_score += score
            self.completed_puzzles.append(puzzle_id)
            return score
        return 0
    
    def get_progress(self) -> Dict:
        """Get game progress"""
        return {
            "completed": len(self.completed_puzzles),
            "total": len(self.puzzles),
            "score": self.total_score,
            "percentage": (len(self.completed_puzzles) / len(self.puzzles)) * 100
        }
    
    def is_complete(self) -> bool:
        """Check if all puzzles are completed"""
        return len(self.completed_puzzles) == len(self.puzzles)
