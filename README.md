<p align="center">
<img src="logo.gif">
</p>

A containersized command-line cybersecurity challenge built in Python, simulating a Linux/Windows terminal where players solve hacking-style puzzles using real Linux/Windows commands.

##  Overview ![Python](https://img.shields.io/badge/python-3.9%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green) [![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/diversionsec/TerminalWarrior) [![GitHub Stars](https://img.shields.io/github/stars/diversionsec/TerminalWarrior?style=social)](https://github.com/diversionsec/TerminalWarrior)
**TerminalWarrior** is an interactive command-line training game where players explore a simulated Linux/Windows filesystem to uncover hidden flags, passwords, and secrets using real terminal commands.

## ✨ Features
- 🟦 **Linux/Windows-style terminal simulation** (Python-only)
- 🧩 **Multiple levels with increasing difficulty**
- 💻 **Realistic commands** (`ls`, `cat`, `cd`, `chmod`, `sudo`, etc.)
- 📌 **Progress tracking with challenge checklist**
- 🐳 **Full Docker support** (no installations required)
- 🖥️ **Cross-platform** — Windows, macOS, Linux

## Levels Overview

---
### 🐧 Linux Terminal Levels:
1. **Intro Challenge**: Explore directories and find hidden files | Basic Linux commands `ls`, `cat`, `cd`, `pwd`, `whoami`
2. **Permissions & Ownership**: Learn how to view and modify file permissions | `chmod`, `chown`, `sudo`, `su`
3. **Searching the system**: Find hidden files and analyze logs | `grep`, `find`, `locate`, `which` `whereis`
4. **Networking Challenge**: Discover hosts and services | `ping`, `netcat`, `traceroute`, `nmap`
5. **Cryptography & Decoding**: Decode hidden messages and hash files | `base64`, `hashing`, `simple ciphers`

### 🪟 Windows Terminal Levels:
1. **Intro challenge**: Navigate folders and uncover hidden files | Basic Window commands `dir`, `cd`, `type`, `cls`, `echo`
2. **Permissions & Ownership**: View and edit file rights | `icals`, `attrib`, `takeown`
3. **Searching the System**: Hunt for hiden files and read logs | `findstr`, `where`, `tree`
4. **Networking Challenge**: Scan the network and check services | `ping`, `tracert`, `netstat`, `curl`, `ipconfig`
5. **Cryptography & Decoding**: Decode messages and inspect hashes | `base64`, `certutil`, `simple ciphers`
6. **Registry Deep Dive**: Navigate the Windows Registry to find hidden configuration keys
7. **Task Scheduler & Services**: Investigate scheduled tasks and services to find malicious activity
8. **Event Log Forensics**: Analyze Windows Event Logs to trace security incidents
9. **Disk Forensics & File Recovery**: Recover deleted files and analyze disk partitions
10. **PowerShell Scripting Challenge**: Use PowerShell to automate tasks and solve complex problems
## Installation & Setup 

----

### 🐧 Run Locally for Linux


#### Step 1: Clone the repo
```bash
git clone https://github.com/diversionsec/TerminalWarrior.git
```
#### Step 2: Enter the project repo
```bash
cd TerminalWarrior
```
#### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```
#### step 4: Run the CLI Lab
```bash
python -m cli_lab.main
```

### 🪟 Run Locally for Windows

#### Step 1: Clone the repo
```bash
git clone https://github.com/diversionsec/TerminalWarrior.git
```
#### Step 2: Enter the project
```bash
cd TerminalWarrior
```
#### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```
#### Step 4: Run the CLI Lab
```bash
python -m cli_lab.main
```
