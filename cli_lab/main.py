from cli_lab.levels.linux import level1_intro, level2_permissions

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
        print("Invalid choice!")

def linux_menu():
    while True:
     print("\n=== Linux Levels ===")
     print("1) Level 1 - Intro Challenge")
     print("2) Level 2 - Permissions")
     print("3) Level 3 - COMING SOON")
     print("4) Level 4 - COMING SOON")
     print("5) Level 5 - COMING SOON")
     print("0) Back\n")

     choice = input("Select a level: ").strip()

     if choice == "1":
        level1_intro.main()
     elif choice == "2":
        level2_permissions.main()
     elif choice == "3":
        print("COMING SOON!")
     elif choice == "4":
        print("COMING SOON!")
     elif choice == "5":
        print("COMING SOON!")
     elif choice == "0":
        return
     else:
        print("Invalid choice!")

def windows_menu():
    while True:
     print("\n=== Windows Levels ===")
     print("1) Level 1 - COMING SOON")
     print("2) Level 2 - COMING SOON")
     print("3) Level 3 - COMING SOON")
     print("4) Level 4 - COMING SOON")
     print("5) Level 5 - COMING SOON")
     print("0) Back\n")
    
     choice = input("Select a level: ").strip()

     if choice == "1":
        print("COMING SOON!")
     elif choice == "2":
        print("COMING SOON!")
     elif choice == "3":
        print("COMING SOON!")
     elif choice == "4":
        print("COMING SOON!")
     elif choice == "5":
        print("COMING SOON!")
     elif choice == "0":
        return
     else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()

