import matplotlib.pyplot as plt

year = ['1953年', '1964年', '1982年', '1990年', '2000年', '2010年', "2020年"]
population = [58260, 69458, 100818, 113368, 126583, 133972, 141178]
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.grid(axis='y', which='major')
plt.xlabel('年份 years')
plt.ylabel('（万人 10000 persons）')
plt.title('历次普查全国人口')
plt.ticklabel_format(style='plain')
plt.subplots_adjust(left=0.15)
plt.bar(year, population, width=0.5, align='center', color='slateblue', bottom=0.8)
for x, y in zip(year, population):
    plt.text(x, y, format(y, ','), ha='center', fontsize=9)
plt.legend(['人口（万）'])
plt.savefig('visual_1.png')
plt.show()
