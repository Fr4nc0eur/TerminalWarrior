# cli_lab/main.py
from cli_lab.levels import level1_intro, level2_permissions

def main():
    print("=== CLI Linux Lab ===")
    print("1) Level 1 - Intro Challenge")
    print("2) Level 2 - Permissions")
    print("0) Exit")
    choice = input("Select a level: ").strip()

    if choice == "1":
        level1_intro.main()
    elif choice == "2":
        level2_permissions.main()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()

