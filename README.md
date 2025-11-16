S# TerminalWarrior
A containersized command-line cybersecurity challenge built in Python, simulating a Linux/Windows terminal where players solve hacking-style puzzles using real Linux/Windows commands.

##  Overview
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
- |1| Intro Challenge | Explore directories and find hidden files | Basic Linux commands ('ls', 'cat', 'cd', 'pwd', 'whoami') |
- |2| Permissions & Ownership | Learn how to view and modify file permissions | 'chmod', 'chown', 'sudo', file modes |
- |3| Searching the system *(COMING SOON)* | Find hidden files and analyze logs | 'grep', 'find', 'less', 'head', 'tail' |
- |4| Networking Challenge *(COMING SOON)* | Discover hosts and services | 'ping', 'netcat', 'curl', 'ssh' |
- |5| Cryptography & Decoding *(COMING SOON)* | Decode hidden messages and hash files | base64, hashing, simple ciphers |

### 🪟 Windows Terminal Levels:
- |1| Intro challenge *(COMING SOON)* | Navigate folders and uncover hidden files | Basic Window commands ('dir', 'cd', 'type', 'cls', 'echo') |
- |2| Permissions & Ownership *(COMING SOON)*| View and edit file rights | 'icals', 'attrib', 'takeown' |
- |3| Searching the System *(COMING SOON)*| Hunt for hiden files and read logs | 'findstr', 'where', 'tree' |
- |4| Networking Challenge *(COMING SOON)*| Scan the network and check services | 'ping', 'tracert' 'netstat', 'curl', 'ipconfig' |
- |5| Ctryptography & Decoding *(COMING SOON)*| Decode messages and inspect hashes | base64, certutil, simple ciphers |

## Installation & Setup

---

### 🐧 Run Locally for Linux (Without Docker)


#### Step 1: Clone the repo
```bash
git clone https://github.com/Ban5hee-GH/TerminalWarrior.git
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

### 🪟 Run Locally for Windows (Without Docker)

#### Step 1: Clone the repo
```bash
git clone https://github.com/Ban5hee-GH/TerminalWarrior.git
```
#### Step 2: Enter the project
```bash
cd FileSystem-CTF
```
#### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```
#### Step 4: Run the CLI Lab
```bash
python -m cli_lab.main
```

### 🐳 Run With Docker (Recommended)

#### Step 1: Build Docker image
```bash
 docker build -t cli-lab -f docker/Dockerfile .
```
#### Step 2: Run the containter interactively
```bash
 docker run -it cli-lab
```
