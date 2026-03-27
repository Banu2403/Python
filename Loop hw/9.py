i = 2
#XARICI
while i <= 100:
    n = 2
    is_prime = True
    #DAXILI
    while n < i:
        if i % n == 0:
            is_prime = False
        n +=1
    
    if is_prime:
        print(i)
    i +=1