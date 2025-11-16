# CLI Hacking Game - Quick Start Guide

## Installation

### Windows (PowerShell)

```powershell
# Navigate to project directory
cd path\to\mike

# Install dependencies (virtual environment already created)
.\.venv\Scripts\Activate
pip install -r requirements.txt
```

### macOS/Linux

```bash
cd path/to/mike
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the Game

### Windows (PowerShell)

```powershell
# Activate virtual environment (if not already activated)
.\.venv\Scripts\Activate

# Run the game
python main.py
```

### macOS/Linux

```bash
source .venv/bin/activate
python main.py
```

## Game Commands

### Navigation Commands
- `pwd` - Print working directory
- `cd <path>` - Change directory (e.g., `cd /tmp` or `cd ..`)
- `ls` - List directory contents
- `ls -l` - List with detailed info
- `ls -a` - Include hidden files

### File Commands
- `cat <file>` - Display file contents
- `grep <pattern> <file>` - Search for text patterns
- `find <path> [-name pattern]` - Search for files
- `file <path>` - Determine file type
- `wc <file>` - Count lines/words/characters
- `head <file>` - Show first 10 lines
- `tail <file>` - Show last 10 lines
- `stat <file>` - Show file statistics
- `touch <file>` - Create or update file
- `chmod <perms> <file>` - Change permissions (e.g., `chmod 777 file.txt`)

### Information Commands
- `whoami` - Display current user
- `echo <text>` - Print text
- `sudo <command>` - Execute as root (e.g., `sudo cat /etc/shadow`)

### Game Commands
- `status` - Show progress and score
- `puzzles` - List all available challenges
- `solve <puzzle_id>` - Activate a specific puzzle
- `hint` - Get a hint for current puzzle
- `help` - Show command help
- `exit` - Quit the game

## Example Gameplay

### Starting a Puzzle

```
player@hacker:/$ puzzles
[Shows list of available challenges]

player@hacker:/$ solve find_password
[Puzzle activated: Find the Hidden Password]

player@hacker:/$ cd /tmp
player@hacker:/tmp$ ls
log.txt

player@hacker:/tmp$ grep password log.txt
[2025-11-15] Password: hidden_flag_123

[SUCCESS] Puzzle completed! Score: 80 points
```

### Using Hints

```
player@hacker:/$ hint
[Hint: Look in the /tmp directory for log files]

player@hacker:/$ hint
[Hint: Use grep with the pattern 'password' to find hints]
```

### Privilege Escalation

```
player@hacker:/$ cat /etc/shadow
cat: /etc/shadow: Permission denied

player@hacker:/$ sudo cat /etc/shadow
[Displays shadow file contents]

[SUCCESS] Puzzle completed! Score: 75 points
```

## Puzzle Objectives

1. **Find the Hidden Password** - Search log files for credentials
2. **Read Protected File** - Use sudo to bypass permissions
3. **Locate Configuration Files** - Find system config files using find command
4. **Escalate File Permissions** - Modify file permissions with chmod
5. **Decode Hidden Information** - Extract data using text processing commands
6. **Establish Persistence** - Create executable scripts in system locations

## Scoring

- Base score per puzzle: Difficulty level × 100
- Penalties: -10 points per hint used, -time penalty (1 point per 10 seconds)
- Complete all 6 puzzles to win!

## Filesystem Structure

The game includes a simulated Linux filesystem with:

```
/
├── bin/          - Binary executables
├── etc/          - System configuration
│   ├── passwd    - User database
│   └── shadow    - Password hashes
├── home/         - User home directories
│   └── player/   - Your home directory
├── root/         - Root user home
├── tmp/          - Temporary files
│   └── log.txt   - Important logs
└── var/          - Variable data
```

## Tips and Tricks

1. **Navigation**: Use `pwd` to see where you are, `cd ..` to go up one level
2. **Exploration**: Use `ls` to explore directories and `cat` to read files
3. **Searching**: Combine `grep` and `find` to locate specific information
4. **Permissions**: Check `ls -l` to see file permissions (e.g., `-rw-r--r--`)
5. **Sudoing**: Most restricted files require `sudo` to access
6. **History**: The game tracks your commands and validates solutions automatically

## Troubleshooting

### Terminal Colors Not Working
- The game should work on both Windows 10+ and Unix systems
- If colors don't display, the game will fall back to plain text

### Import Errors
- Ensure you're in the virtual environment: `.\.venv\Scripts\Activate`
- Verify dependencies: `pip list` should show `colorama` and `prompt_toolkit`

### Command Not Found
- Check spelling: `ls` not `list`, `cat` not `display`
- Use `help` to see the full command list
- Some commands may require root via `sudo`

## For Developers

See `README.md` and `.github/copilot-instructions.md` for architecture details.

### Project Structure
- `src/main.py` - Entry point
- `src/filesystem.py` - Virtual filesystem simulator
- `src/commands.py` - Linux command interpreter
- `src/puzzles.py` - Puzzle system
- `src/game.py` - Game engine
- `src/ui.py` - Terminal interface
- `data/` - Game content (currently in code)

### Running Tests

```python
# Test all modules
python -m pytest tests/ -v

# Test specific module
python -m pytest tests/test_filesystem.py -v
```

## License

MIT - Feel free to modify and distribute!
