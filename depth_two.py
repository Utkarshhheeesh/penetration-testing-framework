import requests
from bs4 import BeautifulSoup

def find_depth_two_links(links):
    with open("output/depth_two.html", "w", encoding="utf-8") as f:
        for url in links:
            f.write("<hr>")
            f.write(f"<h2>{url}</h2>\n")
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    for link2 in soup.find_all('a'):
                        href2 = link2.get('href')
                        if href2 and href2.startswith('http'):
                            f.write(f"<h4>{href2} ----->>> Status Code: {response.status_code}</h4>\n")
            except Exception as e:
                f.write(f"<h4>{url} ----->>> Failed to fetch</h4>\n")