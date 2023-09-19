size = eval(input())
scoreString = input()
sum = 0
count = 0
scoreList = scoreString.split()
for score in scoreList:
    sum += int(score)
    if int(score) >= 60:
        count += 1
print("average = %.1f" % (sum / size))
print("count = %d" % count)