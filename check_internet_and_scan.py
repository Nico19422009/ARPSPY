import socket
import os
import subprocess
import platform
import time

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

def print_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█'):
    # Funktion zum Drucken eines Ladebalkens
    percent = f"{100 * (iteration / float(total)):.1f}"
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()  # Neue Zeile am Ende des Fortschrittsbalkens

def scan_network():
    local_ip = get_local_ip()
    network = '.'.join(local_ip.split('.')[:-1]) + '.'
    total_ips = 254  # Es gibt 254 mögliche Adressen im /24-Netz
    print(f"Scanning Netzwerk: {network}0/24\n")

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

        # Fortschrittsbalken aktualisieren
        print_progress_bar(i, total_ips, prefix='Fortschritt:', suffix='Fertig', length=50)

if __name__ == "__main__":
    if check_internet():
        print("Internetverbindung ist vorhanden.\n")
        scan_network()
    else:
        print("Keine Internetverbindung. Abbruch...")
        exit(1)
