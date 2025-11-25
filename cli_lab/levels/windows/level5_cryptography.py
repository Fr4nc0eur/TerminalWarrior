# FILE: level5_cryptography.py
import time
from utils import clear_screen, print_header, print_objectives, print_success, generic_cmd_handler, CURRENT_DIR

# This is 'FINAL_FLAG:WINDOWS_MASTER_HACKER' encoded in Base64
ENCODED_FLAG = "RklOQUxfRkxBRzpXSU5ET1dTX01BU1RFUl9IQUNLRVI="

def run_level():
    title = "LEVEL 5: CRYPTOGRAPHY & DECODING"
    objectives = [
        "The server response provided a mysterious encoded file: 'flag.b64'.",
        "Decode the file using Windows utilities to reveal the final flag."
    ]
    hint = "Use the Windows built-in 'certutil' command to decode the Base64 file."
    
    print_header(title)
    print_objectives(objectives, hint)

    while True:
        try:
            prompt = f"{CURRENT_DIR}> "
            user_input = input(prompt).strip().lower()
            parts = user_input.split()
            cmd = parts[0] if parts else ""
            arg = parts[1] if len(parts) > 1 else ""

            common = generic_cmd_handler(cmd, arg)
            if common == "EXIT": return False
            if common: continue

            # Level 5 Specific Logic (Crypto)
            if cmd == "type" or cmd == "cat":
                if arg == "flag.b64":
                    print("\n[CONTENT OF flag.b64]")
                    print(ENCODED_FLAG)
                    print()
                else:
                    print("File not found.")

            elif cmd == "certutil":
                # Win condition: certutil -decode flag.b64 flag.txt
                if "-decode" in user_input and "flag.b64" in user_input:
                    print("\nCertUtil: -decode command completed successfully.")
                    print("Output written to flag.txt.")
                    time.sleep(1)
                    
                    print_success(f"Final Flag Decoded: FINAL_FLAG:WINDOWS_MASTER_HACKER! Campaign Complete.")
                    return True
                else:
                    print("CertUtil: Syntax or parameters invalid.")

            elif cmd == "base64":
                print("base64: Command not implemented. Use certutil instead.")

            else:
                print(f"'{cmd}' is not recognized.")

        except KeyboardInterrupt:
            return False