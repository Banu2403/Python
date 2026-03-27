n = int(input("yaz birsey: "))
i = 0
even = 0
odd = 0

while i < 10:
   
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    
    i += 1

print("Cüt faiz:", even * 100 / 10, "%")
print("Tək faiz:", odd * 100 / 10, "%")
