def guess_vulnerability(banner):
    if not banner:
        return None

    banner = banner.lower()
    VULN_SIGNATURES = {
        "openssh_5": "OpenSSH 5.x is outdated and may contain security vulnerabilities.",
        "apache/2.2": "Apache 2.2 is end-of-life and vulnerable.",
        "apache/2.0": "Apache 2.0 is obsolete and insecure.",
        "vsftpd 2.3.4": "vsFTPd 2.3.4 contains a known backdoor vulnerability.",
        "proftpd 1.3.3": "ProFTPD 1.3.3 has known remote execution vulnerabilities.",
        "iis/6.0": "Microsoft IIS 6.0 is outdated and vulnerable.",
        "mysql 5.0": "MySQL 5.0 is outdated and contains multiple CVEs.",
        "php/5": "PHP 5.x is end-of-life and insecure.",
        "nginx/1.0": "Old Nginx 1.0 versions may contain vulnerabilities.",
        "samba 3": "Samba 3.x may be vulnerable to remote exploits.",
    }

    for signature, message in VULN_SIGNATURES.items():
        if signature in banner:
            return message

    return None