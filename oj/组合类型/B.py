n = eval(input())
list1 = []
num = input().split()
for i in range (0, n):
    list1.append(eval(num[i]))

m = eval(input())
list2 = []
num = input().split()
for i in range (0, m):
    list2.append(eval(num[i]))

'''
交集
'''
list3 = [x for x in list1 if x in list2]
list3.sort()
for i in range (0, len(list3) - 1):
    print(list3[i], end = " ")
print(list3[len(list3) - 1])

'''
并集
'''
list3 = list1 + [x for x in list2 if x not in list1]
list3.sort()
for i in range (0, len(list3) - 1):
    print(list3[i], end = " ")
print(list3[len(list3) - 1])



list3 = [x for x in list1 if x not in list2]
list3.sort()
for i in range (0, len(list3) - 1):
    print(list3[i], end = " ")
print(list3[len(list3) - 1])


