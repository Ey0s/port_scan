COMMON_PORTS = {
    # File Transfer
    20: "FTP-Data",
    21: "FTP",
    22: "SSH",
    69: "TFTP",
    989: "FTPS (Data)",
    990: "FTPS (Control)",

    # Remote Access
    23: "Telnet",
    3389: "RDP",
    5900: "VNC",
    5938: "TeamViewer",
    5800: "VNC (Web)",

    # Web Services
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
    8000: "HTTP-Dev",
    8888: "HTTP-Alt2",

    # Mail
    25: "SMTP",
    465: "SMTPS",
    587: "SMTP (Submission)",
    110: "POP3",
    995: "POP3S",
    143: "IMAP",
    993: "IMAPS",

    # DNS
    53: "DNS",
    5353: "mDNS",

    # Databases
    1433: "MSSQL",
    1521: "Oracle DB",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis",
    27017: "MongoDB",
    9042: "Cassandra",
    9200: "Elasticsearch",

    # Directory / Auth
    389: "LDAP",
    636: "LDAPS",
    88: "Kerberos",

    # Network Services
    123: "NTP",
    161: "SNMP",
    162: "SNMP Trap",
    179: "BGP",
    194: "IRC",
    5060: "SIP",
    5061: "SIPS",

    # SMB / Windows
    135: "MS RPC",
    137: "NetBIOS-NS",
    138: "NetBIOS-DGM",
    139: "NetBIOS-SSN",
    445: "SMB",

    # DevOps / Monitoring
    3000: "Grafana/Dev Server",
    5601: "Kibana",
    9090: "Prometheus",
    9100: "Node Exporter",

    # Containers / Orchestration
    2375: "Docker",
    2376: "Docker TLS",
    6443: "Kubernetes API",

    # VPN
    1194: "OpenVPN",
    500: "IPSec",
    4500: "IPSec NAT-T",
}


def detect_service(port):
    return COMMON_PORTS.get(port, "Unknown Service")