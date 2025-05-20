# === Modules/port_scan.py ===
import nmap

def scan_ports_gui(target):
    scanner = nmap.PortScanner()
    try:
        print(f"[*] Scanning ports on {target}...")
        scanner.scan(hosts=target, arguments='-Pn -T4 -p 1-1000')
        output = ""

        if scanner.all_hosts():
            for host in scanner.all_hosts():
                output += f"Host: {host} ({scanner[host].hostname()})\n"
                output += f"State: {scanner[host].state()}\n"

                if 'tcp' in scanner[host]:
                    for port in scanner[host]['tcp']:
                        port_data = scanner[host]['tcp'][port]
                        state = port_data['state']
                        name = port_data['name']
                        output += f"Port {port}/tcp - State: {state}, Service: {name}\n"
                else:
                    output += "No TCP ports found.\n"
        else:
            output = f"[!] No scan results for {target}. The host may be down or not responding."

    except Exception as e:
        output = f"[!] Error scanning {target}: {str(e)}"

    return output
