# CLI Hacking Game - Cross-Platform Linux Filesystem Simulator

A command-line game where you explore a simulated Linux filesystem and solve hacking-themed puzzles using realistic Linux commands. **Works on Windows, macOS, and Linux with no native dependencies!**

## Features

- **Virtual Linux Filesystem**: In-memory filesystem simulation with directories, files, permissions, and symlinks
- **15+ Linux Commands**: Execute real commands like `ls`, `cat`, `grep`, `find`, `chmod`, `whoami`, `sudo`, and more
- **6 Progressive Hacking Challenges**: Escalating difficulty from file discovery to privilege escalation
- **Cross-Platform**: Works natively on Windows, macOS, and Linux
- **Interactive CLI**: Rich terminal interface with colors and real-time feedback
- **Scoring System**: Earn points, use hints, compete for high scores
- **Educational**: Learn Linux filesystem concepts and security principles

## Quick Start

### Installation

```bash
# Navigate to project directory
cd mike

# Install dependencies (requires Python 3.7+)
pip install -r requirements.txt
```

### Run the Game

```bash
python main.py
```

## Project Structure

- `src/main.py` - Game entry point
- `src/filesystem.py` - Virtual filesystem simulator
- `src/commands.py` - Linux command interpreter
- `src/puzzles.py` - Puzzle and challenge system
- `src/game.py` - Game engine and state management
- `src/ui.py` - CLI interface and terminal rendering
- `data/scenarios.json` - Game scenarios and puzzles

## Commands Supported

- `ls` - List directory contents
- `cat` - Display file contents
- `grep` - Search text patterns
- `find` - Search for files
- `chmod` - Change file permissions
- `pwd` - Print working directory
- `cd` - Change directory
- `whoami` - Display current user
- `sudo` - Execute with elevated privileges
- `file` - Determine file type
- `wc` - Word/line count
- `head`/`tail` - Display file portions
- And more...

## Game Flow

1. **Introduction**: Learn the story and objectives
2. **Exploration**: Navigate the filesystem and discover clues
3. **Puzzles**: Solve challenges by executing commands
4. **Progression**: Unlock new areas and challenges
5. **Victory**: Complete all objectives and win the game

## License

MIT License - Feel free to use, modify, and distribute!

---

**Have fun hacking! Can you complete all challenges?** 🖥️

For detailed information, see [QUICKSTART.md](QUICKSTART.md) and the [development guide](.github/copilot-instructions.md).
# FileSystem-CTF
