import numpy as np
filename = './befkbhalderstatkode.csv'

bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
print(type(bef_stats_df),' of size: ',bef_stats_df.size)
print('The skip_header=1 means that we have only the data\n\nfirst line:\n',bef_stats_df[0],'\nlast line\n',bef_stats_df[len(bef_stats_df)-1])

dd = bef_stats_df
mask = (dd[:,0] == 1998) # for all rows filter column/index = 0 to be 1998
dd[mask]

mask = (dd[:,0] == 2015) & (dd[:,2] == 18) & (dd[:,3] == 5100)
print(dd[mask])
#plt.axis([0,10,300,600])
#plt.bar(dd[:,1], dd[:,4])
np.sum(dd[mask][:,4])
#plt.show()

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
          10: 'Amager Vest', 99: 'Udenfor'}

def number_of_people_per_neighbourhood(n, mask):
    all_people_in_given_n = dd[mask & (dd[:,1] == n)]
    sum_of_people = all_people_in_given_n[:,4].sum() # index 4 is no of 'PERSONER'
    return sum_of_people

french_mask = (dd[:,0] == 2015) & (dd[:,3] == 5130)
german_mask = (dd[:,0] == 2015) & (dd[:,3] == 5180)

french = np.array([number_of_people_per_neighbourhood(n, french_mask) for n in neighb.keys()])
#print(french)
germans = np.array([number_of_people_per_neighbourhood(n, german_mask) for n in neighb.keys()])
german_children = (dd[:,2] == 2015) & (dd[:,3] == 5180) & (dd[:,2] <= 0)

index_max_fr = np.argmax(french)
index_max_de = np.argmax(germans)
print('german children', german_children)
# msg = 'The majority of {} {} are living in {}'
# french_neighbourhood_index = list(neighb.keys())[index_max_fr]
# print(msg.format(french.max(), 'Frenchmen', neighb[french_neighbourhood_index]))
# print(msg.format(germans.max(), 'Germans', neighb[list(neighb.keys())[index_max_de]]))