n = input()
lst = []
m = int(input())
for i in range (0,len(n),m):
    lst.append(n[i:i+m])

for i in lst:
    print(i)
