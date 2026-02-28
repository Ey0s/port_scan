def guess_vulnerability(banner):
    if not banner:
        return None

    banner = banner.lower()
    VULN_SIGNATURES = {
        "openssh_5": "OpenSSH 5.x is outdated and may contain security vulnerabilities.",
        "openssh_6.0": "OpenSSH 6.0 is outdated and contains several vulnerabilities.",
        "apache/2.2": "Apache 2.2 is end-of-life and vulnerable.",
        "apache/2.0": "Apache 2.0 is obsolete and insecure.",
        "apache/2.4.1": "Apache 2.4.1 has known security issues; update recommended.",
        "vsftpd 2.3.4": "vsFTPd 2.3.4 contains a known backdoor vulnerability.",
        "proftpd 1.3.3": "ProFTPD 1.3.3 has known remote execution vulnerabilities.",
        "iis/6.0": "Microsoft IIS 6.0 is outdated and vulnerable.",
        "iis/7.0": "Microsoft IIS 7.0 has several security issues.",
        "mysql 5.0": "MySQL 5.0 is outdated and contains multiple CVEs.",
        "mysql 5.5": "MySQL 5.5 has known vulnerabilities.",
        "php/5": "PHP 5.x is end-of-life and insecure.",
        "php/7.0": "PHP 7.0 is outdated and no longer supported.",
        "nginx/1.0": "Old Nginx 1.0 versions may contain vulnerabilities.",
        "nginx/1.4": "Nginx 1.4 has known security issues.",
        "samba 3": "Samba 3.x may be vulnerable to remote exploits.",
        "tomcat/6.0": "Apache Tomcat 6.0 is end-of-life and vulnerable.",
        "tomcat/7.0": "Apache Tomcat 7.0 has known security flaws.",
        "openssl 0.9.8": "OpenSSL 0.9.8 is very old and insecure.",
        "openssl 1.0.1": "OpenSSL 1.0.1 is vulnerable to Heartbleed.",
        "openssl 1.0.2": "OpenSSL 1.0.2 requires updates due to multiple CVEs.",
        "bind 9.4": "BIND 9.4 has known DNS vulnerabilities.",
        "bind 9.6": "BIND 9.6 requires updates due to security flaws.",
        "java/1.6": "Java 6 is outdated and insecure.",
        "java/1.7": "Java 7 is no longer supported and vulnerable.",
        "postgresql 8.3": "PostgreSQL 8.3 is obsolete and vulnerable.",
        "postgresql 9.1": "PostgreSQL 9.1 is outdated and unsupported.",
    }

    for signature, message in VULN_SIGNATURES.items():
        if signature in banner:
            return message

    return None