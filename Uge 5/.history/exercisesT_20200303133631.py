import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&Tid=2008K1%2C2020K1&CIVILSTAND=TOT%2CG%2CF')
# data_frame = pd.read_csv('dk-stat-all-tables.csv')
# list([]).append()

# df = pd.read_csv('dk-stat-all-tables.csv')

dataArr = np.array(data)

# print(data.head(1))
# print(data.tail(1))
# print(dataArr)
# print( pd.DataFrame(data) )
# print(data)


