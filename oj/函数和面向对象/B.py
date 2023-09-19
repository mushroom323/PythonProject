class myStack:
    mystack = []
 
    def __init__(self, _list1):
        self.mystack = _list1
    
    def push(self, num):
        for i in range(0, len(num)):
            self.mystack.append(num[i])

    def pop(self, num):
        nums = num
        poplist = []
        if (num > len(self.mystack)):
            nums = len(self.mystack)
        for i in range(0, nums):
            poplist.append(self.mystack.pop())
        return nums, poplist


list1 = [] 
n = eval(input())
str1 = input().split()
for i in range(0, n):
    list1.append(eval(str1[i]))
mine = myStack(list1)

poplist = []
popnum = 0

str1 = input()
if (str1[0:3] == "pop"):
    str1 = str1.lstrip("pop ")
    num = eval(str1)
    tmpnum, tmplist = mine.pop(num)
    popnum += tmpnum
    for i in range(0, len(tmplist)):
        poplist.append(tmplist[i])
else:
    str1 = str1.lstrip("push ")
    strlist = str1.split()
    pushlist = []
    for i in range(0, len(strlist)):
        pushlist.append(eval(strlist[i]))
    mine.push(pushlist)

str1 = input()
if (str1[0:3] == "pop"):
    str1 = str1.lstrip("pop ")
    num = eval(str1)
    tmpnum, tmplist = mine.pop(num)
    popnum += tmpnum
    for i in range(0, len(tmplist)):
        poplist.append(tmplist[i])
else:
    str1 = str1.lstrip("push ")
    strlist = str1.split()
    pushlist = []
    for i in range(0, len(strlist)):
        pushlist.append(eval(strlist[i]))
    mine.push(pushlist)

print("len = ", end="")
print(len(mine.mystack), end="")
if (len(mine.mystack) > 0):
    print(", data = ", end="")
    for i in range(0, len(mine.mystack) - 1):
        print(mine.mystack[i], end=" ")
    print(mine.mystack[len(mine.mystack) - 1])
else:
    print("")

print("len = ", end="")
print(popnum, end="")
if (popnum > 0):
    print(", data = ", end="")
    for i in range(0, popnum - 1):
        print(poplist[i], end=" ")
    print(poplist[popnum - 1], end="")
