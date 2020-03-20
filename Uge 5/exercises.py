import pandas as pd
import matplotlib.pyplot as plt
# url = 'https://api.statbank.dk/v1/tables'
url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&Tid=2008K1%2C2020K1&CIVILSTAND=G%2CF'
dst = pd.read_json(url)
dst.to_csv('FOLK1A.csv.csv', encoding='utf-8', index=False)
print(dst.head())
# print(dst[:20])



#---- plt.bar(ages, no_citicens, width=0.5, linewidth=0, align='center') # first plot: danes
# plt.ticklabel_format(useOffset=False)
# plt.axis([0, max(ages) + 10, 0, 17000])
# title = 'Distribution of CPH Citizens in {}'.format(2015)
# plt.title(title, fontsize=12)
# plt.xlabel("Ages", fontsize=10)
# plt.ylabel("Amount", fontsize=10)
# plt.tick_params(axis='both', which='major', labelsize=10)

# p1 = plt.bar(ages, no_citicens, width=0.5, linewidth=0, align='center', color='red')
# p2 = plt.bar(ages_f, no_citicens_f, width=0.5, linewidth=0, align='center', color='yellow') 
# plt.legend([p1,p2],['danish','foreigners'],loc=1)    
# plt.show()