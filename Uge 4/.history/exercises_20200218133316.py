import numpy as np
filename = './befkbhalderstatkode.csv'

dd = bef_stats_df

np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}

def getSomething(aar, bydel, alder, statkode):
    deezMask = (dd[:,0] == aar) & (dd[:,3] == statkode) & (dd[:,2] <= alder) & (dd[:,1] == bydel)
    # deezSum = np.sum(dd[deezMask][:,4])
    deezData = dd[deezMask]
    print(deezData)