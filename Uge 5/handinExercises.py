import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataA = pd.read_csv('https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&Tid=2008K1%2C2020K1&CIVILSTAND=G%2CF', delimiter=';')
dataB1 = pd.read_csv('https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&CIVILSTAND=TOT', delimiter=';')
# dataB = pd.read_csv('https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND(Head)=U%2CTOT&OMR%C3%85DE=*&Tid=2020K1', delimiter=';')
dataB2 = pd.read_csv('https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&CIVILSTAND=U', delimiter=';')
dataC1 = pd.read_csv('https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=101&CIVILSTAND=*&Tid=*', delimiter=';')

filename = './FOLK1A.csv'
test = np.genfromtxt(filename, delimiter=';', dtype=np.uint, skip_header=1)
testData = pd.read_csv(filename)

status = {1:'I alt', 2:'Ugift', 3:'Gift/separeret', 4: 'Enke/enkemand', 5:'Fraskilt'}
# test = np.genfromtxt('https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=101&CIVILSTAND=*&Tid=*', delimiter=';', dtype=np.uint, skip_header=1)

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
# ls = largestCities.head(2)

def highestPctOfNeverMarried():
    pctList = {}
    lst = [1,2,32,50,73]
    for number in lst:
        area = dataB2['OMRÅDE'][number]
        val = dataB2['INDHOLD'][number] / dataB1['INDHOLD'][number] * 100
        # print(area, 'Ugifte i procent', val)
        pctList.update({area: val})
    print('Highest pct of never married \n', max(zip(pctList.values(), pctList.keys())))

def printMeYo():
    # deezMask = (data[:,0] == 2015) & (data[:,2] <= 65) & (data[:,3] == countrycode)
    # return np.sum(data[deezMask][:,4])
    deezMask = (test[:,1] == 'I alt')
    print(np.sum(test[deezMask][:,3]))
    # for i in dataC1:
        # if dataC1['CIVILSTAND'][i] == 'I alt':
        # print('------------------------------------------------ IN FOR LOOOP')
            # print('YO!')
            # print(dataC1['INDHOLD'][i])
        # if dataC1['CIVILSTAND'][idx] == 'I alt':
        #     print(dataC1['INDHOLD'][idx])
        # if dataC1['CIVILSTAND'][i] == 'I alt':
        # print(dataC1['INDHOLD'][i]

# def changesInPctPlot():
#     yearsToDisp = []
#     eastpopulation = []
#     westpopulation = []

#     for key, value in years.items():
#         yearsToDisp.append(key)

#     for key, value in east.items():
#         eastpopulation.append(value)
    
#     for key, value in west.items():
#         westpopulation.append(value)

#     plt.plot(yearsToDisp, eastpopulation, linewidth=2)
#     plt.plot(yearsToDisp, westpopulation, linewidth=2)
#     plt.title("Number of poeple in %", fontsize=18)
#     plt.xlabel("Year", fontsize=10)
#     plt.xticks(yearsToDisp, rotation=65)
#     plt.tick_params(axis='both', labelsize=10)
#     plt.show()



regionH = dataB2['INDHOLD'][1] / dataB1['INDHOLD'][1] * 100
    # regionM = dataB2['INDHOLD'][73] / dataB1['INDHOLD'][73] * 100
    # regionSD = dataB2['INDHOLD'][50] / dataB1['INDHOLD'][50] * 100
    # regionS = dataB2['INDHOLD'][32] / dataB1['INDHOLD'][32] * 100
    # kbh = dataB2['INDHOLD'][2] / dataB1['INDHOLD'][2] * 100

print('5.B')
# print(largestCities)
# print('------------------------------')
# print('Region H procent',regionH)
highestPctOfNeverMarried()
# print(dataB2.loc[0])
# print(yo)
# print(dataB)


print('5.C')
# print(dataC1)
printMeYo()
# print(testData)

# plt.bar(ages, no_citicens, width=0.5, linewidth=0, align='center') # first plot: danes
# plt.ticklabel_format(useOffset=False)
# # plt.axis([0, max(ages) + 10, 0, 17000])
# title = 'Distribution of CPH Citizens in {}'.format(2015)
# plt.title(title, fontsize=12)
# plt.xlabel("Year", fontsize=10)
# plt.ylabel("Number of poeple in %", fontsize=10)
# plt.tick_params(axis='both', which='major', labelsize=10)

# p1 = plt.bar(ages, no_citicens, width=0.5, linewidth=0, align='center', color='red')
# p2 = plt.bar(ages_f, no_citicens_f, width=0.5, linewidth=0, align='center', color='yellow') 
# plt.legend([p1,p2],['danish','foreigners'],loc=1)    
# plt.show()
