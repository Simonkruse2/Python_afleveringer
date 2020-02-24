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