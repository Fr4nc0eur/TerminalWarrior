import time
from .utils import (
    print_header,
    print_objectives,
    print_success,
    generic_cmd_handler,
    CURRENT_DIR,
    print_windows_motd,
    build_prompt,
)


def run_level():
    title = "LEVEL 2: PERMISSIONS & OWNERSHIP"
    objectives = [
        "The file 'secret.txt' is protected. Gain access to read it.",
        "Use ownership and ACL commands to unlock the file."
    ]
    hint = "Try: 'takeown /f secret.txt' then 'icacls secret.txt /grant user:(F)'."

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    current_dir = f"{CURRENT_DIR}\\Intel"
    ownership_taken = False
    permissions_granted = False
    hidden_revealed = False

    def list_dir(show_hidden=False):
        nonlocal hidden_revealed
        print(f" Directory of {current_dir}\n")
        print("02/20/2026  09:45 AM               512 brief.txt")
        if show_hidden:
            hidden_revealed = True
            print("02/20/2026  09:46 AM               768 secret.txt")
        print()

    while True:
        try:
            user_input = input(build_prompt(current_dir)).strip()
            parts = user_input.split()
            cmd = parts[0].lower() if parts else ""
            args = parts[1:]
            arg_str = " ".join(args)

            common = generic_cmd_handler(cmd, arg_str)
            if common == "EXIT":
                return False
            if common:
                continue

            if cmd in ["dir", "ls"]:
                show_hidden = any(a.lower() in ["/a", "/ah", "-a"] for a in args)
                list_dir(show_hidden=show_hidden)
            elif cmd == "attrib":
                if "secret.txt" in user_input.lower():
                    hidden_revealed = True
                    print("H  S  C:\\Users\\User\\Intel\\secret.txt")
                    print("Hidden and system attributes cleared.")
                else:
                    print("attrib: file not found.")
            elif cmd == "takeown":
                if "secret.txt" in user_input.lower():
                    ownership_taken = True
                    print("SUCCESS: Ownership updated for secret.txt.")
                else:
                    print("ERROR: File not specified.")
            elif cmd == "icacls":
                if "secret.txt" in user_input.lower() and "/grant" in user_input.lower():
                    if ownership_taken:
                        permissions_granted = True
                        print("SUCCESS: Full control granted to user.")
                    else:
                        print("ERROR: Take ownership first.")
                else:
                    print("icacls: Invalid syntax.")
            elif cmd in ["type", "cat"]:
                target = args[0].lower() if args else ""
                if target == "secret.txt":
                    if not hidden_revealed:
                        print("Access Denied: File is hidden.")
                    elif permissions_granted:
                        print("\n[SECRET.TXT]")
                        print("-" * 30)
                        print("Clue: Level 3 key is buried in audit logs.")
                        print("-" * 30)
                        time.sleep(1)
                        print_success("Permissions fixed. Level 2 Complete.")
                        return True
                    else:
                        print("Access Denied: Permissions required.")
                else:
                    print("The system cannot find the file specified.")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()
