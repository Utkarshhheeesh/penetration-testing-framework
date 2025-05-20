from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def capture_screenshot_gui(url):
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1280,1024')

        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(2)
        driver.save_screenshot("output/screenshot.png")
        driver.quit()
        return "[+] Screenshot saved to output/screenshot.png"
    except Exception as e:
        return f"[!] Screenshot capture failed: {str(e)}"
