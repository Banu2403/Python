#1
X = int(input("1ci ededi daxil ele:"))
Y =int(input("2ci ededi daxil ele:"))
if X%Y == 0:
    print('yes')
else:
    print("no")

 #2
 num = int(input("ededi daxil ele:"))
if num % 3== 0 or num % 5 ==0 or num % 7 == 0:
      print("yes")
else:
    print("no")
    
#3
num = int(input("ededi daxil ele:"))
if num< 0:
    print(-num)
else:
    print(num)

#4

num = (input("ededi daxil ele:"))
inputun_leni = len(num)
if inputun_leni > 4:
    print("leng coxdur")
else:
    print(inputun_leni)

#5
num = int(input("ededi daxil ele:"))
bes = (num // 10000)%10
d = (num // 1000)% 10
u = (num // 100)% 10
i = (num // 10)% 10
bir =  num % 10

if bes == bir and d == i:
    print("it's palindrom:)")
else:
   print("try again:(")

#6
X= (input("new password:"))
Y =(input("checking:"))
if X == Y:
    print("--Accepted succesfully--")
else:
    print("--Acces denied--")
