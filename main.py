# === GUI_Main.py ===
import os
import tkinter as tk
from tkinter import scrolledtext
from Modules.port_scan import scan_ports_gui
from Modules.whois_lookup import get_whois_gui
from Modules.find_links import extract_links_gui
from Modules.regex_extractor import run_regex_gui
from Modules.subdomain_scan import find_subdomains_gui
from Modules.screenshot import capture_screenshot_gui

# Create output directory if not exists
os.makedirs("output", exist_ok=True)

# GUI App
class PentestingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pentesting Framework")
        self.root.geometry("700x600")

        tk.Label(root, text="Enter Target URL / Domain:").pack(pady=5)
        self.target_entry = tk.Entry(root, width=60)
        self.target_entry.pack(pady=5)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Port Scan", command=self.run_port_scan).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="WHOIS Lookup", command=self.run_whois).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Extract Links", command=self.run_link_extractor).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Regex Match", command=self.run_regex).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Find Subdomains", command=self.run_subdomains).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(button_frame, text="Capture Screenshot", command=self.run_screenshot).grid(row=1, column=2, padx=5, pady=5)

        self.output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25)
        self.output_area.pack(pady=10)

    def get_target(self):
        return self.target_entry.get().strip()

    def run_port_scan(self):
        target = self.get_target()
        if target:
            result = scan_ports_gui(target)
            self.output_area.insert(tk.END, f"\n[Port Scan]\n{result}\n")

    def run_whois(self):
        target = self.get_target()
        if target:
            result = get_whois_gui(target)
            self.output_area.insert(tk.END, f"\n[WHOIS]\n{result}\n")

    def run_link_extractor(self):
        target = self.get_target()
        if target:
            # Ensure full URL with scheme
            if not target.startswith("http://") and not target.startswith("https://"):
                target = "http://" + target
            result = extract_links_gui(target)
            self.output_area.insert(tk.END, f"\n[Links]\n{result}\n")

    def run_regex(self):
        target = self.get_target()
        if target:
            result = run_regex_gui(target)
            self.output_area.insert(tk.END, f"\n[Regex Match]\n{result}\n")

    def run_subdomains(self):
        target = self.get_target()
        if target:
            result = find_subdomains_gui(target)
            self.output_area.insert(tk.END, f"\n[Subdomains]\n{result}\n")

    def run_screenshot(self):
        target = self.get_target()
        if target:
            result = capture_screenshot_gui(target)
            self.output_area.insert(tk.END, f"\n[Screenshot Capture]\n{result}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = PentestingApp(root)
    root.mainloop()
