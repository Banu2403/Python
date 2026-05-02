# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1

list = []
for i in range(5):
    row=[]
    for j in range(5):
        if j % 2 == 0:
            row.append("1")
        else:
            row.append("0")
    list.append(row)


# 1 0 0 0 1
# 0 1 0 1 0
# 0 0 1 0 0
# 0 1 0 1 0
# 1 0 0 0 1
list= []
for i in range(5):
    row = []

    for j in range(5):
        if  j == 5 - i - 1 or j == i:
            row.append("1")
        else:
            row.append("0")
    list.append(row)
    print()


# 1 0 1


