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
    title = "LEVEL 8: EVENT LOG FORENSICS"
    objectives = [
        "Analyze Security event logs for suspicious activity.",
        "Identify the incident ID from failed logons."
    ]
    hint = "Try: wevtutil qe Security /c:10 /rd:true"

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

            if cmd == "wevtutil":
                if "security" in user_input.lower():
                    print("\nEvent[0]:")
                    print("  EventID: 4625")
                    print("  Account Name: attacker")
                    print("  Failure Reason: Unknown user name or bad password")
                    print("  Incident ID: EVT-8-A9\n")
                    time.sleep(1)
                    print_success("Incident traced. Flag: TW_EVENT_TRACE_8")
                    return True
                else:
                    print("wevtutil: log name not specified.")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()
