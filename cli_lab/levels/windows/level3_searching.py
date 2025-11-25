# FILE: level3_searching.py (NEW FILE)
import time
from utils import clear_screen, print_header, print_objectives, print_success, generic_cmd_handler, CURRENT_DIR

LOG_CONTENT = (
    "12:01:05 SYSTEM Starting service logon.\n"
    "12:01:10 ERROR Failed connection attempt from 10.0.0.1.\n"
    "12:01:15 SYSTEM Audit success for user guest.\n"
    "12:01:20 ALERT FLAG_KEY:HUNT3R_L0G_TRACER\n" # <-- The hidden flag string
    "12:01:25 SYSTEM Service shutdown complete.\n"
)

def run_level():
    title = "LEVEL 3: SEARCHING THE SYSTEM"
    objectives = [
        "A suspicious log file has been created: 'system.log'.",
        "Use search tools to find the hidden challenge key inside."
    ]
    hint = "Use 'findstr' to search the content of 'system.log' for the word 'FLAG'."
    
    print_header(title)
    print_objectives(objectives, hint)

    while True:
        try:
            prompt = f"{CURRENT_DIR}> "
            user_input = input(prompt).strip() # Keep case for findstr
            parts = user_input.lower().split()
            cmd = parts[0] if parts else ""
            
            common = generic_cmd_handler(cmd, '') # Use empty string for arg check
            if common == "EXIT": return False
            if common: continue
            
            # Level 3 Specific Logic (Searching)
            if cmd == "dir" or cmd == "ls":
                print(f" Directory of {CURRENT_DIR}")
                print("12/01/2025  12:02 PM             1,200 system.log")
                print("               1 File(s)          1,200 bytes\n")

            elif cmd == "type" or cmd == "cat":
                if "system.log" in user_input:
                    print("\n[LOG FILE CONTENT PREVIEW]")
                    print("-" * 30)
                    print(LOG_CONTENT)
                    print("-" * 30)
                else:
                    print("File not found.")

            elif cmd == "findstr":
                # Check for the key command: findstr FLAG system.log
                if "flag" in user_input.lower() and "system.log" in user_input.lower():
                    print("\n[SEARCH RESULTS]")
                    print("12:01:20 ALERT FLAG_KEY:HUNT3R_L0G_TRACER")
                    
                    # WIN CONDITION
                    time.sleep(1)
                    print_success("Key Found! Level 3 Complete.")
                    return True
                else:
                    print("findstr: Search string or file name not specified.")
            
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False
