# Exercise meanshift
# load 'iris_data.csv' into a dataframe
# get unique labels (Species column)
# plot with a scatter plot each iris flower sample colored by label (3 different colors)
# use: MeanShift and estimate_bandwidth from sklearn.cluster to first estimate bandwidth and then get the clusters (HINT: estimate_bandwidth() takes an argument: quantile set it to 0.2 for best result
# print out labels, cluster centers and number of clusters (as returned from the MeanShift function
# create a new scatter plot where each flower is colored according to cluster label
# add a dot for the cluster centers
# Compare the 2 plots (colored by actual labels vs. colored by cluster label)
from sklearn.cluster import estimate_bandwidth

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# Indlæs filen enten som xlsx(excel fil) eller som .csv 
iris = pd.read_excel("iris_data.xlsx")

# Lav one hot encoding på species, så de hver især enten er 0 eller 1 i en art række. 
iris_data = pd.get_dummies(iris,columns=['Species'])
print(iris_data.head())

# Tjek efter nullværdier 
print('rows before drop n/a',len(iris_data))
missing = iris_data[iris_data.isnull().any(axis=1)]

# Fjern evt. nullværdier, i det her tilfælde er det ingen. 
iris_data = iris_data.dropna()
print('rows after',len(iris_data))


iris_data.plot.scatter(x = 1, y =3)
plt.show()



