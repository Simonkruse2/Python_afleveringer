import numpy as np
filename = './befkbhalderstatkode.csv'

bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
print(type(bef_stats_df),' of size: ',bef_stats_df.size)
print('The skip_header=1 means that we have only the data\n\nfirst line:\n',bef_stats_df[0],'\nlast line\n',bef_stats_df[len(bef_stats_df)-1])

dd = bef_stats_df

# How many german children were 0 years old in 2015?
# Hvorfor kan man ikke lave flere masks?
mask_german = (dd[:,3] == 5180)
mask_year_2015 = (dd[:,0] == 2015)
mask_age = (dd[:2] == 0)
german_mask = (dd[:,3] == 5180) & (dd[:,0] == 2015) & (dd[:,2] == 0)
print(np.sum(dd[german_mask][:,4]))

# create a function that can take any combination of the 4 parameters:AAR,BYDEL,ALDER,STATKODE and return population data
def pop(*argv):
    mask = ((dd[:,0] == argv[0]) & (dd[:,1] == argv[1]) & (dd[:,2] == argv[2]) & (dd[:,3] == argv[3]))
    print(np.sum(dd[mask]))

# pop(2015,1,0,5180)

# create a new function like previous so that it can sum values for all ages if age is not provided to the function
def sumPop(aar=None, bydel=None, statkode=None, alder=None,):
    if(statkode is None and bydel is None and alder is None):
        mask = (dd[:,0] == aar)
        print("Pop data without citizenship, age or area parameter:\n",dd[mask],"\nPop count:\n", np.sum(dd[mask][:4]) )
    if(alder is None and statkode is not None):
        mask = (dd[:,0] == aar) & (dd[:,1] == bydel) & (dd[:,3] == statkode)
        print("Pop data without age parameter:\n",dd[mask],"\nPop count:\n", np.sum(dd[mask][:4]) )
    # else:
    if(aar is not None and bydel is not None and statkode is not None and alder is not None):
        mask = (dd[:,0] == aar) & (dd[:,1] == bydel) & (dd[:,2]== alder) & (dd[:,3] == statkode)
        print("Pop data with parameters:\n",dd[mask],"\nPop count:\n", np.sum(dd[mask][:4]) )
# sumPop(2015)
# sumPop(aar=2015,bydel=1, alder=15, statkode=5180)
sumPop(aar=2015,bydel=1, statkode=5180)
# sumPop(2015,1,5180)
