n=int(input("eded yaz:"))
m=n
rn=0
while n>0:
    rn=rn*10+n%10
    n=n//10
if m==rn: print("Palindromdur")
else : print("deyil")