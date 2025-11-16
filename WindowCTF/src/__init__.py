"""CLI Hacking Game - Simulated Linux Filesystem with Hacking Puzzles"""

__version__ = "1.0.0"
__author__ = "Security Research Team"

from .filesystem import VirtualFilesystem, FileNode
from .commands import CommandInterpreter, CommandResult
from .puzzles import PuzzleManager, Puzzle
from .game import GameEngine, GameState
from .ui import TerminalUI

__all__ = [
    "VirtualFilesystem",
    "FileNode",
    "CommandInterpreter",
    "CommandResult",
    "PuzzleManager",
    "Puzzle",
    "GameEngine",
    "GameState",
    "TerminalUI",
]
