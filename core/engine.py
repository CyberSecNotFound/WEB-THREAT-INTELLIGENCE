from modules.url_analysis import analyze_url
from modules.whois_scan import whois_check
from modules.content_scan import content_scan
from modules.malware_scan import malware_scan
from ml.model import ml_predict
from core.scoring import verdict
import tldextract

def run_engine(url):
    total_score = 0
    report = []

    s, r = analyze_url(url)
    total_score += s
    report += r

    domain = ".".join(tldextract.extract(url)[1:])
    s, r = whois_check(domain)
    total_score += s
    report.append(r)

    s, r = content_scan(url)
    total_score += s
    report += r

    s, r = malware_scan(url)
    total_score += s
    report += r

    ml = ml_predict(url, total_score)
    if ml == 1:
        total_score += 40
        report.append("Machine Learning: MALICIOUS")

    status, color = verdict(total_score)
    return total_score, status, color, report
