import numpy as np
filename = './befkbhalderstatkode.csv'

data = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}

def getSomething(hood):
    deezMask = (data[:,1] == hood)
    # deezSum = np.sum(dd[deezMask][:,4])
    deezData = data[deezMask]
    print(deezData)
print(neighb[o])
print(neighb.get(10))
# def getSumPerHood():
#     for hood in neighb:
#         print(hood.value(), getSomething(hood))

# getSumPerHood()