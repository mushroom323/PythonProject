import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('iris.csv')
xnames = ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']
ynames = ['Petal.Width', 'Petal.Length', 'Sepal.Width', 'Sepal.Length']

Species = iris['Species'].unique()
Colors = ['dodgerblue', 'orange', 'g']

fig, ax = plt.subplots(4, 4, figsize=(16, 16))

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5, hspace=0.5)

for x in range(len(xnames)):
    for y in range(len(ynames)):
        for i in range(len(Species)):
            ax[x][y].scatter(iris.loc[iris['Species'] == Species[i], xnames[x]], iris.loc[iris['Species'] == Species[i], ynames[y]], s=7, c=Colors[i], label=Species[i])
            ax[x][y].set_title(xnames[x] + ' vs ' + ynames[y])
            ax[x][y].grid(True)
            ax[x][y].set_xlabel(xnames[x])
            ax[x][y].set_ylabel(ynames[y])
labelname = []
for i in range(len(Species)):
    labelname.append('lris-' + Species[i])
plt.figlegend(labels=labelname, loc='upper left', bbox_to_anchor=(-0., 0.4, 0.5, 0.5))
plt.savefig('visual_3.png')
plt.show()
