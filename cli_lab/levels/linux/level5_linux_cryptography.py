import random
import pyfiglet
import hashlib
import base64

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Run 'echo \"secret\" | md5sum' to calculate MD5 hash.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Run 'openssl enc -aes-256-cbc -in secret.txt -out encrypted.bin' to encrypt a file.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Run 'openssl enc -aes-256-cbc -d -in encrypted.bin -out decrypted.txt' to decrypt a file.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Run 'sha256sum secret.txt' to calculate SHA256 hash.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Run 'openssl rand -hex 32' to generate a random key.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Run 'gpg --symmetric secret.txt' to encrypt with GPG.",
        "",
        f"{'✅' if state[7] else '◻️'} 7) Run 'gpg --decrypt secret.txt.gpg' to decrypt with GPG."
        "",
    ]

def print_help():
    print(" help - Display this help menu")
    print(" challenge - Display the current challenges")
    print(" exit - Exit the terminal")
    print(" md5sum <file> - Calculate MD5 hash")
    print(" sha256sum <file> - Calculate SHA256 hash")
    print(" openssl enc -aes-256-cbc -in <input> -out <output> -encrypt -k <password>")
    print(" openssl enc -aes-256-cbc -d -in <input> -out <output> -k <password>")
    print(" openssl rand -hex 32 - Generate random hex key")
    print(" gpg --symmetric <file> - Encrypt with GPG")
    print(" gpg --decrypt <file> - Decrypt with GPG")
    print(" pwd - Print Working Directory")
    print(" whoami - Display current user")

def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)

def main():
    challenge_state = {i: False for i in range(1, 8)}
    
    processes = random.randint(100, 200)
    memoryusage = random.randint(50, 150)
    time1 = random.randint(1, 24)
    time2 = random.randint(10, 59)
    time3 = random.randint(10, 59)
    day = random.randint(1, 28)
    ip_parts = [str(random.randint(10, 100)) for _ in range(4)]
    ip_address = ".".join(ip_parts)

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="slant")
    print(ascii_banner)
    print("\nWelcome to Challenge level 5 (CRYPTOGRAPHY) made by (Diversion/diverter)\n")
    print("type 'help' and 'challenge' to access help menu and view challenges.")
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
    test_file_content = "This is a secret message for cryptographic operations.\nIt contains confidential information that needs protection."
    
    import os
    if not os.path.exists("secret.txt"):
        with open("secret.txt", "w") as f:
            f.write(test_file_content)
    
    if not os.path.exists("encrypted.bin"):
        with open("encrypted.bin", "wb") as f:
            f.write(b"Encrypted data placeholder")
    
    if not os.path.exists("secret.txt.gpg"):
        with open("secret.txt.gpg", "wb") as f:
            f.write(b"GPG encrypted data placeholder")

    while True:
        prompt = f"user@linux:{current_directory}$ "
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

        if cmd == "md5sum":
            if len(args) < 1:
                print("Usage: md5sum <file>")
                continue
            filename = args[0]
            if filename == "secret.txt":
                md5_hash = hashlib.md5(test_file_content.encode()).hexdigest()
                print(f"{md5_hash}  {filename}")
                if not challenge_state[1]:
                    challenge_state[1] = True
                    print("\nYou completed challenge 1! Type 'challenge' to see your progress.")
            else:
                print(f"md5sum: {filename}: No such file or directory")
            continue

        if cmd == "sha256sum":
            if len(args) < 1:
                print("Usage: sha256sum <file>")
                continue
            filename = args[0]
            if filename == "secret.txt":
                sha256_hash = hashlib.sha256(test_file_content.encode()).hexdigest()
                print(f"{sha256_hash}  {filename}")
                if not challenge_state[4]:
                    challenge_state[4] = True
                    print("You completed challenge 4! Type 'challenge' to see your progress.")
            else:
                print(f"sha256sum: {filename}: No such file or directory")
            continue

        if cmd == "openssl":
            if len(args) < 3:
                print("Usage: openssl enc -aes-256-cbc -in <input> -out <output> [-encrypt|-decrypt] -k <password>")
                continue
            
            action = None
            infile = None
            outfile = None
            password = None
            
            i = 0
            while i < len(args):
                if args[i] == "-in":
                    infile = args[i+1] if i+1 < len(args) else None
                elif args[i] == "-out":
                    outfile = args[i+1] if i+1 < len(args) else None
                elif args[i] == "-encrypt" or args[i] == "-e":
                    action = "encrypt"
                elif args[i] == "-decrypt" or args[i] == "-d":
                    action = "decrypt"
                elif args[i] == "-k":
                    password = args[i+1] if i+1 < len(args) else None
                i += 1
            
            if infile and outfile and action:
                if action == "encrypt":
                    print("Loading 'secret.txt' into memory...")
                    print("Generating key from password...")
                    print("Encrypting data...")
                    print("Writing encrypted data to 'encrypted.bin'")
                    if not challenge_state[2]:
                        challenge_state[2] = True
                        print("You completed challenge 2! Type 'challenge' to see your progress.")
                elif action == "decrypt":
                    print("Loading 'encrypted.bin' into memory...")
                    print("Decrypting data...")
                    print("Writing decrypted data to 'decrypted.txt'")
                    if not challenge_state[3]:
                        challenge_state[3] = True
                        print("You completed challenge 3! Type 'challenge' to see your progress.")
            else:
                print("Usage: openssl enc -aes-256-cbc -in <input> -out <output> [-encrypt|-decrypt] -k <password>")
            continue

        if cmd == "openssl" and len(args) >= 1 and args[0] == "rand":
            if len(args) >= 2 and args[1] == "-hex":
                print("Generating 32-byte random key...")
                import secrets
                key = secrets.token_hex(32)
                print(key)
                if not challenge_state[5]:
                    challenge_state[5] = True
                    print("You completed challenge 5! Type 'challenge' to see your progress.")
            else:
                print("Usage: openssl rand -hex 32")
            continue

        if cmd == "gpg":
            if len(args) < 1:
                print("Usage: gpg --symmetric <file> or gpg --decrypt <file>")
                continue
            
            action = args[0]
            if action == "--symmetric" and len(args) > 1:
                filename = args[1]
                if filename == "secret.txt":
                    print("gpg: CAST5 encrypted data")
                    print("gpg: encrypted with 1 passphrase")
                    if not challenge_state[6]:
                        challenge_state[6] = True
                        print("You completed challenge 6! Type 'challenge' to see your progress.")
                else:
                    print(f"gpg: {filename}: No such file or directory")
            elif action == "--decrypt" and len(args) > 1:
                filename = args[1]
                if filename == "secret.txt.gpg":
                    print("gpg: encrypted with 1 passphrase")
                    print("gpg: decryption successful")
                    if not challenge_state[7]:
                        challenge_state[7] = True
                        print("You completed challenge 7! Type 'challenge' to see your progress.")
                else:
                    print(f"gpg: {filename}: No such file or directory")
            else:
                print("Usage: gpg --symmetric <file> or gpg --decrypt <file>")
            continue

        if cmd == "pwd":
            print("/home/user")
            continue

        if cmd == "whoami":
            print("user")
            continue

        print(f"{cmd}: command not found")

if __name__ == "__main__":
    main()