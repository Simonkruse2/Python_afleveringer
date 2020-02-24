import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

filename = './befkbhalderstatkode.csv'
data = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}

nordicCountryCodes = {5104: 'Finland', 5106: 'Island', 5110: 'Norge', 5120: 'Sverige'}

def getSomething(hood):
    deezMask = (data[:,0] == 2015) & (data[:,1] == hood)
    return np.sum(data[deezMask][:,4])

def getOldPeople():
    deezMask = (data[:,0] == 2015) & (data[:,2] <= 65) 
    return np.sum(data[deezMask][:,4])

def getOldNordicPeople(countrycode):
    deezMask = (data[:,0] == 2015) & (data[:,2] <= 65) & (data[:,3] == countrycode)
    return np.sum(data[deezMask][:,4])
    
def getSumOfOldNordicPeople():
    lst = {}
    for key, value in nordicCountryCodes.items():
        # print(value, getOldNordicPeople(key))
        lst.update({value: getOldNordicPeople(key)})
    return lst    

def getSumPerHood():
    lst = {}
    for key, value in neighb.items():
        # print(value, getSomething(key))
        lst.update({value: getSomething(key)})
    return lst

def displayPlotOfHoodsPop():
    lst = getSumPerHood()
    hoodsSorted = OrderedDict(sorted(lst.items(), key=lambda x: x[1]))
    cityAreas = []
    sumOfPeople = []
    for key, value in hoodsSorted.items():
        cityAreas.append(key)
        sumOfPeople.append(value)

    plt.bar(cityAreas, sumOfPeople, width=0.5, linewidth=0, align='center')
    title = 'Population in various areas in cph'
    plt.title(title, fontsize=12)
    plt.xticks(cityAreas, rotation=65)
    plt.tick_params(axis='both', labelsize=8)

    plt.show()

def displayPopulationOverTheYears():
    # lst = getSumPerHood()
    # hoodsSorted = OrderedDict(sorted(lst.items(), key=lambda x: x[1]))
    # cityAreas = []
    # sumOfPeople = []
    # for key, value in hoodsSorted.items():
    #     cityAreas.append(key)
    #     sumOfPeople.append(value)

    plt.figure()
    input_values = range(1,6)
    squares = [x ** 2 for x in input_values]

    plt.plot(input_values, squares, linewidth=5)

    # Set chart title and label axes. 
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    # Set size of tick labels.

    plt.tick_params(axis='both', labelsize=14)


# print(getSumPerHood())
# displayPlotOfHoodsPop()
# print('Number of people above the age of 65 --',getOldPeople())
# print(getSumOfOldNordicPeople())
displayPopulationOverTheYears()
