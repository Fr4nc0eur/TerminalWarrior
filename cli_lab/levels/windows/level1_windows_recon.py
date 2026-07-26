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
    title = "LEVEL 1: INTRO CHALLENGE"
    objectives = [
        "Navigate folders to uncover a hidden file.",
        "Read the hidden file to extract credentials."
    ]
    hint = "Use 'dir', 'dir /a', and 'cd' to explore. Read files with 'type'."

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    current_dir = CURRENT_DIR
    hidden_revealed = False

    def list_dir(show_hidden=False):
        nonlocal hidden_revealed
        print(f" Directory of {current_dir}\n")
        if current_dir == CURRENT_DIR:
            print("02/20/2026  09:10 AM    <DIR>          .")
            print("02/20/2026  09:10 AM    <DIR>          ..")
            print("02/20/2026  08:55 AM    <DIR>          Intel")
            print("02/20/2026  08:55 AM    <DIR>          Public")
            print("02/20/2026  08:40 AM               256 readme.txt")
        elif current_dir == f"{CURRENT_DIR}\\Intel":
            print("02/20/2026  08:30 AM               512 brief.txt")
            if show_hidden:
                hidden_revealed = True
                print("02/20/2026  08:31 AM               384 notes.txt")
        elif current_dir == f"{CURRENT_DIR}\\Public":
            print("02/20/2026  08:20 AM               128 welcome.txt")
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
            elif cmd == "cd":
                if not args:
                    print(current_dir)
                elif args[0] == "..":
                    current_dir = CURRENT_DIR
                elif args[0].lower() == "intel":
                    current_dir = f"{CURRENT_DIR}\\Intel"
                elif args[0].lower() == "public":
                    current_dir = f"{CURRENT_DIR}\\Public"
                else:
                    print("The system cannot find the path specified.")
            elif cmd in ["type", "cat"]:
                target = args[0].lower() if args else ""
                if current_dir == CURRENT_DIR and target == "readme.txt":
                    print("Welcome agent. Explore the Intel folder for operational notes.")
                elif current_dir == f"{CURRENT_DIR}\\Intel" and target == "brief.txt":
                    print("Brief: Locate hidden notes and extract credentials.")
                elif current_dir == f"{CURRENT_DIR}\\Intel" and target == "notes.txt":
                    if hidden_revealed:
                        print("\n[NOTES.TXT]")
                        print("-" * 30)
                        print("Username: admin_root")
                        print("Temp Password: Winter2026!")
                        print("Next: Use proper ownership tools to access locked files.")
                        print("-" * 30)
                        time.sleep(1)
                        print_success("Hidden file recovered. Level 1 Complete.")
                        return True
                    else:
                        print("Access Denied: File is hidden.")
                elif current_dir == f"{CURRENT_DIR}\\Public" and target == "welcome.txt":
                    print("Welcome. Nothing sensitive here.")
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
