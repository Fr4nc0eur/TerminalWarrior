"""Virtual Linux Filesystem Simulator"""

import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class FileNode:
    """Represents a file or directory in the virtual filesystem"""
    
    def __init__(self, name: str, is_dir: bool = False, owner: str = "root", 
                 permissions: str = "644", content: str = ""):
        self.name = name
        self.is_dir = is_dir
        self.owner = owner
        self.permissions = permissions  # e.g., "644" or "755"
        self.content = content
        self.created_time = datetime.now()
        self.modified_time = datetime.now()
        self.children: Dict[str, 'FileNode'] = {} if is_dir else {}
        self.parent: Optional['FileNode'] = None
        self.symlink_target: Optional[str] = None
    
    def is_readable(self, user: str) -> bool:
        """Check if file is readable by user"""
        if user == self.owner:
            return self.permissions[0] in ['4', '5', '6', '7']
        return self.permissions[2] in ['4', '5', '6', '7']
    
    def is_writable(self, user: str) -> bool:
        """Check if file is writable by user"""
        if user == self.owner:
            return self.permissions[0] in ['2', '3', '6', '7']
        return self.permissions[2] in ['2', '3', '6', '7']
    
    def is_executable(self, user: str) -> bool:
        """Check if file is executable by user"""
        if user == self.owner:
            return self.permissions[0] in ['1', '3', '5', '7']
        return self.permissions[2] in ['1', '3', '5', '7']
    
    def get_size(self) -> int:
        """Get file size in bytes"""
        if self.is_dir:
            return 4096
        return len(self.content.encode('utf-8'))
    
    def add_child(self, name: str, node: 'FileNode') -> None:
        """Add child node to directory"""
        if self.is_dir:
            node.parent = self
            self.children[name] = node
    
    def get_child(self, name: str) -> Optional['FileNode']:
        """Get child node by name"""
        return self.children.get(name)
    
    def list_children(self) -> List[Tuple[str, 'FileNode']]:
        """List all children"""
        return sorted(self.children.items())


class VirtualFilesystem:
    """Simulated Linux filesystem"""
    
    def __init__(self):
        self.root = FileNode("/", is_dir=True, owner="root", permissions="755")
        self.current_user = "player"
        self.current_dir = self.root
        self._initialize_filesystem()
    
    def _initialize_filesystem(self) -> None:
        """Initialize filesystem with default structure"""
        # Create standard Linux directories
        dirs = [
            ("bin", "root", "755"),
            ("etc", "root", "755"),
            ("home", "root", "755"),
            ("tmp", "root", "777"),
            ("var", "root", "755"),
            ("root", "root", "700"),
        ]
        
        for dir_name, owner, perms in dirs:
            node = FileNode(dir_name, is_dir=True, owner=owner, permissions=perms)
            self.root.add_child(dir_name, node)
        
        # Create home directory structure
        home = self.root.get_child("home")
        player_home = FileNode("player", is_dir=True, owner="player", permissions="755")
        if home is not None:
            home.add_child("player", player_home)
        
        # Create root's home
        root_home = self.root.get_child("root")
        if root_home is not None:
            root_home.add_child(".ssh", FileNode(".ssh", is_dir=True, owner="root", permissions="700"))
        
        # Add some files
        etc = self.root.get_child("etc")
        if etc is not None:
            etc.add_child("passwd", FileNode("passwd", owner="root", permissions="644", 
                         content="root:x:0:0:root:/root:/bin/bash\nplayer:x:1000:1000:player:/home/player:/bin/bash\n"))
            etc.add_child("shadow", FileNode("shadow", owner="root", permissions="640",
                         content="root:$6$hash:18000:0:99999:7:::\nplayer:$6$hash:18000:0:99999:7:::\n"))
        
        player_home.add_child("notes.txt", FileNode("notes.txt", owner="player", permissions="644",
                             content="Remember: The password is hidden in the log files\n"))
        player_home.add_child("secret.txt", FileNode("secret.txt", owner="player", permissions="600",
                             content="Confidential data here\n"))
        
        # Create tmp files
        tmp = self.root.get_child("tmp")
        if tmp is not None:
            tmp.add_child("log.txt", FileNode("log.txt", owner="root", permissions="644",
                         content="[2025-11-15] User login attempt\n[2025-11-15] Password: hidden_flag_123\n"))
        
        # Create bin files
        bin_dir = self.root.get_child("bin")
        if bin_dir is not None:
            bin_dir.add_child("ls", FileNode("ls", owner="root", permissions="755",
                             content="#!/bin/bash\n# List command"))
            bin_dir.add_child("cat", FileNode("cat", owner="root", permissions="755",
                             content="#!/bin/bash\n# Cat command"))
    
    def get_path(self, node: FileNode) -> str:
        """Get absolute path of a node"""
        if node == self.root:
            return "/"
        parts = []
        current = node
        while current and current != self.root:
            parts.append(current.name)
            current = current.parent
        return "/" + "/".join(reversed(parts))
    
    def navigate_to(self, path: str) -> Optional[FileNode]:
        """Navigate to a path and return the node"""
        if path == "/":
            return self.root
        
        if path.startswith("/"):
            current = self.root
            parts = path.strip("/").split("/")
        else:
            current = self.current_dir
            parts = path.split("/")
        
        for part in parts:
            if part == "." or part == "":
                continue
            elif part == "..":
                if current.parent:
                    current = current.parent
            else:
                next_node = current.get_child(part)
                if next_node is None:
                    return None
                current = next_node
        
        return current
    
    def change_directory(self, path: str) -> bool:
        """Change current directory"""
        node = self.navigate_to(path)
        if node and node.is_dir and node.is_readable(self.current_user):
            self.current_dir = node
            return True
        return False
    
    def create_file(self, name: str, content: str = "", owner: str = "player", permissions: str = "644") -> bool:
        """Create a file in current directory"""
        
        if name in self.current_dir.children:
            return False
        
        node = FileNode(name, is_dir=False, owner=owner, permissions=permissions, content=content)
        self.current_dir.add_child(name, node)
        return True
    
    def create_directory(self, name: str) -> bool:
        """Create a directory in current directory"""
        if name in self.current_dir.children:
            return False
        
        node = FileNode(name, is_dir=True, owner=self.current_user, permissions="755")
        self.current_dir.add_child(name, node)
        return True
    
    def delete_file(self, name: str) -> bool:
        """Delete a file in current directory"""
        if name in self.current_dir.children:
            del self.current_dir.children[name]
            return True
        return False
    
    def chmod(self, name: str, permissions: str) -> bool:
        """Change file permissions"""
        node = self.current_dir.get_child(name)
        if node:
            node.permissions = permissions
            return True
        return False
