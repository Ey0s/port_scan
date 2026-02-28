import socket
import threading


class TCPScanner:
    def __init__(self, target, timeout=5):
        self.target = target
        self.timeout = timeout
        self.open_ports = []
        self.lock = threading.Lock()

    def scan_port(self, port):
        sock = None
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                with self.lock:
                    self.open_ports.append(port)
        except (socket.error, OSError):
            pass
        finally:
            if sock is not None:
                sock.close()

    def run_scan(self, start_port, end_port):
        threads = []

        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=self.scan_port, args=(port,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return sorted(self.open_ports)
