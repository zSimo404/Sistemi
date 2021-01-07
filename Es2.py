import random
import string

def mac():
    tipo = string.digits + "ABCDEF" 
    mac = ""
    for x in range (6):
        if x < 5:
            for _ in range(2):
                coppia = random.choice(tipo)
                mac = mac + coppia
            mac = mac + ":"    
        else:
            for _ in range(2):
                coppia = random.choice(tipo)
                mac = mac + coppia
                 
    print(mac)    

mac()