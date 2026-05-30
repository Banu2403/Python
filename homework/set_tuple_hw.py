#1
# dost1 = {'Minecraft', 'Roblox', 'Brawl Stars'} 
# dost2 = {'Roblox', 'PUBG', 'Minecraft'}
# print(dost1.intersection(dost2))


#2
# fruits = ('alma', 'armud', 'alma', 'banan', 'armud', 'alma')
# print("alma:",fruits.count('alma'))
# print("armud:",fruits.count('armud'))
# print("banan:", fruits.count('banan'))

#3
# heroes = [('Batman', 85), ('Robin', 70), ('Superman', 99)]

# for names, score in heroes:
#     if score > 80:
#         print(names)

#4
# ansler = {10, 20, 10, 30, 20, 50, 40}
# print(sorted(ansler))

#5

# def func(ballar):
#   return max(ballar,)#?

# ballar = {'Əli': 85, 'Aytən': 95, 'Murad': 78}
# print(func(ballar))


#6
###????????


#7
# def sum(qiymetler):
#     tot = 0
#     for qiymet in qiymetler:
#         tot += qiymet
#     return tot

# qiymetler = (12, 15, 8, 20)

# print(sum(qiymetler))

#8
# def combine(plan1, plan2):
#     return plan1.union(plan2) #|

# plan1 = {'Kino', 'Park', 'Muzey'}
# plan2 = {'Park', 'Zoopark'}

# print(combine(plan1, plan2))

#9
#?


#10
# def unique(soz):
#     return set(soz.replace(" ", ""))
# print(unique('qələm'))

#11
# def cut_sec(reqemler):
#     cut_lar = []
#     for reqem in reqemler:
#         if reqem % 2 == 0:
#             cut_lar.append(reqem)
#     return cut_lar

# reqemler = [1, 2, 3, 4, 5, 6, 7]
# print(cut_sec(reqemler))

#12
#?

#13
# def search(ref, kitab):
#     if kitab in ref:
#         return True
#     else:
#         return False

# ref = ('Riyaziyyat', 'Nağıllar', 'Tarix')
# kitab = 'Nağıllar'

# print(search(ref, kitab))

#14
# def delete_it(num):
#     for i in range(len(num)):
#         if num[i] < 0:
#             num[i] = 0
#     return num

# num = [5, -2, 9, -1, 4]
# print(delete_it(num))


#15
# def captilaze(adlar):
#     new = []
#     for ad in adlar:
#         new.append(ad.capitalize())
#     return new

# adlar = ['əli', 'vəli', 'aysel']
# print(captilaze(adlar))


# #16 #islemedi
# def new(qiymetler):
#     for i in qiymetler:
#         qiymetler[i] = qiymetler[i] - 2
#     return qiymetler

# qiymetler = {'kitab': 10, 'qələm': 3, 'dəftər': 5}
# print(new(qiymetler))

# #17
# def eksik_tap(reqemler):
#     for i in range(len(reqemler)):###1,11
#        if i not in reqemler:
#             return i

# reqemler = [1, 2, 3, 4, 5, 7, 8, 9, 10]

# print(eksik_tap(reqemler)) 


#18

# def diff(cagirilanlar, gelenler):
#     return cagirilanlar - gelenler ####difference

# cagirilanlar = {'Anar', 'Leyla', 'Nurlan', 'Səma'}
# gelenler = {'Anar', 'Səma'}

# print(diff(cagirilanlar, gelenler))

#19#################?????????????
# def sirala(komandalar):
#     komandalar.sort()
#     komandalar.reverses()
#     return komandalar

# komandalar = [('Qarabağ', 15), ('Neftçi', 10), ('Sabah', 12)]

# print(sirala(komandalar))

#20
# def birlesdirmek(a, b):
#     a.update(b)
#     return a

# sinif_a = {'Əli': 90, 'Vəli': 85}
# sinif_b = {'Aysu': 92, 'Leyla': 88}

# print(birlesdirmek(sinif_a, sinif_b))


#21

def reverses(sozler):
    new = []
    for soz in sozler:
        new.append(soz[::-1])
    return new

sozler = ['ata', 'ana', 'kitab']

print(reverses(sozler))

#22############??????????????????

#24

def func(reqemler):
    tek = []
    cut = []

    for i in reqemler:
        if i % 2 == 0:
            cut.append(i)
        else:
            tek.append(i)

    return {'tək': tek, 'cüt': cut}

reqemler = [1, 2, 3, 4, 5, 6]

print(func(reqemler))

#25

def cevr(metn):
    emojiler = {
        'gülüş': '😄',
        'ürək': '❤️',
        'ulduz': '⭐'
    }

    for soz in emojiler:
        metn = metn.replace(soz, emojiler[soz])

    return metn

metn = 'Mənim sənə ürək dolusu gülüş göndərirəm'

print(cevr(metn))

#27
def themostlikedfilms(filmler):
    ans = []
    for ad in filmler:
        if filmler[ad] > 8:
            ans.append(ad)

    return ans

filmler = {'Qaraca qız': 9, 'Qisasçılar': 8.5, 'Pis film': 4}

print(themostlikedfilms(filmler))

#28
def sirala(adlar):
    adlar.sort()
    return adlar

adlar = ['Zəhra', 'Aylin', 'Cavid']

print(sirala(adlar))

#29
def birlesdir(sozler):
    return " ".join(sozler)

sozler = ['Mən', 'Python', 'öyrənirəm']

print(birlesdir(sozler))


#30
# ???