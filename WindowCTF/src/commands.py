"""Linux Command Interpreter"""

import re
from typing import List, Tuple, Optional
try:
    from .filesystem import VirtualFilesystem, FileNode
except ImportError:
    from filesystem import VirtualFilesystem, FileNode


class CommandResult:
    """Result of command execution"""
    
    def __init__(self, success: bool, output: str = "", error: str = ""):
        self.success = success
        self.output = output
        self.error = error


class CommandInterpreter:
    """Interprets and executes Linux commands against virtual filesystem"""
    
    def __init__(self, filesystem: VirtualFilesystem):
        self.fs = filesystem
        self.command_map = {
            'ls': self.cmd_ls,
            'cat': self.cmd_cat,
            'pwd': self.cmd_pwd,
            'cd': self.cmd_cd,
            'whoami': self.cmd_whoami,
            'grep': self.cmd_grep,
            'find': self.cmd_find,
            'chmod': self.cmd_chmod,
            'echo': self.cmd_echo,
            'file': self.cmd_file,
            'wc': self.cmd_wc,
            'head': self.cmd_head,
            'tail': self.cmd_tail,
            'stat': self.cmd_stat,
            'touch': self.cmd_touch,
            'sudo': self.cmd_sudo,
            'help': self.cmd_help,
        }
    
    def execute(self, command_line: str) -> CommandResult:
        """Execute a command line"""
        if not command_line.strip():
            return CommandResult(True, "")
        
        parts = self._parse_command(command_line)
        if not parts:
            return CommandResult(False, error="Invalid command")
        
        cmd_name = parts[0].lower()
        args = parts[1:]
        
        if cmd_name not in self.command_map:
            return CommandResult(False, error=f"Command not found: {cmd_name}")
        
        try:
            return self.command_map[cmd_name](args)
        except Exception as e:
            return CommandResult(False, error=str(e))
    
    def _parse_command(self, command_line: str) -> List[str]:
        """Parse command line into parts"""
        # Simple parser - handles quoted strings
        parts = []
        current = ""
        in_quotes = False
        
        for char in command_line:
            if char == '"' and (not current or current[-1] != '\\'):
                in_quotes = not in_quotes
            elif char == ' ' and not in_quotes:
                if current:
                    parts.append(current)
                    current = ""
            else:
                current += char
        
        if current:
            parts.append(current)
        
        return parts
    
    def cmd_ls(self, args: List[str]) -> CommandResult:
        """ls - List directory contents"""
        target = "."
        long_format = False
        all_files = False
        
        for arg in args:
            if arg == "-l":
                long_format = True
            elif arg == "-a":
                all_files = True
            elif not arg.startswith("-"):
                target = arg
        
        node = self.fs.navigate_to(target)
        if not node:
            return CommandResult(False, error=f"ls: cannot access '{target}': No such file or directory")
        
        if not node.is_dir:
            return CommandResult(False, error=f"ls: '{target}' is not a directory")
        
        if not node.is_readable(self.fs.current_user):
            return CommandResult(False, error=f"ls: cannot open directory '{target}': Permission denied")
        
        output = []
        items = node.list_children()
        
        for name, child in items:
            if not all_files and name.startswith("."):
                continue
            
            if long_format:
                perms = child.permissions
                size = child.get_size()
                owner = child.owner
                file_type = "d" if child.is_dir else "-"
                output.append(f"{file_type}{perms} {owner} {size} {child.modified_time.strftime('%b %d %H:%M')} {name}")
            else:
                output.append(name)
        
        return CommandResult(True, "\n".join(output) if output else "")
    
    def cmd_cat(self, args: List[str]) -> CommandResult:
        """cat - Display file contents"""
        if not args:
            return CommandResult(False, error="cat: missing operand")
        
        output = []
        for filename in args:
            node = self.fs.navigate_to(filename)
            if not node:
                output.append(f"cat: {filename}: No such file or directory")
                continue
            
            if node.is_dir:
                output.append(f"cat: {filename}: Is a directory")
                continue
            
            if not node.is_readable(self.fs.current_user):
                output.append(f"cat: {filename}: Permission denied")
                continue
            
            output.append(node.content.rstrip())
        
        return CommandResult(True, "\n".join(output))
    
    def cmd_pwd(self, args: List[str]) -> CommandResult:
        """pwd - Print working directory"""
        return CommandResult(True, self.fs.get_path(self.fs.current_dir))
    
    def cmd_cd(self, args: List[str]) -> CommandResult:
        """cd - Change directory"""
        if not args:
            path = f"/home/{self.fs.current_user}"
        else:
            path = args[0]
        
        if self.fs.change_directory(path):
            return CommandResult(True)
        else:
            return CommandResult(False, error=f"cd: {path}: No such file or directory")
    
    def cmd_whoami(self, args: List[str]) -> CommandResult:
        """whoami - Print current user"""
        return CommandResult(True, self.fs.current_user)
    
    def cmd_grep(self, args: List[str]) -> CommandResult:
        """grep - Search text patterns"""
        if len(args) < 2:
            return CommandResult(False, error="grep: missing arguments")
        
        pattern = args[0]
        filename = args[1]
        
        node = self.fs.navigate_to(filename)
        if not node:
            return CommandResult(False, error=f"grep: {filename}: No such file or directory")
        
        if node.is_dir:
            return CommandResult(False, error=f"grep: {filename}: Is a directory")
        
        if not node.is_readable(self.fs.current_user):
            return CommandResult(False, error=f"grep: {filename}: Permission denied")
        
        try:
            regex = re.compile(pattern, re.IGNORECASE)
            matches = [line for line in node.content.split('\n') if line and regex.search(line)]
            return CommandResult(True, "\n".join(matches) if matches else "")
        except re.error:
            return CommandResult(False, error=f"grep: Invalid regular expression")
    
    def cmd_find(self, args: List[str]) -> CommandResult:
        """find - Search for files"""
        if not args:
            return CommandResult(False, error="find: missing arguments")
        
        start_path = args[0] if args and not args[0].startswith("-") else "."
        name_pattern = None
        
        for i, arg in enumerate(args):
            if arg == "-name" and i + 1 < len(args):
                name_pattern = args[i + 1]
        
        start_node = self.fs.navigate_to(start_path)
        if not start_node:
            return CommandResult(False, error=f"find: '{start_path}': No such file or directory")
        
        results = []
        self._find_recursive(start_node, name_pattern, results, start_path)
        
        return CommandResult(True, "\n".join(results) if results else "")
    
    def _find_recursive(self, node: FileNode, pattern: Optional[str], results: List[str], current_path: str) -> None:
        """Recursively search directory"""
        for name, child in node.list_children():
            if not child.is_readable(self.fs.current_user):
                continue
            
            child_path = f"{current_path}/{name}".replace("//", "/")
            
            if pattern is None or self._match_pattern(name, pattern):
                results.append(child_path)
            
            if child.is_dir:
                self._find_recursive(child, pattern, results, child_path)
    
    def _match_pattern(self, name: str, pattern: str) -> bool:
        """Match filename against pattern (simple wildcard support)"""
        pattern = pattern.replace("*", ".*").replace("?", ".")
        return bool(re.match(f"^{pattern}$", name))
    
    def cmd_chmod(self, args: List[str]) -> CommandResult:
        """chmod - Change file permissions"""
        if len(args) < 2:
            return CommandResult(False, error="chmod: missing arguments")
        
        permissions = args[0]
        filename = args[1]
        
        if not re.match(r"^\d{3}$", permissions):
            return CommandResult(False, error="chmod: invalid permissions")
        
        if self.fs.chmod(filename, permissions):
            return CommandResult(True)
        else:
            return CommandResult(False, error=f"chmod: {filename}: No such file or directory")
    
    def cmd_echo(self, args: List[str]) -> CommandResult:
        """echo - Print text"""
        return CommandResult(True, " ".join(args))
    
    def cmd_file(self, args: List[str]) -> CommandResult:
        """file - Determine file type"""
        if not args:
            return CommandResult(False, error="file: missing argument")
        
        node = self.fs.navigate_to(args[0])
        if not node:
            return CommandResult(False, error=f"file: {args[0]}: No such file or directory")
        
        if node.is_dir:
            file_type = "directory"
        elif node.name.endswith(".txt"):
            file_type = "ASCII text"
        else:
            file_type = "empty" if node.get_size() == 0 else "data"
        
        return CommandResult(True, f"{args[0]}: {file_type}")
    
    def cmd_wc(self, args: List[str]) -> CommandResult:
        """wc - Count lines, words, characters"""
        if not args:
            return CommandResult(False, error="wc: missing argument")
        
        node = self.fs.navigate_to(args[0])
        if not node:
            return CommandResult(False, error=f"wc: {args[0]}: No such file or directory")
        
        lines = node.content.count('\n')
        words = len(node.content.split())
        chars = len(node.content)
        
        return CommandResult(True, f"{lines} {words} {chars} {args[0]}")
    
    def cmd_head(self, args: List[str]) -> CommandResult:
        """head - Display first lines"""
        if not args:
            return CommandResult(False, error="head: missing argument")
        
        lines_count = 10
        filename = args[-1]
        
        node = self.fs.navigate_to(filename)
        if not node:
            return CommandResult(False, error=f"head: {filename}: No such file or directory")
        
        lines = node.content.split('\n')[:lines_count]
        return CommandResult(True, "\n".join(lines))
    
    def cmd_tail(self, args: List[str]) -> CommandResult:
        """tail - Display last lines"""
        if not args:
            return CommandResult(False, error="tail: missing argument")
        
        lines_count = 10
        filename = args[-1]
        
        node = self.fs.navigate_to(filename)
        if not node:
            return CommandResult(False, error=f"tail: {filename}: No such file or directory")
        
        lines = node.content.split('\n')[-lines_count:]
        return CommandResult(True, "\n".join(lines))
    
    def cmd_stat(self, args: List[str]) -> CommandResult:
        """stat - Display file statistics"""
        if not args:
            return CommandResult(False, error="stat: missing argument")
        
        node = self.fs.navigate_to(args[0])
        if not node:
            return CommandResult(False, error=f"stat: {args[0]}: No such file or directory")
        
        info = f"""File: {args[0]}
Size: {node.get_size()} Bytes
Owner: {node.owner}
Permissions: {node.permissions}
Modified: {node.modified_time}
Type: {'Directory' if node.is_dir else 'Regular file'}"""
        
        return CommandResult(True, info)
    
    def cmd_touch(self, args: List[str]) -> CommandResult:
        """touch - Create empty file or update timestamp"""
        if not args:
            return CommandResult(False, error="touch: missing argument")
        
        for filename in args:
            if "/" in filename:
                return CommandResult(False, error=f"touch: {filename}: No such file or directory")
            
            node = self.fs.current_dir.get_child(filename)
            if node:
                node.modified_time = node.modified_time  # Update timestamp
            else:
                self.fs.create_file(filename)
        
        return CommandResult(True)
    
    def cmd_sudo(self, args: List[str]) -> CommandResult:
        """sudo - Execute as root"""
        if not args:
            return CommandResult(False, error="sudo: missing command")
        
        current_user = self.fs.current_user
        self.fs.current_user = "root"
        result = self.execute(" ".join(args))
        self.fs.current_user = current_user
        
        return result
    
    def cmd_help(self, args: List[str]) -> CommandResult:
        """help - Display help information"""
        help_text = """Available commands:
ls [options] [path]     - List directory contents
cat [file]              - Display file contents
pwd                     - Print working directory
cd [path]               - Change directory
whoami                  - Print current user
grep [pattern] [file]   - Search text patterns
find [path] [-name]     - Search for files
chmod [perms] [file]    - Change file permissions
echo [text]             - Print text
file [path]             - Determine file type
wc [file]               - Count lines/words/characters
head [file]             - Display first lines
tail [file]             - Display last lines
stat [file]             - Display file statistics
touch [file]            - Create/update file
sudo [command]          - Execute as root
help                    - Show this help"""
        
        return CommandResult(True, help_text)
