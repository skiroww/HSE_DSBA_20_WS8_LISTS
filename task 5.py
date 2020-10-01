n = input()
lst = n.split()
lst2 = []
lstlast=[]
n = ''
for i in range(0,len(lst)+1):
    for j in range(0,len(lst)+1):
        n = lst[i:j]
        lst2.append(n)
for i in lst2:
    if i !=[]:
        lstlast.append(i)
print(lstlast)