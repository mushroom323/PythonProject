list1 = []
n, m = input().split()
n = eval(n)
m = eval(m)
order = [int(i) for i in input().split()]
load = 0
for page in order:
    if page not in list1:
        load += 1
        if len(list1) == n:
            list1.pop(0)
        list1.append(page)
    else:
        list1.remove(page)
        list1.append(page)
print(load)
list1.sort()
for i in range (0, len(list1) - 1):
    print(list1[i], end = " ")
print(list1[len(list1) - 1], end = '')

