from scanner import TCPScanner
from banner import grab_banner
from service_detect import detect_service
from vuln_guess import guess_vulnerability


def main():
    print("=" * 50)
    print("Simple Network Port_Scanner")
    print("=" * 50)

    target = input("Enter target IP or Hostname: ")

    start_port = int(input("Start Port: "))
    end_port = int(input("End Port: "))

    # Initialize scanner
    scanner = TCPScanner(target)

    print("\nScanning...\n")

    open_ports = scanner.run_scan(start_port, end_port)

    if not open_ports:
        print("No open ports found.")
        return

    print("Open Ports Found:\n")

    for port in open_ports:
        service = detect_service(port)
        banner = grab_banner(target, port)
        vuln = guess_vulnerability(banner)

        print(f"Port: {port}")
        print(f"Service: {service}")

        if banner:
            print(f"Banner: {banner}")
        else:
            print("Banner: Not detected")

        if vuln:
            print(f"Vulnerability Guess: {vuln}")

        print("-" * 40)


if __name__ == "__main__":
    main()