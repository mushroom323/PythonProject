import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)

raw = pd.read_csv('BeijingPM2015_Process.csv')

print('【缺失值统计】')
print(raw.isnull().sum())