import numpy as np
filename = './befkbhalderstatkode.csv'

bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
print(type(bef_stats_df),' of size: ',bef_stats_df.size)
print('The skip_header=1 means that we have only the data\n\nfirst line:\n',bef_stats_df[0],'\nlast line\n',bef_stats_df[len(bef_stats_df)-1])


dd = bef_stats_df
mask_german = (dd[:,3] == 5180)
mask_year_2015 = (dd[:,0] == 2015)
mask_age = (dd[:2] == 0)
german_mask = (dd[:,3] == 5180) & (dd[:,0] == 2015) & (dd[:,2] == 0)
# print(dd[mask])
print(np.sum(dd[german_mask][:,4]))
print(dd[mask_age & mask_year_2015 & mask_age)]