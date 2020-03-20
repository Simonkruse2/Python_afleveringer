import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&Tid=2008K1%2C2020K1&CIVILSTAND=G%2CF', delimiter=';')

pct08 = data['INDHOLD'][1] / data['INDHOLD'][0] * 100
pct20 = data['INDHOLD'][3] / data['INDHOLD'][2] * 100
pctchange = pct20 - pct08

print('---------------------------------')
print("Divorced procent in '08",pct08)
print("Divorced procent in '20",pct20)
print('Change in procent',pctchange)
print('---------------------------------')


# print(data)
# print(data.head(1))
# print(data.tail(1))
# print(dataArr)
# print( pd.DataFrame(data) )
# print(data)


# dataArr = np.array(data)
# data_frame = pd.read_csv('dk-stat-all-tables.csv')
# list([]).append()

# df = pd.read_csv('dk-stat-all-tables.csv')


