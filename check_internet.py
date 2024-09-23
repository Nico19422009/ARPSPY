import socket
import os
import subprocess
import platform

def check_internet():
    try:
        # Prüfen, ob Google erreichbar ist (über Port 80)
        socket.create_connection(("www.google.com", 80), 2)
        return True
    except OSError:
        return False

def get_local_ip():
    # Holen der lokalen IP-Adresse des Computers
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def scan_network():
    local_ip = get_local_ip()
    network = '.'.join(local_ip.split('.')[:-1]) + '.'
    
    print(f"Scanning Netzwerk: {network}0/24\n")
    
    # Pingt IPs im Netzwerk und speichert die Antworten
    for i in range(1, 255):
        ip = network + str(i)
        try:
            # Prüfen, ob IP erreichbar ist
            if platform.system().lower() == "windows":
                output = subprocess.check_output(f"ping -n 1 -w 500 {ip}", shell=True)
            else:
                output = subprocess.check_output(f"ping -c 1 -W 500 {ip}", shell=True)
            
            # Wenn das Ping erfolgreich war, Hostnamen abrufen
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except socket.herror:
                hostname = "Unbekannt"
            
            print(f"IP-Adresse: {ip} - Hostname: {hostname}")
        except subprocess.CalledProcessError:
            # IP nicht erreichbar
            continue

if __name__ == "__main__":
    if check_internet():
        print("Internetverbindung ist vorhanden.\n")
        scan_network()
    else:
        print("Keine Internetverbindung. Abbruch...")
        exit(1)
