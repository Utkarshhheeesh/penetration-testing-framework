# Modules/regex_matcher.py
import re
import requests
from urllib.parse import urlparse

def normalize_url(url):
    parsed = urlparse(url)
    if not parsed.scheme:
        url = "http://" + url  # Default to http if no scheme
    return url

def run_regex(domain):
    url = normalize_url(domain)
    try:
        response = requests.get(url, timeout=10)
        content = response.text
    except requests.RequestException as e:
        return f"[!] Error fetching URL content: {e}"

    # Regex for emails
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    emails = re.findall(email_pattern, content)

    # Regex for IPv4 addresses
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    ips = re.findall(ip_pattern, content)

    result = ""
    if emails:
        result += "Emails:\n" + "\n".join(set(emails)) + "\n\n"
    else:
        result += "Emails:\nNone found\n\n"

    if ips:
        result += "IPs:\n" + "\n".join(set(ips)) + "\n"
    else:
        result += "IPs:\nNone found\n"

    return result

# GUI wrapper function
def run_regex_gui(domain):
    return run_regex(domain)
