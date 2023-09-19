n = eval(input())
dict1 = {}
for i in range (0, n):
    str = input()
    cat, dog = str.split()
    dict1[dog] = cat
str = input()
while str != "dog":
    if str in dict1:
        print(dict1[str])
    else:
        print("dog")
    str = input()
