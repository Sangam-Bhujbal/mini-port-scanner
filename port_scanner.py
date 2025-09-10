import socket
import threading

# Function to scan a single port
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # timeout in seconds
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
    except:
        pass

# Main function
def main():
    print("==== Mini Port Scanner ====")
    target = input("Enter Target IP or Hostname: ")

    try:
        ip = socket.gethostbyname(target)
        print(f"Scanning Target: {ip}")
    except socket.gaierror:
        print("Invalid Hostname/IP")
        return

    start_port = int(input("Enter Start Port: "))
    end_port = int(input("Enter End Port: "))

    print("\n[!] Scanning...\n")

    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nScan Completed ✅")

if __name__ == "__main__":
    main()
