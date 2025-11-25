# FILE: windows_menu.py (UPDATED FLOW)
import sys
import time
from utils import clear_screen, print_header

import level1_recon 
import level2_permissions 
import level3_searching
import level4_networking
import level5_cryptography

def main_menu():
    print_header("THEROOTEXEC CHALLENGE SYSTEM | MAIN CONSOLE")
    print(":: CHALLENGE TRACKS ::")
    print("-" * 35)
    print(" [1] Start Windows Campaign (Levels 1-5)")
    print(" [2] Exit System")
    print("-" * 35)
    
    while True:
        choice = input("Selection: ")
        
        if choice == "1":
            if level1_recon.run_level():
                 if level2_permissions.run_level(): 
                    if level3_searching.run_level(): 
                        if level4_networking.run_level():
                            if level5_cryptography.run_level():
                                clear_screen()
                                print("\n\n")
                                print("*" * 50)
                                print("MISSION COMPLETE! WINDOWS CAMPAIGN ACHEIVED")
                                print("*" * 50)
                                input()
            return 
        elif choice == "2":
            print("System Disconnected.")
            sys.exit(0)
                     
if __name__ == "__main__":
    main_menu()                     


