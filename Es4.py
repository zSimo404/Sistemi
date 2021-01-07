import string

lista=[]

def rot():
    while True:
        print("Inserisci 1 se vuoi criptare la frase, 2 se la vuoi decriptare")
        num=int(input())
        if(num==1 or num==2):
            break

    if num==1:
        lista=input("inserisci la frase")
        
        for k in lista:

            if chr(ord(lista[k])+15) <= chr(ord('z')):
                lista[k]=chr(ord(lista[k])+15)
            else:
                val=ord(lista[k])+15-ord('z')
                lista[k]=chr(ord(lista[k])+val)

    elif num==2:
        lista=input("inserisci la frase")
    
        for k in lista:
            if chr(ord(lista[k])-15) >= chr(ord('a')):
                lista[k]=chr(ord(lista[k])-15)
            else:
                val=ord(lista[k])-15+ord('a')
                lista[k]=chr(ord(lista[k])-val)

    print(lista)
        
rot()