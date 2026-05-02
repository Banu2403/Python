#1
A = [1, 2, 3, 4, 5]
B = [6, 7, 8, 9, 10]

C = []

i = 0
while i < 5:
    C.append(A[i])
    C.append(B[i])
    i += 1

print(C)

#2
A = [1, -2, 0, -3]

neg = []
zero = []
pos = []

for x in A:
    if x < 0:
        neg.append(x)
    elif x == 0:
        zero.append(x)
    else:
        pos.append(x)

B = neg + zero + pos

print(B)


#3

#4&5
A = [1, 2, 3, 4, 2, 8, 7]
B = [4, 2, 5, 7, 8]

C = []
D = []

for x in A:

    if x in B and x not in C:
        C.append(x)

    if not x in B and x not in D:
        D.append(x)

print(C)
print(D)