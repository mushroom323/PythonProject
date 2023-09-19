import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
loupan = pd.read_csv('loupan.csv', sep=',', encoding="utf-8")

'''总价'''
print('\n【总价最贵】')
print(loupan.loc[loupan['总价（万元/套）'] == loupan['总价（万元/套）'].max()])
print('\n【总价最便宜】')
print(loupan.loc[loupan['总价（万元/套）'] == loupan['总价（万元/套）'].min()])
print('\n【总价中位数】')
print(loupan['总价（万元/套）'].median())

'''均价'''
print('\n【均价最贵】')
print(loupan.loc[loupan['均价（元/平米）'] == loupan['均价（元/平米）'].max()])
print('\n【均价最便宜】')
print(loupan.loc[loupan['均价（元/平米）'] == loupan['均价（元/平米）'].min()])
print('\n【均价中位数】')
print(loupan['均价（元/平米）'].median())

'''总价异常值'''
print("\n【总价异常值】")
min_mask = loupan['总价（万元/套）'] < (loupan['总价（万元/套）'].mean() - 3 * loupan['总价（万元/套）'].std())
max_mask = loupan['总价（万元/套）'] > (loupan['总价（万元/套）'].mean() + 3 * loupan['总价（万元/套）'].std())
mask = min_mask | max_mask
print(loupan.loc[mask])

'''均价异常值'''
print('\n【均价异常值】')
plt.boxplot(x=loupan['均价（元/平米）'])
plt.show()
q1 = loupan['均价（元/平米）'].quantile(q=0.25)
q3 = loupan['均价（元/平米）'].quantile(q=0.75)
low_mask = loupan['均价（元/平米）'] < q1 - 1.5*(q3-q1)
high_mask = loupan['均价（元/平米）'] > q3 + 1.5*(q3-q1)
mask = low_mask | high_mask
print(loupan.loc[mask])

print('\n【均价离散化】')
bins = [0, 30000, 40000, 50000, 60000, 80000, 200000]
cuts = pd.cut(loupan['均价（元/平米）'], bins)
print('离散房屋数量：')
print(pd.value_counts(cuts, sort=False))
pd.set_option('display.float_format', lambda x: format(x, '.2%')) 
print('\n离散所占比例：')
print(pd.value_counts(cuts, normalize=True, sort=False))