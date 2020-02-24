import numpy as np
filename = './befkbhalderstatkode.csv'

bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
print(type(bef_stats_df),' of size: ',bef_stats_df.size)
print('The skip_header=1 means that we have only the data\n\nfirst line:\n',bef_stats_df[0],'\nlast line\n',bef_stats_df[len(bef_stats_df)-1])

dd = bef_stats_df
mask_german = dd[:,3] == 5180
mask_year_2015 = dd[:,0] == 2015
mask_age = dd[:2] == 0
mask = mask_german & mask_age & mask_year_2015
german_mask = (dd[:,3] == 5180) & (dd[:,0] == 2015) & (dd[:2] == 0)
french_mask = (dd[:,0] == 2015) & (dd[:,3] == 5130)
# print(dd[mask])
print(dd[(mask_year_2015) & (mask_german) & (mask_age)][:,4])