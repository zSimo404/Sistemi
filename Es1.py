import random
import string

def generatore_password():
    
    pass_easy = string.digits + string.ascii_letters #caratteri alfanumerici
    pass_hard = string.digits + string.ascii_letters + string.punctuation #caratteri ascii

    print("Inserisci 1 se vuoi una password semplice, 2 se ne vuoi una complicata")
    num=int(input())

    if num==1:
        k=8
        tipo=pass_easy
    elif num==2:
        k=20
        tipo=pass_hard
    else:
        print("Numero selezionato non corretto, la password creata sarà semplice") 
        k=8
        tipo=pass_easy

    password=""
    for _ in range(k):
        char = random.choice(tipo)
        password = password + char
    
    print(password)

generatore_password()



