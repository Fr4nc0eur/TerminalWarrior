"""Main entry point for the CLI Hacking Game"""

import sys
import os

from src.ui import TerminalUI


def main():
    """Main entry point"""
    try:
        ui = TerminalUI()
        ui.start_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nFatal error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
