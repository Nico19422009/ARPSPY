import socket

def check_internet():
    try:
        # Prüfen, ob Google erreichbar ist (über Port 80)
        socket.create_connection(("www.google.com", 80), 2)
        return True
    except OSError:
        return False

if __name__ == "__main__":
    if check_internet():
        exit(0)  # Erfolgreich, Internet ist vorhanden
    else:
        exit(1)  # Kein Internet
