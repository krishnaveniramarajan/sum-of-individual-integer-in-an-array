import array as a
total = []
res = []
res1=a.array('i', [])
rem = 0
n = int(input("enter the number"))
for i in range(n):
    a = int(input("enter the value"))
    total.append(a)
print(total)
for j in total:
    res=0
    while j != 0:
        rem = j % 10
        res = res + rem
        j = j // 10
    res1.append(res)
for i in res1:
    print(i,end=' ')


