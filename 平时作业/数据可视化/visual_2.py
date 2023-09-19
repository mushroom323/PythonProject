import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.figure(figsize=(8, 6.5))
items = ['酒店旅游', '转账红包', '餐饮美食', '日用百货', '交通出行', '充值缴费', '服饰装扮', '互助保障']
spendings = [21914.00, 19973.20, 10379.59, 9859.93, 8351.35, 2428.54, 950.83, 827.20]
colors = ['r', 'y', 'slateblue', 'g', 'm', 'cyan', 'darkorange', 'lawngreen']
plt.pie(spendings, labels=items, colors=colors, labeldistance=1.05, autopct='%.2f%%', textprops={'fontsize': 9, 'color': 'k'})
plt.title('2020年支付宝年支出情况')
plt.savefig('visual_2.png')
plt.show()
