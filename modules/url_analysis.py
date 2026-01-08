import re
import tldextract

def analyze_url(url):
    score = 0
    reasons = []

    if len(url) > 75:
        score += 15
        reasons.append("URL terlalu panjang")

    if re.search(r'@\d+|@', url):
        score += 20
        reasons.append("Mengandung simbol @")

    ext = tldextract.extract(url)
    if ext.suffix in ["xyz", "tk", "ml", "top"]:
        score += 25
        reasons.append(f"TLD mencurigakan: .{ext.suffix}")

    if url.count("-") > 3:
        score += 10
        reasons.append("Terlalu banyak '-'")

    return score, reasons
