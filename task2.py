n = input()
m = input()
lst = n.split()
lst2 = m.split()
str = 'NO'
for i in lst:
    for j in lst2:
        if int(i)==int(j):
            str = 'YES'


print(str)