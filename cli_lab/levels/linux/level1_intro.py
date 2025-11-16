import random

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Read the Flag.txt.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Find the ssh username for other computer.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Find the ssh password for other computer.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Find the ssh IP address for other computer.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Successfully ssh into other computer.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Find hidden.txt and read it on other computer.",
        "",
    ]

def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)

def main():

    challenge_state = {i: False for i in range(1, 7)}

    print("Type command 'challenge' to see your progress.\n")
    input("Press Enter to start...")


    processes = random.randint(100, 200)
    memoryusage = random.randint(100, 800)
    time1 = random.randint(1, 24)
    time2 = random.randint(10, 59)
    time3 = random.randint(10, 59)
    day = random.randint(1, 28)
    ip_parts = [str(random.randint(1, 254)) for _ in range(4)]
    other_ip_address = ".".join(ip_parts)
    ip_address = ".".join(ip_parts)

    print("\nWelcome to the Linux CLI Flag Challenge level 1 (INTRO) made by (Ban5hee)\n")
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
    print("Last Login: Thu Oct 3 12:00:00 UTC 2025\n")


    current_directory = "~"
    ssh_username = ['JoeBiden', 'DonaldTrump', 'JeremyClarkson', 'RichardHammond', 'JamesMay', 'GordonRamsay', 'ColdPlay', 'JeffreyDahmer', 'HarryPotter', 'KimJongUn']
    ssh_password = ['DumbassLeftHisPassword', 'Password123!', 'ILeftMyKeysAgain', 'Admin1234', 'qwerty_is_bad', 'LetMeInPlease', 'Eggcellent123', 'Passw0rd!', 'ThisIsNotASecurePass', 'ForgottenPassword69',]
    randomusername = random.choice(ssh_username)
    randompassword = random.choice(ssh_password)
    on_remote = False

    while True:
        if on_remote:
            prompt = f"ban5hee@linux-remote:~$ "
        else:
            prompt = f"user@linux:{current_directory}$ "

        command = input(prompt).strip()


        if command == "exit":

            if on_remote:
                print("Logging out of remote machine.")
                on_remote = False
                continue
            print("logout")
            break

        if command == "challenge":
            print()
            print_challenges(challenge_state)
            print()
            continue

        if not on_remote:

            if command == "ls":
                if current_directory == "~":
                    print("Bin.txt  Flag  notes.txt  Documents")
                elif current_directory == "~/Flag":
                    print("Flag.txt  something.txt  birthday.txt")
                elif current_directory == "~/Documents":
                    print("ssh_Username.txt  ssh_Password.txt")
            elif command == "pwd":
                print("/home/user" + ("" if current_directory == "~" else current_directory[1:]))
            elif command == "whoami":
                print("user")
            elif command == "cd Flag":
                current_directory = "~/Flag"
            elif command == "cd Documents":
                current_directory = "~/Documents"
            elif command == "cd ..":
                current_directory = "~"
            elif command.startswith("cat "):
                filename = command[4:]

                if current_directory == "~":
                    if filename == "notes.txt":
                        print(f"The ssh IP address for the other computer is {other_ip_address}")
                        if not challenge_state[4]:
                            challenge_state[4] = True
                            print("You completed challenge 4! Type 'challenge' to see your progress.")
                    elif filename == "Bin.txt":
                        print("Just some random binary notes...")
                    else:
                        print(f"cat: {filename}: No such file")
                elif current_directory == "~/Flag":
                    if filename == "Flag.txt":
                        print("You completed challenge 1! Type 'challenge' to see your progress.")
                        challenge_state[1] = True
                    elif filename == "birthday.txt":
                        print("Happy Birthday John!")
                    elif filename == "something.txt":
                        print("I don't know what to put here.")
                    else:
                        print(f"cat: {filename}: No such file")
                elif current_directory == "~/Documents":
                    if filename == "ssh_Username.txt":
                        print("You found the ssh_Username.txt!")
                        print("Username:", randomusername)
                        if not challenge_state[2]:
                            challenge_state[2] = True
                            print("You completed challenge 2! Type 'challenge' to see your progress.")
                    elif filename == "ssh_Password.txt":
                        print("You found the ssh_Password.txt!")
                        print("Password:", randompassword)
                        if not challenge_state[3]:
                            challenge_state[3] = True
                            print("You completed challenge 3! Type 'challenge' to see your progress.")
                    else:
                        print(f"cat: {filename}: No such file")
                else:
                    print(f"cat: {filename}: No such file")
            elif command.startswith("ssh"):
                print("Attempting to ssh into other computer...")
                user_input = input("Username: ").strip()
                password_input = input("Password: ").strip()

                if user_input == randomusername and password_input == randompassword:
                    print("Correct credentials. Successfully ssh'd into other computer.")
                    on_remote = True
                    if not challenge_state[5]:
                        challenge_state[5] = True
                        print("You completed challenge 5! Type 'challenge' to see your progress.")
                else:
                    print("Authentication failed.")
            elif command == "":
                continue
            else:
                print(f"{command}: command not found")
        else:
            if command == "ls":
                print("Use -la to find the hidden.txt")
            elif command == "ls -la":
                print(".  ..  hidden.txt")
            elif command == "cat hidden.txt":
                print("You found the hidden.txt! You completed challenge 6!")
                if not challenge_state[6]:
                    challenge_state[6] = True
                    print("Type 'challenge' to see your progress.")
            elif command == "":
                continue
            else:
                print(f"{command}: command not found on remote")

if __name__ == "__main__":
    main()
