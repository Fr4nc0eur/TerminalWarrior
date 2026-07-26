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
    title = "LEVEL 9: DISK FORENSICS & FILE RECOVERY"
    objectives = [
        "Analyze disk volumes and partitions.",
        "Recover a deleted file from the Recycle Bin."
    ]
    hint = "Try: 'list volume' (or 'wmic logicaldisk get name,filesystem') then 'dir /a C:\\$Recycle.Bin'."

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    volumes_checked = False

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

            if cmd == "list" and "volume" in user_input.lower():
                volumes_checked = True
                print("\n  Volume ###  Ltr  Label        Fs     Type        Size     Status")
                print("  ----------  ---  -----------  -----  ----------  -------  --------")
                print("  Volume 0     C   OS           NTFS   Partition  237 GB   Healthy")
                print("  Volume 1     D   DATA         NTFS   Partition  465 GB   Healthy\n")
            elif cmd == "wmic":
                if "logicaldisk" in user_input.lower():
                    volumes_checked = True
                    print("\nDescription       FileSystem  Name")
                    print("Local Fixed Disk  NTFS        C:")
                    print("Local Fixed Disk  NTFS        D:\n")
                else:
                    print("wmic: Invalid query.")
            elif cmd in ["dir", "ls"]:
                if "recycle.bin" in user_input.lower():
                    print("\n Directory of C:\\$Recycle.Bin\n")
                    print("02/20/2026  11:59 AM               320 D3L3T3D.txt")
                    print()
                else:
                    print("The system cannot find the path specified.")
            elif cmd in ["type", "cat"]:
                if "d3l3t3d.txt" in user_input.lower():
                    if volumes_checked:
                        print("\n[RECOVERED FILE]")
                        print("Recovered Flag: TW_DISK_RECOVERY_9\n")
                        time.sleep(1)
                        print_success("Deleted file recovered. Level 9 Complete.")
                        return True
                    else:
                        print("ERROR: Analyze volumes before recovery.")
                else:
                    print("The system cannot find the file specified.")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()
