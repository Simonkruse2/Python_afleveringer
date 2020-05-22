# Exercise meanshift
# load 'iris_data.csv' into a dataframe
# get unique labels (Species column)
# plot with a scatter plot each iris flower sample colored by label (3 different colors)
# use: MeanShift and estimate_bandwidth from sklearn.cluster to first estimate bandwidth and then get the clusters (HINT: estimate_bandwidth() takes an argument: quantile set it to 0.2 for best result
# print out labels, cluster centers and number of clusters (as returned from the MeanShift function
# create a new scatter plot where each flower is colored according to cluster label
# add a dot for the cluster centers
# Compare the 2 plots (colored by actual labels vs. colored by cluster label)

iris = open("iris_data.csv", "r", encoding="utf8")

print(iris)