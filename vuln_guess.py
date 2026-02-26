def guess_vulnerability(banner):
    if not banner:
        return None

    if "OpenSSH_5" in banner:
        return "Possibly outdated OpenSSH version"

    if "Apache/2.2" in banner:
        return "Apache 2.2 is outdated"

    if "vsFTPd 2.3.4" in banner:
        return "Known vulnerable vsFTPd version"

    return None