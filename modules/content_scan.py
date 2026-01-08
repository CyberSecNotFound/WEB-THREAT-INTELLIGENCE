import requests
from bs4 import BeautifulSoup

def content_scan(url):
    score = 0
    reasons = []

    try:
        html = requests.get(url, timeout=10).text.lower()
        soup = BeautifulSoup(html, "html.parser")

        keywords = open("data/phishing_keywords.txt").read().splitlines()
        found = [k for k in keywords if k in html]

        if found:
            score += min(30, len(found) * 5)
            reasons.append(f"Keyword phishing: {', '.join(found[:5])}")

        if soup.find("form"):
            score += 20
            reasons.append("Form login terdeteksi")

    except:
        score += 10
        reasons.append("Gagal mengambil konten")

    return score, reasons
