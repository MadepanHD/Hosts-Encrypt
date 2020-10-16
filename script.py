import random
from getpass import getpass

def obfuscate(ip=None, line=100):

    

    if ip is None and port is None:
        print("[S] Ip and Password cannot be None!")
        exit()
    print(f"[S] Encrypting... (Line input {line})")
    real = random.randint(0, line)
    obfuscated = []
    for x in range(line):
        if x == real:
            obfuscated.append(f"{ip} growtopia1.com")
            obfuscated.append(f"{ip} growtopia2.com")
            print(x)
        else:
            pagar = []
            for z in range(random.randint(1, 100)):
                pagar.append("#")
            

            obfuscated.append(f"{''.join(pagar)}{random.randint(1, 999)}.{random.randint(1, 999)}.{random.randint(1, 999)}.{random.randint(1, 999)} growtopia1.com")
            obfuscated.append(f"{''.join(pagar)}{random.randint(1, 999)}.{random.randint(1, 999)}.{random.randint(1, 999)}.{random.randint(1, 999)} growtopia2.com")

    file = open("hosts", "w")
    file.write("\n".join(obfuscated))
    print(f"{line} lines of hosts saved to hosts.txt")
    getpass("Enter to continue...")

def obfuscate2(ip2=None, line2=100, last=None):

    

    if ip2 is None and port2 is None:
        print("[S] Ip and Password cannot be None!")
        exit()
    print(f"[S] Encrypting... (Line input {line2})")
    real2 = random.randint(0, line2)
    obfuscated2 = []
    for x in range(line2):
        if x == real2:
            obfuscated2.append(f"{ip2} {last}")
            obfuscated2.append(f"{ip2} {last}")
            print(x)
        else:
            pagar2 = []
            for z in range(random.randint(1, 100)):
                pagar2.append("#")
            

            obfuscated2.append(f"{''.join(pagar2)}{random.randint(1, 999)}.{random.randint(1, 999)}.{random.randint(1, 999)}.{random.randint(1, 999)} {last}")
            obfuscated2.append(f"{''.join(pagar2)}{random.randint(1, 999)}.{random.randint(1, 999)}.{random.randint(1, 999)}.{random.randint(1, 999)} {last}")

    file = open("hosts", "w")
    file.write("\n".join(obfuscated2))
    print(f"{line2} lines of hosts saved to hosts.txt")
    getpass("Enter to continue...")

def gthosts():
    print("[S] Input IP Hosts for continue..")
    ip = input("[S] IP Address > ")
    print("[S] Recommended Input : 300 - 1000 lines Ip ( MAX : 100000 )")
    line = input("[S] How Many Want to Input > ")

    if line == "" or line == " ":
        line = 300

    try:
        line = int(line)
    except:
        print("Line must be Number!")
        exit

    obfuscate(ip, line)

def otherhosts():
    print("[S] Input IP Hosts for continue..")
    ip2 = input("[S] IP Address > ")
    print("[S] Recommended Input : 300 - 1000 lines Ip ( MAX : 100000 )")
    line2 = input("[S] How Many Want to Input > ")
    last = input("[S] Last Ip / DNS (example : pornhub1.net) ")

    if line2 == "" or line2 == " ":
        line2 = 300

    try:
        line2 = int(line2)
    except:
        print("Line must be Number!")
        exit

    obfuscate2(ip2, line2, last)

class main:
    print("[S] Hosts Encrypt by MadepanHD")
    print("""
[+]=======[ Layer 7 ]=======[+]=======[ Layer 4 ]=======[+]
            1: Server_data.php      [ Growtopia ]
            2: Game Server     [ Other ] 
[+]=====================================================[+]
""")

    choice_mode = input("[S] Choose Mode [1 - 2]: ")

    if choice_mode == "1":
        gthosts()
    
    if choice_mode == "2":
        otherhosts()
