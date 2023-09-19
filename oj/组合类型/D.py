str = input()
set1 = set({})
for i in str:
    set1.add(i)
list1 = list(set1)
list1.sort()
for i in range (0, len(list1) - 1):
    print(list1[i], end = '')
print(list1[len(list1) - 1])


