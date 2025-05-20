import requests
from bs4 import BeautifulSoup

def extract_links_gui(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a') if a.get('href')]
        return "\n".join(links) if links else "[!] No links found."
    except Exception as e:
        return f"[!] Error extracting links: {str(e)}"
