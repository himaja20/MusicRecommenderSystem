import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.decomposition import PCA

songDataFrame = numpy.genfromtxt('code/featureSet', delimiter=",")
songDataFrameScaled = preprocessing.scale(songDataFrame)

kmeans_plus_plus=KMeans(n_clusters=10, init='k-means++', n_init=10, max_iter=100)
rVal = kmeans_plus_plus.fit(songDataFrameScaled)

plotPoints = PCA(n_components=2).fit_transform(songDataFrameScaled)

