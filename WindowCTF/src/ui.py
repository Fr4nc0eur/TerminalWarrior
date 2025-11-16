"""CLI Interface and Terminal Rendering"""

from colorama import Fore, Back, Style, init
from prompt_toolkit import PromptSession
from prompt_toolkit.formatted_text import HTML
try:
    from .game import GameEngine
except ImportError:
    from game import GameEngine

# Initialize colorama for Windows compatibility
init(autoreset=True)


class TerminalUI:
    """Terminal user interface"""
    
    def __init__(self):
        self.engine = GameEngine()
        self.session = PromptSession()
        self.running = False
    
    def start_game(self) -> None:
        """Start the game loop"""
        self.running = True
        self._show_intro()
        self._game_loop()
    
    def _show_intro(self) -> None:
        """Display intro screen"""
        intro = GameEngine.STORY_INTRO
        try:
            print(Fore.CYAN + intro)
        except UnicodeEncodeError:
            # Fallback for Windows console encoding issues
            print(intro.encode('ascii', 'ignore').decode('ascii'))
        print(Style.RESET_ALL)
    
    def _game_loop(self) -> None:
        """Main game loop"""
        state = self.engine.get_game_state()
        
        while self.running and state.game_active:
            try:
                # Get current directory for prompt
                current_path = state.filesystem.get_path(state.filesystem.current_dir)
                user = state.filesystem.current_user
                
                # Create prompt with colors using prompt_toolkit HTML formatting
                try:
                    # Use literal 'guest' in the prompt so runtime shows guest@terminal
                    prompt_text = HTML(f"<ansigreen>guest@terminal</ansigreen>:<ansiblue>{current_path}</ansiblue>$ ")
                except Exception:
                    # Fallback to plain text if formatting fails
                    prompt_text = f"guest@terminal:{current_path}$ "

                # Get command input (prompt accepts FormattedText or str)
                command = self.session.prompt(prompt_text).strip()
                
                if not command:
                    continue
                
                # Execute command
                result = self.engine.execute_command(command)
                
                # Display result
                if result.success:
                    if result.output:
                        print(Fore.WHITE + result.output + Style.RESET_ALL)
                else:
                    if result.error:
                        print(Fore.RED + f"Error: {result.error}" + Style.RESET_ALL)
                
                # Check win condition
                if self.engine.check_win_condition():
                    self._show_victory()
                    self.running = False
                
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}Use 'exit' command to quit{Style.RESET_ALL}")
            except Exception as e:
                print(Fore.RED + f"Unexpected error: {str(e)}" + Style.RESET_ALL)
    
    def _show_victory(self) -> None:
        """Show victory screen"""
        final_score = self.engine.get_final_score()
        victory_text = f"""
{Fore.GREEN}
╔════════════════════════════════════════════════════════════════╗
║                     VICTORY! VICTORY!                         ║
║                                                                ║
║             You have successfully completed all                ║
║                  hacking challenges!                           ║
║                                                                ║
║                    Final Score: {final_score:>6} points                  ║
╚════════════════════════════════════════════════════════════════╝

Congratulations! You have demonstrated mastery of:
  [OK] Linux filesystem navigation
  [OK] Permission escalation
  [OK] Information gathering
  [OK] File manipulation
  [OK] System exploitation
  [OK] Persistence mechanisms

Your journey as a security researcher is just beginning...
{Style.RESET_ALL}"""
        
        try:
            print(victory_text)
        except UnicodeEncodeError:
            print(victory_text.encode('ascii', 'ignore').decode('ascii'))
    
    @staticmethod
    def clear_screen() -> None:
        """Clear terminal screen"""
        print("\033[2J\033[H", end="")
    
    @staticmethod
    def print_banner(text: str) -> None:
        """Print colored banner"""
        print(Fore.CYAN + f"\n{'='*60}")
        print(Fore.CYAN + text.center(60))
        print(Fore.CYAN + f"{'='*60}\n" + Style.RESET_ALL)
    
    @staticmethod
    def print_success(text: str) -> None:
        """Print success message"""
        print(Fore.GREEN + f"✓ {text}" + Style.RESET_ALL)
    
    @staticmethod
    def print_error(text: str) -> None:
        """Print error message"""
        print(Fore.RED + f"✗ {text}" + Style.RESET_ALL)
    
    @staticmethod
    def print_info(text: str) -> None:
        """Print info message"""
        print(Fore.BLUE + f"ℹ {text}" + Style.RESET_ALL)
    
    @staticmethod
    def print_warning(text: str) -> None:
        """Print warning message"""
        print(Fore.YELLOW + f"⚠ {text}" + Style.RESET_ALL)
