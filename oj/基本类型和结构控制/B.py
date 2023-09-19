string = input()
aOrigin, bOrigin = string.split()
aString = aOrigin.lstrip('0')
bString = bOrigin.lstrip('0')
aList = list(aString)
i = 1
for c in bString:
    aList.insert(i, c)
    if i + 2 > len(aList):
        i += 1
    else:
        i += 2
print(''.join(aList))