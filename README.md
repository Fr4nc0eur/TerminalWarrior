# CLI Linux Lab (FileSystem-CTF)
A containerized command-line cybersecurity challenge built in Python, simulating a Linux terminal where players solve hacking-style puzzles using real Linux commands.

##  Overview
**CLI Linux Lab** is an interactive command-line training game where players explore a simulated Linux filesystem to uncover hidden flags, passwords, and secrets using real terminal commands.

## ✨ Features
- 🟦 **Linux-style terminal simulation** (Python-only)
- 🧩 **Multiple levels with increasing difficulty**
- 💻 **Realistic commands** (`ls`, `cat`, `cd`, `chmod`, `sudo`, etc.)
- 📌 **Progress tracking with challenge checklist**
- 🐳 **Full Docker support** (no installations required)
- 🖥️ **Cross-platform** — Windows, macOS, Linux

## Levels Overview
- |1| Intro Challenge | Explore directories and find hidden files | Basic Linux commands ('ls', 'cat', 'cd', 'pwd', 'whoami') |
- |2| Permissions & Ownership | Learn how to view and modify file permissions | 'chmod', 'chown', 'sudo', file modes |
- |3| Searching the system *(COMING SOON)* | Find hidden files and analyze logs | 'grep', 'find', 'less', 'head', 'tail' |
- |4| Networking Challenge *(COMING SOON)* | Discover hosts and services | 'ping', 'netcat', 'curl', 'ssh' |
- |5| Cryptography & Decoding *(COMING SOON)* | Decode hidden messages and hash files | base64, hashing, simple ciphers |

## Installation & Setup

---

### 🐧 Run Locally for Linux (Without Docker)

```bash
#### Step 1: Clone the repo
git clone https://github.com/Ban5hee-GH/FileSystem-CTF.git

#### Step 2: Enter the project repo
cd FileSystem-CTF

#### Step 3: Install dependencies
pip install -r requirements.txt

#### step 4: Run the CLI Lab
python -m cli_lab.main

### 🪟 Run Locally for Windows (Withour Docker)

#### Step 1: Clone the repo
git clone https://github.com/Ban5hee-GH/FileSystem-CTF.git
#### Step 2: Enter the project
cd FileSystem-CTF

#### Step 3: Install dependencies
pip install -r requirements.txt

#### Step 4: Run the CLI Lab
python -m cli_lab.main


### 🐳 Run With Docker (Recommended)

#### Step 1: Build Docker image
 docker build -t cli-lab -f docker/Dockerfile .
#### Step 2: Run the containter interactively
 docker run -it cli-lab
