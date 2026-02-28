# Simple Network Port Scanner

A lightweight Python TCP port scanner that:
- scans a target host across a port range using threads,
- reports open ports,
- maps common ports to likely services,
- attempts basic banner grabbing,
- makes simple vulnerability guesses from known banner strings.

## Features
- Multi-threaded TCP connect scan
- Configurable start and end ports via CLI prompts
- Basic service detection from common port mappings
- Banner grabbing for open ports
- Basic vulnerability hints for a few legacy signatures

## Requirements
- Python 3.8+
- Network access to the target host

## Installation
1. Clone or download this project.
2. From the project directory, run:

```bash
python main.py
```

No external dependencies are required.

## Usage
Run:

```bash
python main.py
```

You will be prompted for:
- Target IP or hostname
- Start port
- End port

Example:

```text
Enter target IP or hostname: scanme.nmap.org
Start Port: 20
End Port: 100
```

## Example Output
```text
==================================================
Simple Network Port Scanner
==================================================

Scanning...

Open Ports Found:

Port: 22
Service: SSH
Banner: SSH-2.0-OpenSSH_8.9
----------------------------------------
```

## Project Structure
- `main.py` - CLI flow and output formatting
- `scanner.py` - threaded TCP port scanning logic
- `service_detect.py` - port-to-service mapping
- `banner.py` - banner grabbing via socket receive
- `vuln_guess.py` - simple vulnerability guessing rules

## Current Limitations
- TCP connect scan only (no UDP/SYN scan)
- Banner grabbing depends on service behavior and may return nothing
- Vulnerability detection is heuristic and very limited
- One thread per port can be heavy for very large ranges

## Ethical Use
Only scan systems you own or are explicitly authorized to test. Unauthorized scanning may violate laws or policies.

## Future Improvements
- Add argument parsing (`argparse`) instead of interactive prompts
- Add timeout and thread-pool controls from CLI
- Expand service fingerprints and vulnerability rule set
- Add unit tests
