import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# 数据抽取，注意这里的读取会读取出 index 信息
raw = pd.read_csv('BeijingPM20100101_20151231.csv')
condition = raw['year'] == 2015
after = raw.loc[condition]
# 存储 2015 的 PM 信息。不存储 index 信息
after.to_csv('BeijingPM2015.csv', index=False)

new = pd.read_csv('BeijingPM2015.csv')

# 含空值列及对应空值数量统计输出
print('【缺失值统计】')
print(new.isnull().sum())

# 删除缺失率过高的列
new = new.drop('PM_Dongsihuan', axis=1)

# 前向填充
new['cbwd'] = new['cbwd'].fillna(method='ffill')
new['precipitation'] = new['precipitation'].fillna(method='ffill')
new['Iprec'] = new['Iprec'].fillna(method='ffill')
new['DEWP'] = new['DEWP'].fillna(method='ffill')
new['HUMI'] = new['HUMI'].fillna(method='ffill')
new['PRES'] = new['PRES'].fillna(method='ffill')
new['TEMP'] = new['TEMP'].fillna(method='ffill')

# 线性插值
new = new.interpolate(method='linear').round(2)

# 精度调整
new['PM_Dongsi'] = new['PM_Dongsi'].round()
new['PM_Nongzhanguan'] = new['PM_Nongzhanguan'].round()
new['PM_US Post'] = new['PM_US Post'].round()

new.to_csv('BeijingPM2015_Process.csv', index=False)
