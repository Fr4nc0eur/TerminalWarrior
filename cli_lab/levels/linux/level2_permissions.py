import random

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Read /home/user/locked.log.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Gain access to /srv/team/shared_notes.txt.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Use /var/shared (sticky dir) to create proof.txt.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Execute a misconfigured helper script that runs with elevated privileges.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Fix a file owned by nobody so a service can start.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Locate a SUID binary and use it to read a sensitive file.",
        "",
    ]

def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)

def main():
    challenge_state = {i: False for i in range(1, 7)}

    print("Type command 'challenge' to see your progress.\n")
    input("Press Enter to start...")

    # Random MOTD bits
    processes = random.randint(100, 200)
    memoryusage = random.randint(100, 800)
    time1 = random.randint(1, 24)
    time2 = random.randint(10, 59)
    time3 = random.randint(10, 59)
    day = random.randint(1, 28)
    ip_parts = [str(random.randint(1, 254)) for _ in range(4)]
    ip_address = ".".join(ip_parts)

    print("\nWelcome to the Linux CLI Flag challenge LEVEL 2 (Permissions) made by (Ban5hee)\n")
    input("Press Enter to continue...")
    print()

    print_challenges(challenge_state)
    print("\nWelcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-91-generic x86_64)\n")
    print("* Documentation: https://help.ubuntu.com")
    print("* Management:    https://landscape.canonical.com")
    print("* Support:       https://ubuntu.com/advantage\n")
    print(f"System information as of [Thu Oct {day} {time1:02d}:{time2:02d}:{time3:02d} UTC 2025]\n")
    print(f"System load: 0.00               Processes:          {processes}")
    print("Usage of /:   20.75% of 49.11GB  Users logged in:     1")
    print(f"Memory usage: {memoryusage}MB             IP address for eth0: {ip_address}")
    print("Swap usage:   0%\n")
    print("0 updates can be applied immediately\n")
    print("Last Login: Thu Oct 4 16:00:00 UTC 2025\n")

    current_directory = "/home/user"

    locked_log_unlocked = False
    shared_accessed = False
    proof_created = False
    helper_ran = False
    config_fixed = False
    suid_found = False
    suid_used = False

    def print_help():
        print("Available commands:")
        print("  help                - Show this help message")
        print("  ls / ls -l          - List files (long format shows permissions/owners)")
        print("  cd <dir>            - Change directory (home, srv, /srv/team, /var/shared, /etc/service)")
        print("  pwd                 - Print current directory")
        print("  whoami              - Show current user")
        print("  cat <file>          - Read file contents (may be permission denied!)")
        print("  touch <file>        - Create empty file (used in /var/shared)")
        print("  sudo ...            - Simulated sudo for certain commands")
        print("  helper_script       - Run the misconfigured helper script")
        print("  find / -perm -4000  - Find SUID binaries (simulated)")
        print("  suid_tool           - Run the simulated SUID binary")
        print("  challenge           - Show challenge progress")
        print("  exit                - Exit level 2")

    def print_ls(directory, long=False):
        if directory == "/home/user":
            if not long:
                print("locked.log  Documents  srv  var  etc")
            else:
                print("total 5")
                print("-rw------- 1 root   root   120 Oct  4 15:00 locked.log")
                print("drwxr-xr-x 2 user   user  4096 Oct  4 15:00 Documents")
                print("drwxr-xr-x 3 root   root  4096 Oct  4 15:00 srv")
                print("drwxrwxrwt 2 root   root  4096 Oct  4 15:00 var")
                print("drwxr-xr-x 3 root   root  4096 Oct  4 15:00 etc")
        elif directory == "/home/user/Documents":
            if not long:
                print("notes.txt  permissions_tips.txt")
            else:
                print("total 2")
                print("-rw-r--r-- 1 user user 220 Oct  4 15:01 notes.txt")
                print("-rw-r--r-- 1 user user 420 Oct  4 15:01 permissions_tips.txt")
        elif directory == "/srv/team":
            if not long:
                print("shared_notes.txt")
            else:
                print("total 1")
                print("-rw-r----- 1 admin investigators 350 Oct  4 15:02 shared_notes.txt")
        elif directory == "/var/shared":
            if not long:
                if proof_created:
                    print("proof.txt")
                else:
                    print("")
            else:
                print("drwxrwxrwt 2 root shared 4096 Oct  4 15:03 .")
                print("drwxr-xr-x 3 root root   4096 Oct  4 15:00 ..")
                if proof_created:
                    print("-rw-r--r-- 1 user user   10 Oct  4 15:05 proof.txt")
        elif directory == "/etc/service":
            if not long:
                print("config.json")
            else:
                owner = "service" if config_fixed else "nobody"
                group = owner
                print("total 1")
                print(f"-rw-r--r-- 1 {owner} {group} 180 Oct  4 15:02 config.json")
        else:
            if not long:
                print("")
            else:
                print("total 0")

    while True:
        prompt = f"user@linux:{current_directory}$ "
        command = input(prompt).strip()

        if command == "":
            continue

        if command == "exit":
            print("logout")
            break

        if command == "challenge":
            print()
            print_challenges(challenge_state)
            print()
            continue

        if command == "help":
            print_help()
            continue

        if command == "pwd":
            print(current_directory)
            continue

        if command == "whoami":
            print("user")
            continue

        if command.startswith("cd "):
            target = command[3:].strip()
            if target in ("~", "/home/user"):
                current_directory = "/home/user"
            elif target in ("Documents", "/home/user/Documents"):
                current_directory = "/home/user/Documents"
            elif target in ("srv", "/srv"):
                current_directory = "/srv"
            elif target in ("/srv/team", "team") and current_directory in ("/srv", "/home/user"):
                current_directory = "/srv/team"
            elif target in ("/var/shared", "shared") and current_directory in ("/var", "/home/user"):
                current_directory = "/var/shared"
            elif target in ("var", "/var"):
                current_directory = "/var"
            elif target in ("/etc/service", "service") and current_directory in ("/etc", "/home/user"):
                current_directory = "/etc/service"
            elif target in ("etc", "/etc"):
                current_directory = "/etc"
            elif target == "..":

                if current_directory == "/home/user":
                    pass
                elif current_directory.startswith("/home/user/"):
                    current_directory = "/home/user"
                elif current_directory in ("/srv", "/var", "/etc"):
                    current_directory = "/home/user"
                elif current_directory.startswith("/srv/"):
                    current_directory = "/srv"
                elif current_directory.startswith("/var/"):
                    current_directory = "/var"
                elif current_directory.startswith("/etc/"):
                    current_directory = "/etc"
            else:
                print(f"cd: no such file or directory: {target}")
            continue

        if command == "ls":
            print_ls(current_directory, long=False)
            continue

        if command == "ls -l":
            print_ls(current_directory, long=True)
            continue

        if command.startswith("touch "):
            filename = command[6:].strip()
            if current_directory == "/var/shared" and filename == "proof.txt":
                if not proof_created:
                    proof_created = True
                    if not challenge_state[3]:
                        challenge_state[3] = True
                        print("Created proof.txt in sticky dir /var/shared.")
                        print("You completed challenge 3! Type 'challenge' to see your progress.")
                else:
                    print("proof.txt already exists.")
            else:
                print(f"touch: cannot touch '{filename}': Permission denied (simulated)")
            continue

        if command.startswith("sudo "):
            sudo_cmd = command[5:].strip()

            if sudo_cmd.startswith("cat "):
                target = sudo_cmd[4:].strip()
                if target in ("locked.log", "/home/user/locked.log"):
                    print("Root-only log contents: You found the first permissions clue.")
                    print("CLUE: Groups and permissions matter. Check /srv/team next.")
                    locked_log_unlocked = True
                    if not challenge_state[1]:
                        challenge_state[1] = True
                        print("You completed challenge 1! Type 'challenge' to see your progress.")
                elif target in ("shared_notes.txt", "/srv/team/shared_notes.txt"):
                    if not shared_accessed:
                        shared_accessed = True
                        if not challenge_state[2]:
                            challenge_state[2] = True
                        print("You read /srv/team/shared_notes.txt:")
                        print("NOTE: Only members of 'investigators' should read this.")
                        print("CLUE: Misconfigured scripts and SUID tools can be dangerous...")
                    else:
                        print("You read /srv/team/shared_notes.txt again.")
                elif target in ("config.json", "/etc/service/config.json"):
                    print("Directly reading config.json as root shows:")
                    print("service_enabled=true")
                else:
                    print(f"sudo: cat: {target}: No such file (simulated)")

            elif sudo_cmd.startswith("chown"):
                if "service:service" in sudo_cmd and "config.json" in sudo_cmd:
                    if not config_fixed:
                        config_fixed = True
                        if not challenge_state[5]:
                            challenge_state[5] = True
                        print("You fixed ownership of /etc/service/config.json to service:service.")
                        print("The service can now start successfully.")
                    else:
                        print("Ownership already fixed.")
                else:
                    print("sudo: chown: operation not permitted (simulated)")
            else:
                print("sudo: command not supported in this simulation.")
            continue

        if command.startswith("cat "):
            filename = command[4:].strip()

            if current_directory == "/home/user":
                if filename == "locked.log":
                    print("cat: locked.log: Permission denied (try using sudo).")
                elif filename == "Bin.txt":
                    print("Just some random binary notes... 01010101")
                elif filename == "Flag":
                    print("No such file or directory.")
                else:
                    print(f"cat: {filename}: No such file")
            elif current_directory == "/home/user/Documents":
                if filename == "notes.txt":
                    print("Remember: 'ls -l' shows permissions. 'rwx' bits matter.")
                elif filename == "permissions_tips.txt":
                    print("Tips:")
                    print("- Use 'sudo' to act as root for specific commands.")
                    print("- Group permissions (like 'investigators') control access.")
                    print("- Sticky bit on /var/shared prevents others from deleting your files.")
                else:
                    print(f"cat: {filename}: No such file")
            elif current_directory == "/srv/team":
                if filename == "shared_notes.txt":
                    print("cat: shared_notes.txt: Permission denied (try 'sudo cat').")
                else:
                    print(f"cat: {filename}: No such file")
            elif current_directory == "/var/shared":
                if filename == "proof.txt":
                    if proof_created:
                        print("Proof file found. System will pick this up for review.")
                    else:
                        print("cat: proof.txt: No such file")
                else:
                    print(f"cat: {filename}: No such file")
            elif current_directory == "/etc/service":
                if filename == "config.json":
                    owner = "service" if config_fixed else "nobody"
                    print(f"{{'owner':'{owner}', 'service_enabled':false}}")
                    if not config_fixed:
                        print("Log: service cannot start due to incorrect file ownership.")
                    else:
                        print("Log: service started successfully.")
                else:
                    print(f"cat: {filename}: No such file")
            else:
                print(f"cat: {filename}: No such file")
            continue

        if command == "helper_script":
            print("Running helper_script with elevated privileges (simulated SUID root)...")
            print("Helper script outputs: 'Only root should see this secret token: PERM-HELPER-ROOT-TOKEN'")
            helper_ran = True
            if not challenge_state[4]:
                challenge_state[4] = True
                print("You completed challenge 4! Type 'challenge' to see your progress.")
            continue

        if command.startswith("find "):
            if command.strip() == "find / -perm -4000 -type f 2>/dev/null":
                print("/usr/bin/suid_tool")
                suid_found = True
            else:
                print("find: no results (this simulation only supports 'find / -perm -4000 -type f 2>/dev/null')")
            continue

        if command == "suid_tool":
            if not suid_found:
                print("bash: suid_tool: command not found (try finding it first with 'find').")
            else:
                if not suid_used:
                    suid_used = True
                    if not challenge_state[6]:
                        challenge_state[6] = True
                    print("Running suid_tool as root (simulated)...")
                    print("Root-only file contents: FINAL PERMISSIONS FLAG: PERM-LEVEL2-COMPLETE")
                    print("You completed challenge 6! Type 'challenge' to see your progress.")
                else:
                    print("suid_tool already used. Root-only data already exposed.")
            continue

        print(f"{command}: command not found")

if __name__ == "__main__":
    main()
