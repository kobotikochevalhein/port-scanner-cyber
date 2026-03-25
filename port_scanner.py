
import socket
import argparse
from datetime import datetime

def scan_port(target, port):
    """Teste si un port est ouvert sur la cible"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # 1 seconde max
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except:
        return False

def main():
    parser = argparse.ArgumentParser(description="🔍 Scanner de ports - Projet Cyber")
    parser.add_argument("target", help="IP ou hostname à scanner (ex: 127.0.0.1 ou scanme.nmap.org)")
    parser.add_argument("-p", "--ports", type=str, default="1-1000", help="Plage de ports (ex: 1-1000 ou 80,443,8080)")
    args = parser.parse_args()

    print(f" Scanner de ports lancé le {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f" Cible : {args.target}")
    print("-" * 50)


    if "-" in args.ports:
        start, end = map(int, args.ports.split("-"))
        ports = range(start, end + 1)
    else:
        ports = [int(p) for p in args.ports.split(",")]

    open_ports = []
    for port in ports:
        if scan_port(args.target, port):
        open_ports.append(port)
        print(f"✅ Port {port} ouvert !")

    print("-" * 50)
    print(f"✅ Scan terminé ! {len(open_ports)} port(s) ouvert(s) trouvés : {open_ports}")

if __name__ == "__main__":
    main()

