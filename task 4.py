n = input()
lst = n.split()
lst2 = []
for i in lst:
    if i not in lst2:
        lst2.append(i)


print(lst2)  