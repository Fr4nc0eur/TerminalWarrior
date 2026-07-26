import random
import pyfiglet

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Run 'ping 8.8.8.8' to test network connectivity.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Run 'traceroute google.com' to trace the route to a host.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Run 'ifconfig' or 'ip addr' to view network interfaces.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Run 'netstat -tuln' to display listening ports.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Run 'nslookup google.com' or 'dig google.com' to resolve DNS.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Run 'ssh user@localhost' to test SSH connectivity (password: user).",
        "",
        f"{'✅' if state[7] else '◻️'} 7) Use 'nmap localhost' to scan for open ports.",
        "",
    ]

def print_help():
    print(" help - Display this help menu")
    print(" challenge - Display the current challenges")
    print(" exit - Exit the terminal")
    print(" ping <host> - Test network connectivity")
    print(" traceroute <host> - Trace route to host")
    print(" ifconfig - Display network interfaces (deprecated, use 'ip addr')")
    print(" ip addr - Display network interfaces")
    print(" netstat -tuln - Show listening ports")
    print(" nslookup <host> - Resolve DNS name")
    print(" dig <host> - Alternative DNS resolution tool")
    print(" ssh <user@host> - Connect via SSH")
    print(" nmap <host> - Network port scanning")
    print(" pwd - Print Working Directory")
    print(" whoami - Display current user")

def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)

def main():
    challenge_state = {i: False for i in range(1, 8)}
    
    processes = random.randint(100, 200)
    memoryusage = random.randint(50, 150)
    time1 = random.randint(1, 24)
    time2 = random.randint(10, 59)
    time3 = random.randint(10, 59)
    day = random.randint(1, 28)
    ip_parts = [str(random.randint(10, 100)) for _ in range(4)]
    ip_address = ".".join(ip_parts)

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="slant")
    print(ascii_banner)
    print("\nWelcome to Challenge level 4 (NETWORKING) made by (Diversion/diverter)\n")
    print("type 'help' and 'challenge' to access help menu and view challenges.")
    input("Press Enter to continue...")
    print("")

    print_challenges(challenge_state)
    print("\nWelcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-91-generic x86_64)\n")
    print("* Documentation: https://help.ubuntu.com")
    print("* Management:    https://landscape.canonical.com")
    print("* Support:       https://ubuntu.com/advantage\n")
    print(
        f"System information as of [Thu Oct {day} {time1:02d}:{time2:02d}:{time3:02d} UTC 2025]\n")
    print(f"System load: 0.00               Processes:          {processes}")
    print("Usage of /:   20.75% of 49.11GB  Users logged in:     1")
    print(
        f"Memory usage: {memoryusage}MB             IP address for eth0: {ip_address}")
    print("Swap usage:   0%\n")
    print("0 updates can be applied immediately\n")
    print("Last Login: Thu Oct 3 12:00:00 UTC 2025\n")

    current_directory = "~"
    user_password = "user"
    ssh_port = 22
    open_ports = ["22", "80", "443", "53"]
    network_interfaces = [
        "eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP",
        "lo: <LOOPBACK,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP"
    ]
    
    while True:
        prompt = f"user@linux:{current_directory}$ "
        command = input(prompt).strip()
        if not command:
            continue

        parts = command.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == "help":
            print_help()
            continue

        if cmd == "challenge":
            print()
            print_challenges(challenge_state)
            print()
            continue

        if cmd == "exit":
            print("Goodbye")
            break

        if cmd == "ping":
            if len(args) < 1:
                print("Usage: ping <host>")
                continue
            host = args[0]
            if host in ["8.8.8.8", "google.com"]:
                print("PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.")
                print("64 bytes from 8.8.8.8: icmp_seq=1 ttl=119 time=25.3 ms")
                print("64 bytes from 8.8.8.8: icmp_seq=2 ttl=119 time=24.8 ms")
                if not challenge_state[1]:
                    challenge_state[1] = True
                    print("\nYou completed challenge 1! Type 'challenge' to see your progress.")
            else:
                print(f"ping: unknown host {host}")
            continue

        if cmd == "traceroute":
            if len(args) < 1:
                print("Usage: traceroute <host>")
                continue
            host = args[0]
            if host == "google.com":
                print("traceroute to google.com (142.250.74.14), 30 hops max, 60 byte packets")
                print(" 1  192.168.1.1  1.234 ms  1.123 ms  1.098 ms")
                print(" 2  10.0.0.1  5.432 ms  5.321 ms  5.210 ms")
                print(" 3  142.250.74.14  25.345 ms  25.678 ms  25.901 ms")
                if not challenge_state[2]:
                    challenge_state[2] = True
                    print("You completed challenge 2! Type 'challenge' to see your progress.")
            else:
                print(f"traceroute: unknown host {host}")
            continue

        if cmd in ["ifconfig", "ip"]:
            if len(args) == 0 or args == ["addr"]:
                print("1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UP")
                print("    inet 127.0.0.1/8 scope host lo")
                print("    inet6 ::1/128 scope host")
                print("2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP")
                print("    inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0")
                print("    inet6 fe80::1234:5678:9abc:def0/64 scope link")
                if not challenge_state[3]:
                    challenge_state[3] = True
                    print("You completed challenge 3! Type 'challenge' to see your progress.")
            else:
                print("Usage: ip addr or ifconfig")
            continue

        if cmd == "netstat":
            if len(args) == 1 and args[0] == "-tuln":
                print("Active Internet connections (only servers)")
                print("Proto Recv-Q Send-Q Local Address           Foreign Address         State")
                print("tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN")
                print("tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN")
                print("tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN")
                print("udp        0      0 0.0.0.0:53              0.0.0.0:*               LISTEN")
                if not challenge_state[4]:
                    challenge_state[4] = True
                    print("You completed challenge 4! Type 'challenge' to see your progress.")
            else:
                print("Usage: netstat -tuln")
            continue

        if cmd in ["nslookup", "dig"]:
            if len(args) < 1:
                print("Usage: nslookup <host> or dig <host>")
                continue
            host = args[0]
            if host == "google.com":
                print("Server:		8.8.8.8")
                print("Address:	8.8.8.8:53")
                print("")
                print("Non-authoritative answer:")
                print("Name:	google.com")
                print("Address: 142.250.74.14")
                print("Name:	google.com")
                print("Address: 2a00:1450:4009:80c::200e")
                if not challenge_state[5]:
                    challenge_state[5] = True
                    print("You completed challenge 5! Type 'challenge' to see your progress.")
            else:
                print(f"nslookup: unable to resolve {host}: Unknown host")
            continue

        if cmd == "ssh":
            if len(args) < 1:
                print("Usage: ssh <user@host>")
                continue
            connection = args[0]
            if connection == "user@localhost":
                password_input = input("user@localhost's password: ").strip()
                if password_input == user_password:
                    print("Linux 5.15.0-91-generic x86_64")
                    print("Last login: Thu Oct 3 12:00:00 2025 from 127.0.0.1")
                    print("user@localhost:~$ ")
                    if not challenge_state[6]:
                        challenge_state[6] = True
                        print("You completed challenge 6! Type 'challenge' to see your progress.")
                else:
                    print("Permission denied")
            else:
                print(f"ssh: connect to host {connection.split('@')[1]} port 22: Connection refused")
            continue

        if cmd == "nmap":
            if len(args) < 1:
                print("Usage: nmap <host>")
                continue
            host = args[0]
            if host == "localhost":
                print("Starting Nmap 7.80 ( https://nmap.org ) at 2025-10-03 12:00 UTC")
                print("Nmap scan report for localhost (127.0.0.1)")
                print("Host is up (0.00012s latency).")
                print("")
                print("PORT   STATE SERVICE")
                print("22/tcp open  ssh")
                print("80/tcp open  http")
                print("443/tcp open https")
                print("53/tcp open  domain")
                if not challenge_state[7]:
                    challenge_state[7] = True
                    print("You completed challenge 7! Type 'challenge' to see your progress.")
            else:
                print(f"Nmap scan report for {host}")
                print("Host is up (0.00012s latency).")
                print("")
                print("PORT   STATE SERVICE")
                print("22/tcp open  ssh")
                if not challenge_state[7]:
                    challenge_state[7] = True
                    print("You completed challenge 7! Type 'challenge' to see your progress.")
            continue

        if cmd == "pwd":
            print("/home/user")
            continue

        if cmd == "whoami":
            print("user")
            continue

        print(f"{cmd}: command not found")

if __name__ == "__main__":
    main()