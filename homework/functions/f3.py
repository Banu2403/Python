#task1
def esl_eded(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    
    return sum == n#cemine


#task3
def yuvarlaq(eded, deqiqlik):
    return round(eded, deqiqlik)

print(yuvarlaq()) 

#task4 
def xosbext(n):
    a = n // 100000
    b = (n // 10000) % 10
    c = (n // 1000) % 10
    d = (n // 100) % 10
    e = (n // 10) % 10
    f = n % 10
    
    return a + b + c == d + e + f

#task5
def uzun_il(il):
    if il % 400 == 0:
        return True
    if il % 100 == 0:
        return False
    if il % 4 == 0:
        return True
    return False


def ferq(g1, a1, i1, g2, a2, i2):
    gun1 = i1 * 365 + a1 * 30 + g1
    gun2 = i2 * 365 + a2 * 30 + g2

    if gun1 > gun2:
        return gun1 - gun2
    else:
        return gun2 - gun1

print(uzun_il(2024))     
print(ferq(1,1,2020, 5,1,2020))

#task6
def ededi_orta(arr):
    sum = 0
    for i in arr:
        sum += i
    
    return sum / len(arr)
print(ededi_orta([1, 2, 3, 4, 5])) 

#task7
def ayir(arr):
    musbet = []
    menfi = []
    sifir = 0
    
    for i in arr:
        if i > 0:
            musbet.append(i)
        elif i < 0:
            menfi.append(i)
        else:
            sifir += 1
    
    return musbet, menfi, sifir

#task8
def max_min(arr):
    max_eded = 0
    min_eded =0 
    
    for i in arr:
        if i > max_eded:
            max_eded = i
        if i < min_eded:
            min_eded = i
    
    return max_eded, min_eded

#task9
def ters(arr):
    return arr[::-1]

#task10
def prime(arr):
    res = []
    
    for n in arr:
        if n > 1:
            sade = True
            
            for i in range(2, n):
                if n % i == 0:
                    sade = False
            
            if sade == True:
                res.append(n)
    
    return res