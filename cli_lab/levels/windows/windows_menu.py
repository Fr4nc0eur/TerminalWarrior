# FILE: windows_menu.py (UPDATED FLOW)
import sys
import time
from utils import clear_screen, print_header

import level1_recon 
import level2_permissions 
import level3_searching   

def main_menu():
    
    while True:
        choice = input("Selection: ")
        
        if choice == "1":
            if level1_recon.run_level():
                if level2_permissions.run_level(): 
                    if level3_searching.run_level():                         
                         clear_screen()
                         print("\n\n")
                         print("*" * 50)
                         print("END OF CURRENT CHALLENGE. LEVEL 4 COMING SOON!")
                         print("*" * 50)
                         input()
            return 
