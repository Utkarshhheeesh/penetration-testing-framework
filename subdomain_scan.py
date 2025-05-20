# Modules/subdomain_finder.py
import socket
from urllib.parse import urlparse

def normalize_domain(domain):
    parsed = urlparse(domain if '://' in domain else '//' + domain)
    return parsed.netloc if parsed.netloc else parsed.path

def find_subdomains(domain):
    domain = normalize_domain(domain)
    found_subdomains = []
    try:
        with open("wordlist.txt", "r") as file:
            subdomains = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return "[!] wordlist.txt file not found."

    for sub in subdomains:
        subdomain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(subdomain)
            found_subdomains.append(f"{subdomain} -> {ip}")
        except socket.gaierror:
            pass  # Subdomain does not exist
        except Exception as e:
            return f"[!] Error occurred: {e}"

    if found_subdomains:
        return "\n".join(found_subdomains)
    else:
        return "[!] No subdomains found."

# GUI wrapper function
def find_subdomains_gui(domain):
    return find_subdomains(domain)
