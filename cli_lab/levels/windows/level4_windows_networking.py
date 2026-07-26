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


TARGET_IP = "10.10.5.23"
SERVICE_PORT = "8080"


def run_level():
    title = "LEVEL 4: NETWORKING CHALLENGE"
    objectives = [
        "Identify the target IP from local network info.",
        "Verify connectivity and locate the open service port.",
        "Pull the service token with curl."
    ]
    hint = "Try: 'ipconfig', 'ping <ip>', 'netstat -an', then 'curl http://<ip>:8080/'."

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    pinged = False
    scanned = False

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

            if cmd == "ipconfig":
                print("\nWindows IP Configuration\n")
                print("Ethernet adapter Ethernet:")
                print("   IPv4 Address. . . . . . . . . . . : 10.10.5.10")
                print(f"   Default Gateway . . . . . . . . . : {TARGET_IP}\n")
            elif cmd == "ping":
                if args and args[0] == TARGET_IP:
                    pinged = True
                    print(f"\nPinging {TARGET_IP} with 32 bytes of data:")
                    print(f"Reply from {TARGET_IP}: bytes=32 time=5ms TTL=64")
                    print("Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)\n")
                else:
                    print("Ping request could not find host.")
            elif cmd == "tracert":
                if args and args[0] == TARGET_IP:
                    print(f"\nTracing route to {TARGET_IP} over a maximum of 30 hops:\n")
                    print("  1     1 ms     1 ms     1 ms  10.10.5.1")
                    print(f"  2     8 ms     9 ms     8 ms  {TARGET_IP}\n")
                else:
                    print("Unable to resolve target.")
            elif cmd == "netstat":
                if "-an" in user_input.lower():
                    scanned = True
                    print("\nActive Connections:")
                    print("  Proto  Local Address          Foreign Address        State")
                    print(f"  TCP    10.10.5.10:49601        {TARGET_IP}:{SERVICE_PORT}       ESTABLISHED")
                    print("  TCP    10.10.5.10:49602        52.85.10.10:443        TIME_WAIT")
                    print("  TCP    0.0.0.0:135             0.0.0.0:0              LISTENING\n")
                else:
                    print("Use 'netstat -an' to view all connections.")
            elif cmd == "curl":
                if f"http://{TARGET_IP}:{SERVICE_PORT}" in user_input.lower():
                    if pinged and scanned:
                        print("\nHTTP/1.1 200 OK")
                        print("service=telemetry")
                        print("token=NET_OK:TW_NET_4\n")
                        time.sleep(1)
                        print_success("Service token captured. Level 4 Complete.")
                        return True
                    else:
                        print("Connection refused. Validate connectivity first.")
                else:
                    print("curl: Invalid or missing URL.")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()
