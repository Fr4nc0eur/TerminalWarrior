import random
import pyfiglet


def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Use ls -la to find locked file hidden_data.txt.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Use read to identify the permissions of hidden_data.txt.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Use su to switch user to root.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Use chown to change owner of hidden_data.txt to user.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Now try to read hidden_data.txt again and confirm access.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Run ls to find HelloWorld.exe and run read on HelloWorld.exe.",
        "",
        f"{'✅' if state[7] else '◻️'} 7) Run su to switch to root, chmod HelloWorld.exe to 777, then read it again to finish the challenge.",
        "",
    ]


def print_help():
    print(" help - Display this help menu")
    print(" challenge - Display the list of challenges and your progress")
    print(" exit - Exit the terminal")
    print(" ls - list files in current directory")
    print(" ls -la - list all files and permissions")
    print(" read <file> - Read a file or inspect its permissions")
    print(" cat <file> - Alias for read")
    print(" pwd - Print Working Directory")
    print(" whoami - Displays the current user")
    print(" su <username> - Switch user")
    print(" chmod <octal> <file> - Change file permissions, find out more about octal permissions at https://www.linux.com/training-tutorials/understanding-linux-file-permissions/")
    print(" chown <username> <file> - Modify file ownership")


def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)


def main():

    challenge_state = {i: False for i in range(1, 8)}

    processes = random.randint(100, 200)
    memoryusage = random.randint(100, 800)
    time1 = random.randint(1, 24)
    time2 = random.randint(10, 59)
    time3 = random.randint(10, 59)
    day = random.randint(1, 28)
    ip_parts = [str(random.randint(1, 254)) for _ in range(4)]
    other_ip_address = ".".join(ip_parts)
    ip_address = ".".join(ip_parts)

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="small")
    print(ascii_banner)

    print("\nWelcome to level 2 (PERMISSIONS & OWNERSHIP) made by (Diversion/diversionsec)\n")
    print("type the commands 'help' and 'challenge' to access help menu and view challenges.")
    input("Press Enter to continue...")
    print("")

    print_challenges(challenge_state)
    print("\nWelcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-91-generic x86_64)\n")
    print("* Documentation: https://help.ubuntu.com")
    print("* Management:    https://landscape.canonical.com")
    print("* Support:       https://ubuntu.com/advantage\n")
    print(
        f"System information as of [Thu Oct {day} {time1:02d}:{time2:02d}:{time3:02d} UTC 2025]\n")
    print(f"System load: 0.00               Processes:          {processes}")
    print("Usage of /:   20.75% of 49.11GB  Users logged in:     1")
    print(
        f"Memory usage: {memoryusage}MB             IP address for eth0: {ip_address}")
    print("Swap usage:   0%\n")
    print("0 updates can be applied immediately\n")
    print("Last Login: Thu Oct 3 12:00:00 UTC 2025\n")

    current_directory = "~"
    current_user = "user"
    root_password = "toor"

    hidden_data_owner = "root"
    hidden_data_group = "root"
    hidden_data_perms = "rw-r-----"

    helloworld_owner = "root"
    helloworld_group = "root"
    helloworld_perms = "rwx------"

    while True:

        prompt = f"{current_user}@linux:{current_directory}$ "
        command = input(prompt).strip()
        if not command:
            continue

        parts = command.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == "help":
            print_help()
            continue

        if cmd == "challenge":
            print()
            print_challenges(challenge_state)
            print()
            continue

        if cmd == "exit":
            print("Goodbye")
            break

        if cmd == "ls":
            if len(args) == 0:
                print("HelloWorld.exe")
            elif args == ["-la"] or args == ["-l", "-a"]:
                print("drwxr-xr-x  2 user user 4096 Oct  3 12:00 .")
                print("drwxr-xr-x 10 user user 4096 Oct  3 12:00 ..")
                print(f"-rw-r-----  1 {hidden_data_owner} {hidden_data_group}   32 Oct  3 12:00 hidden_data.txt")
                print(f"-rw-r--r--  1 root root   16 Oct  3 12:00 root_password.txt")
                print(f"-{helloworld_perms}  1 {helloworld_owner} {helloworld_group} 8765 Oct  3 12:00 HelloWorld.exe")
                if not challenge_state[1]:
                    challenge_state[1] = True
                    print("\nYou completed challenge 1! Type 'challenge' to see your progress.")
            else:
                print("ls: invalid option")
            continue

        if cmd in ["read", "cat"]:
            if len(args) == 0:
                print(f"{cmd}: missing file operand")
                continue
            filename = args[0]
            if filename == "hidden_data.txt":
                print(f"-{hidden_data_perms}  1 {hidden_data_owner} {hidden_data_group}   32 Oct  3 12:00 hidden_data.txt")
                if not challenge_state[2]:
                    challenge_state[2] = True
                    print("You completed challenge 2! Type 'challenge' to see your progress.")
                if current_user == "root" or hidden_data_owner == current_user:
                    print("Hidden data contents displayed.")
                    if current_user == "user" and hidden_data_owner == "user" and not challenge_state[5]:
                        challenge_state[5] = True
                        print("You completed challenge 5! Type 'challenge' to see your progress.")
                else:
                    print("Access denied: Permission denied.")
            elif filename == "root_password.txt":
                print("root: toor")
            elif filename == "HelloWorld.exe":
                print(f"-{helloworld_perms}  1 {helloworld_owner} {helloworld_group} 8765 Oct  3 12:00 HelloWorld.exe")
                if current_user == "user" and not challenge_state[6]:
                    challenge_state[6] = True
                    print("You completed challenge 6! Type 'challenge' to see your progress.")
                if current_user == "root" and helloworld_perms == "rwxrwxrwx":
                    print("HelloWorld.exe read successfully.")
                    if not challenge_state[7]:
                        challenge_state[7] = True
                        print("You completed challenge 7! Type 'challenge' to see your progress.")
                elif current_user == "root":
                    print("Access denied: File is not executable by all users.")
                else:
                    print("Access denied: Permission denied.")
            else:
                print(f"{cmd}: {filename}: No such file or directory")
            continue

        if cmd == "pwd":
            print("/home/user/Documents")
            continue

        if cmd == "whoami":
            print(current_user)
            continue

        if cmd == "su":
            if len(args) == 0:
                print("su: missing operand")
                continue
            target = args[0]
            if target == current_user:
                print(f"Already {current_user}.")
                continue
            if target == "root":
                password_input = input("Password: ").strip()
                if password_input == root_password:
                    current_user = "root"
                    print("Root access granted.")
                    if not challenge_state[3]:
                        challenge_state[3] = True
                        print("You completed challenge 3! Type 'challenge' to see your progress.")
                else:
                    print("Authentication failure")
            elif target == "user" and current_user == "root":
                current_user = "user"
                print("Switched to user.")
            else:
                print(f"su: user {target} does not exist")
            continue

        if cmd == "chown":
            if len(args) != 2:
                print("Usage: chown <username> <file>")
                continue
            if current_user != "root":
                print("chown: Permission denied")
                continue
            target_user, filename = args
            if filename != "hidden_data.txt":
                print(f"chown: cannot access '{filename}': No such file or directory")
                continue
            if target_user != "user":
                print(f"chown: invalid user: {target_user}")
                continue
            hidden_data_owner = "user"
            hidden_data_group = "user"
            print("Ownership of hidden_data.txt changed to user.")
            if not challenge_state[4]:
                challenge_state[4] = True
                print("You completed challenge 4! Type 'challenge' to see your progress.")
            continue

        if cmd == "chmod":
            if len(args) != 2:
                print("Usage: chmod <octal> <file>")
                continue
            if current_user != "root":
                print("chmod: Permission denied")
                continue
            mode, filename = args
            if filename != "HelloWorld.exe":
                print(f"chmod: cannot access '{filename}': No such file or directory")
                continue
            if mode != "777":
                print("chmod: invalid mode. Try 777.")
                continue
            helloworld_perms = "rwxrwxrwx"
            print("Permissions of HelloWorld.exe changed to 777.")
            continue

        print(f"{cmd}: command not found")


if __name__ == "__main__":
    main()
