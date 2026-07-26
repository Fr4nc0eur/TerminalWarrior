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
    title = "LEVEL 6: REGISTRY DEEP DIVE"
    objectives = [
        "Locate the hidden configuration key in the registry.",
        "Extract the secret value to advance."
    ]
    hint = r"Try: reg query HKCU\Software\TerminalWarrior\Hidden /v Secret"

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

            if cmd == "reg":
                if "query" in user_input.lower() and "terminalwarrior" in user_input.lower():
                    print(r"\nHKEY_CURRENT_USER\Software\TerminalWarrior\Hidden")
                    print("    Secret    REG_SZ    TW_REGISTRY_6\n")
                    time.sleep(1)
                    print_success("Registry key located. Level 6 Complete.")
                    return True
                else:
                    print("ERROR: The system was unable to find the specified registry key or value.")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()
