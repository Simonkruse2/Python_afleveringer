import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataA = pd.read_csv('https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&Tid=2008K1%2C2020K1&CIVILSTAND=G%2CF', delimiter=';')
dataB1 = pd.read_csv('https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&CIVILSTAND=TOT', delimiter=';')
# dataB = pd.read_csv('https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND(Head)=U%2CTOT&OMR%C3%85DE=*&Tid=2020K1', delimiter=';')
dataB2 = pd.read_csv('https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&CIVILSTAND=U', delimiter=';')

pct08 = dataA['INDHOLD'][1] / dataA['INDHOLD'][0] * 100
pct20 = dataA['INDHOLD'][3] / dataA['INDHOLD'][2] * 100
pctchange = pct20 - pct08

print('5.A')
print('------------------------------------------')
print("Divorced procent in '08",pct08)
print("Divorced procent in '20",pct20)
print('Change in procent',pctchange)
print('------------------------------------------')

# 1:6 to skip "hele landet" at index 0
largestCities = dataB1.sort_values('INDHOLD', ascending=False)[1:6]
yo = dataB2.loc[1]
# lc = dataB2.loc['Region Hovedstaden', 'Region Midtjylland']

print('5B')
print(largestCities)
print('------------------------------')
# print(dataB2.loc[0])
# print(yo)
# print(dataB)


# print(dataA)
# print(dataA.head(1))
# print(dataA.tail(1))
# print(dataArr)
# print( pd.DataFrame(dataA) )
# print(dataA)


# dataArr = np.array(dataA)
# data_frame = pd.read_csv('dk-stat-all-tables.csv')
# list([]).append()

# df = pd.read_csv('dk-stat-all-tables.csv')


