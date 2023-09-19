money = eval(input())
if money <= 60000:
    print("%.2f" % 0)
elif money <= 100000:
    print("%.2f" % ((money - 60000) * 0.03))
elif money <= 180000:
    print("%.2f" % (1200 + (money - 100000) * 0.10))
elif money <= 300000:
    print("%.2f" % (9200 + (money - 180000) * 0.18))
elif money <= 480000:
    print("%.2f" % (30800 + (money - 300000) * 0.25))
elif money <= 700000:
    print("%.2f" % (75800 + (money - 480000) * 0.30))
elif money <= 1000000:
    print("%.2f" % (141800 + (money - 700000) * 0.35))
else:
    print("%.2f" % (246800 + (money - 1000000) * 0.45))

'''
Decimal('1.125').quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)

if money < 6000:
    print(round(0, 2))
elif money <= 100000:
    print(format(round((money - 60000) * 0.03, 2), 2))
elif money <= 180000:
    print(format(round(1200 + (money - 100000) * 0.10, 2), 2))
elif money <= 300000:
    print(format(round(9200 + (money - 180000) * 0.18, 2), 2))
elif money <= 480000:
    print(format(round(30800 + (money - 300000) * 0.25, 2), 2))
elif money <= 700000:
    print(format(round(75800 + (money - 480000) * 0.30, 2), 2))
elif money <= 1000000:
    print(format(round(141800 + (money - 700000) * 0.35, 2), 2))
else:
    print(format(round(246800 + (money - 1000000) * 0.45, 2), 2))
'''
