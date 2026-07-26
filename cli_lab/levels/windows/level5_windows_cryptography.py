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


ENCODED_MESSAGE = "Uk9UMTM6IFNWQU5ZX1NZTlQ6IEpWQVFCSkZfWk5GR1JFX1VOUFhSRQ=="
ROT13_HINT = "ROT13: SVANY_SYNT: JVAQBJF_ZNFGRE_UNPXRE"


def rot13(text):
    result = []
    for ch in text:
        if "a" <= ch <= "z":
            result.append(chr((ord(ch) - 97 + 13) % 26 + 97))
        elif "A" <= ch <= "Z":
            result.append(chr((ord(ch) - 65 + 13) % 26 + 65))
        else:
            result.append(ch)
    return "".join(result)


def run_level():
    title = "LEVEL 5: CRYPTOGRAPHY & DECODING"
    objectives = [
        "Decode the Base64 file with Windows utilities.",
        "Solve the simple cipher to reveal the final flag."
    ]
    hint = "Use 'certutil -decode message.b64 message.txt' then decipher ROT13."

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    decoded_ready = False

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
                print(f" Directory of {CURRENT_DIR}\n")
                print("02/20/2026  11:30 AM               256 message.b64")
                print()
            elif cmd in ["type", "cat"]:
                if args and args[0].lower() == "message.b64":
                    print("\n[CONTENT OF message.b64]")
                    print(ENCODED_MESSAGE)
                    print()
                elif args and args[0].lower() == "message.txt":
                    if decoded_ready:
                        print("\n[CONTENT OF message.txt]")
                        print(ROT13_HINT)
                        print()
                    else:
                        print("The system cannot find the file specified.")
                else:
                    print("The system cannot find the file specified.")
            elif cmd == "certutil":
                if "-decode" in user_input.lower() and "message.b64" in user_input.lower():
                    decoded_ready = True
                    print("\nCertUtil: -decode command completed successfully.")
                    print("Output written to message.txt.")
                else:
                    print("CertUtil: Syntax or parameters invalid.")
            elif cmd == "rot13":
                if args:
                    decoded = rot13(" ".join(args))
                    print(decoded)
                    if "FINAL_FLAG:" in decoded:
                        time.sleep(1)
                        print_success("Cipher solved. Level 5 Complete.")
                        return True
                else:
                    print("Usage: rot13 <text>")
            elif cmd == "base64":
                print("base64: Not available here. Use certutil instead.")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()
