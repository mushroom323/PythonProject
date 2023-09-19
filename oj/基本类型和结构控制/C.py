ans = ""
max = eval(input())
for number in range(2, max + 1):
    flag = True
    for i in range(2, (int)(number/2) + 1):
        if number % i == 0:
            flag = False
            break
    if flag:
        ans += str(number) + " "
ans1 = ans.rstrip(" ")
print(ans1)