from core.banner import banner
from core.engine import run_engine
from colorama import Fore, init

init(autoreset=True)
banner()

url = input(Fore.CYAN + "[+] Target URL: ")

score, status, color, report = run_engine(url)

print(Fore.WHITE + "\n========== FULL SCAN RESULT ==========")
print(f"Target     : {url}")
print(f"Risk Score : {score}\n")

for r in report:
    print(f" - {r}")

if color == "GREEN":
    print(Fore.GREEN + f"\nVERDICT: {status}")
elif color == "YELLOW":
    print(Fore.YELLOW + f"\nVERDICT: {status}")
else:
    print(Fore.RED + f"\nVERDICT: {status}")

print(Fore.RED + "\n[ WEB THREAT INTELLIGENCE | 404 Not Found CyberSec ]")
