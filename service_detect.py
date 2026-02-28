COMMON_PORTS = {
    20: "FTP (Data)",
    21: "FTP",
    22: "SSH",
    69: "TFTP",

    23: "Telnet",
    3389: "RDP",
    5900: "VNC",

    25: "SMTP",
    465: "SMTPS",
    587: "SMTP (Submission)",
    110: "POP3",
    995: "POP3S",
    143: "IMAP",
    993: "IMAPS",

    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP (Alt)",
    8443: "HTTPS (Alt)",

    53: "DNS",
    67: "DHCP (Server)",
    68: "DHCP (Client)",
    123: "NTP",
    161: "SNMP",
    162: "SNMP Trap",

    1433: "Microsoft SQL Server",
    1521: "Oracle DB",
    27017: "MongoDB",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis",

    389: "LDAP",
    636: "LDAPS",

    2375: "Docker",
    2376: "Docker (TLS)",
    6443: "Kubernetes API",

    5672: "RabbitMQ",
    9092: "Kafka",

    9418: "Git",

    1900: "UPnP",
    5060: "SIP",
}


def detect_service(port):
    return COMMON_PORTS.get(port, "Unknown Service")