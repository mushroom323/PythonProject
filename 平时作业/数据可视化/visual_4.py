import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('八年级期末考试成绩表.xlsx')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
courses = ['地理分数', '历史分数', '政治分数', '生物分数', '物理分数', '英语分数']

fig, ax = plt.subplots(2, 3, figsize=(20, 10))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5, hspace=0.45)
for i in range(len(courses)):
    x = int(i / 3)
    y = int(i % 3)
    ax[x][y].set_xlabel('分数', fontsize=12)
    ax[x][y].set_ylabel('学生数量', fontsize=12)
    ax[x][y].set_title('八年级期末考试' + courses[i] + '成绩分布')
    if courses[i] == '英语分数':
        ax[x][y].hist(df[courses[i]], 12, (0, 120), facecolor='blue', edgecolor='black')
    else:
        ax[x][y].hist(df[courses[i]], 10, (0, 100), facecolor='blue', edgecolor='black')
    
plt.savefig('visual_4.png')
plt.show()
