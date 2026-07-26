import os
import sys

# Allow running as a script: python .\cli_lab\main.py
if __name__ == "__main__" and __package__ is None:
    repo_root = os.path.dirname(os.path.dirname(__file__))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

from cli_lab.levels.linux import level1_linux_intro as linux_level1, level2_linux_permissions as linux_level2, level3_linux_searching as linux_level3, level4_linux_networking as linux_level4
from cli_lab.levels.windows import level1_windows_recon as win_level1, level2_windows_permissions as win_level2, level3_windows_searching as win_level3, level4_windows_networking as win_level4, level5_windows_cryptography as win_level5, level6_windows_registry as win_level6, level7_windows_tasks_services as win_level7, level8_Windows_event_logs as win_level8, level9_windows_disk_forensics as win_level9
from cli_lab.levels.linux import (
    level5_linux_cryptography as linux_level5,
)

from cli_lab.levels.windows import (
    level10_windows_powershell as win_level10,
)


def main():
    while True:
        print("=== TerminalWarrior ===\n")
        print("1) Linux Challenges")
        print("2) Windows Challenges")
        print("0) Exit\n")

        terminal_choice = input("Select a Terminal: ").strip()

        if terminal_choice == "1":
            linux_menu()
        elif terminal_choice == "2":
            windows_menu()
        elif terminal_choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid choice!\n")


def linux_menu():
    while True:
        print("\n=== Linux Levels ===")
        print("1) Level 1 - Intro Challenge")
        print("2) Level 2 - Permissions")
        print("3) Level 3 - Searching the System")
        print("4) Level 4 - Networking")
        print("5) Level 5 - Cryptography & Decoding")
        print("0) Back\n")

        choice = input("Select a level: ").strip()

        if choice == "1":
            linux_level1.main()
        elif choice == "2":
            linux_level2.main()
        elif choice == "3":
            linux_level3.main()
        elif choice == "4":
            linux_level4.main()
        elif choice == "5":
            linux_level5.main()
        elif choice == "0":
            return
        else:
            print("Invalid choice!\n")


def windows_menu():
    while True:
        print("\n=== Windows Levels ===")
        print("1) Level 1 - Intro Challenge")
        print("2) Level 2 - Permissions & Ownership")
        print("3) Level 3 - Searching the System")
        print("4) Level 4 - Networking Challenge")
        print("5) Level 5 - Cryptography & Decoding")
        print("6) Level 6 - Registry Deep Dive")
        print("7) Level 7 - Task Scheduler & Services")
        print("8) Level 8 - Event Log Forensics")
        print("9) Level 9 - Disk Forensics & File Recovery")
        print("10) Level 10 - PowerShell Scripting Challenge")
        print("0) Back\n")

        choice = input("Select a level: ").strip()

        if choice == "1":
            win_level1.run_level()
        elif choice == "2":
            win_level2.run_level()
        elif choice == "3":
            win_level3.run_level()
        elif choice == "4":
            win_level4.run_level()
        elif choice == "5":
            win_level5.run_level()
        elif choice == "6":
            win_level6.run_level()
        elif choice == "7":
            win_level7.run_level()
        elif choice == "8":
            win_level8.run_level()
        elif choice == "9":
            win_level9.run_level()
        elif choice == "10":
            win_level10.run_level()
        elif choice == "0":
            return
        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()
