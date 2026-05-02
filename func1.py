import random

# 1
def task1():
    list = []
    for i in range(10):
        list.append(random.randint(1, 100))

    count = 0
    for x in list:
        if x % 3 == 0 and x % 5 != 0:
            count += 1

    return list, count


# 2
def task2():
    lst = []
    for i in range(10):
        lst.append(random.randint(-10, 30))

    found = False
    total = 0

    for x in lst:
        if found == False:
            if x < 0:
                found = True
        else:
            total += x

    return lst, total


# 3
def task3():
    lst = []
    for i in range(10):
        lst.append(random.randint(-30, 20))

    found = False
    total = 0

    for x in lst:
        if found == False:
            if x > 0:
                found = True
        else:
            total += x

    return lst, total


# 4
def task4():
    lst = []
    for i in range(20):
        lst.append(random.randint(-100, 100))

    max_value = 0
    min_value =0

    for x in lst:
        if x > max_value:
            max_value = x
        if x < min_value:
            min_value = x

    return lst, max_value, min_value



print(task1())
print(task2())
print(task3())
print(task4())
