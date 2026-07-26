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


TASKS_CONTENT = (
    "alpha: ok\n"
    "beta: ok\n"
    "gamma: FLAG=TW_POWERSHELL_10\n"
    "delta: ok\n"
)


def run_level():
    title = "LEVEL 10: POWERSHELL SCRIPTING CHALLENGE"
    objectives = [
        "Use PowerShell to filter text and extract the flag.",
        "Automate the search rather than scanning manually."
    ]
    hint = "Try: powershell -command \"Get-Content tasks.txt | Select-String FLAG\""

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    while True:
        try:
            user_input = input(build_prompt(CURRENT_DIR)).strip()
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
                print(f"\n Directory of {CURRENT_DIR}\n")
                print("02/20/2026  12:05 PM               256 tasks.txt")
                print()
            elif cmd in ["type", "cat"]:
                if args and args[0].lower() == "tasks.txt":
                    print("\n[TASKS]")
                    print(TASKS_CONTENT)
                else:
                    print("The system cannot find the file specified.")
            elif cmd in ["powershell", "pwsh"]:
                lower = user_input.lower()
                if "tasks.txt" in lower and ("select-string" in lower or "where-object" in lower):
                    print("\nMatchInfo: gamma: FLAG=TW_POWERSHELL_10\n")
                    time.sleep(1)
                    print_success("Automation complete. Level 10 Complete.")
                    return True
                else:
                    print("PowerShell: Command executed. No matches found.")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()
