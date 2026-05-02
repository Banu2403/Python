#3
def digit(n):
    if n >0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

#4
def op(n,n1,n2):
    if n == "+":
        print(n1 + n2)
    elif n == "-":
        print(n1 - n2)
    elif n == "*":
        print(n2 * n1)
    elif n == "/":
        print(n2 / n1)
    else:
        print("Invalid operator")

n = (input("choose an operator: "))
n1 = int(input("enter a number: "))
n2 = int(input("enter another number: "))

print(op(n,n1,n2))


#5 kubun sahesi
def length(n):
    return n * n

n = int(input("enter a number: "))
print(length(n))

#6 sade ededlerin tapilmasi
def isprime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False

n = int(input("enter a number: "))
print(isprime(n))


#7  faktorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("enter a number: "))
print(factorial(n))

#8 bir ededin digerine quvveti
def quvvet(n,n2):
    return n ** n2

n = int(input("enter a number: "))
n2 = int(input("enter another number: "))
print(quvvet(n,n2))

#9 
def ededlerarasicemi(n,n2):
    if n > n2:
        sum = 0
        for i in range(n2, n + 1):
            sum += i
        return sum
#10 massivdeki en boyuk ededin tapilmasi
def max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

list = [1, 2, 3, 4, 5]
print(max(list))