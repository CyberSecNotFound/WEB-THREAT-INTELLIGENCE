import whois
from datetime import datetime

def whois_check(domain):
    try:
        w = whois.whois(domain)
        c = w.creation_date
        if isinstance(c, list):
            c = c[0]

        age = (datetime.now() - c).days

        if age < 180:
            return 30, f"Domain sangat baru ({age} hari)"
        elif age < 365:
            return 15, f"Domain baru ({age} hari)"

        return 0, f"Domain lama ({age} hari)"

    except:
        return 20, "WHOIS disembunyikan / gagal"
