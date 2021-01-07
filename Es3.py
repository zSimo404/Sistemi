  
def fibonacci(k):
    if k==0:
        return 0
    elif k==1:
        return 1
    else:
        fibonacci(k-1)+fibonacci(k-2)
    

n=int(input("numero max"))       
for k in range (n):
    print(fibonacci(k))