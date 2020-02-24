import numpy as np
import matplotlib.pyplot as plt
filename = './befkbhalderstatkode.csv'

data = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}

def getSomething(hood):
    deezMask = (data[:,1] == hood) & (data[:,0] == 2015)
    return np.sum(data[deezMask][:,4])

def getSumPerHood():
    for key, value in neighb.items():
        # sumOfPeople = getSomething(key)
        print(value, getSomething(key))

getSumPerHood()


plt.bar(years_of_interest, y_values, width=0.5, linewidth=0, align='center')
title = 'Increase of foreign citizens - {} to {}'.format(
    years_of_interest[0], years_of_interest[1])
plt.title(title, fontsize=12)
plt.ticklabel_format(useOffset=False)
plt.xticks(years_of_interest)
plt.ticklabel_format(useOffset=False)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.axis([2013, 2016, 0, 88000]) # starting instead from 0 on y-axis

# plt.show()