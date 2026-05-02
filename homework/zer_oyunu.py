import random
p1 = 0
p2 = 0
for number in range(5):
    #p1
    p1 += random.randint(1, 6) + random.randint(1, 6)
    #p2
    p2 += random.randint(1, 6) + random.randint(1, 6)

print("P1:", p1)
print("P2:", p2)

if p1 > p2:
    print("Player 1 wins")
elif p2 > p1:
    print("Player 2 wins")
else:
    print("tie")