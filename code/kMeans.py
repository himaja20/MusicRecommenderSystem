import numpy
from sklearn.cluster import KMeans
#from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import pairwise_distances
import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt

def main():	
	scaler = StandardScaler()
	songDataFrame = numpy.genfromtxt('./featureSet', delimiter=",")
	userSongFrame = numpy.genfromtxt('./userSongs1.txt',delimiter=",", autostrip=True)
	userSongFrame.astype(float)
	
	scaler.fit(songDataFrame)
	scaler.fit(userSongFrame)

	songDataFrameScaled = scaler.transform(songDataFrame)
	userSongFrameScaled = scaler.transform(userSongFrame)

	#songDataFrameScaled = preprocessing.scale(songDataFrame)
	kmeans_plus_plus=KMeans(n_clusters=10, init='k-means++', n_init=10, max_iter=100)
	rVal = kmeans_plus_plus.fit(songDataFrameScaled)
	centers = rVal.cluster_centers_

	clusterArray = []
        for i in range(rVal.n_clusters):
                clusterArray.append(numpy.where(rVal.labels_ == i)[0])

	distances = pairwise_distances(songDataFrameScaled, centers, metric='euclidean')
	clusters = numpy.argmin(distances,axis=1)
	#getting one component for each song
	#print {i: numpy.where(rVal.labels_ == i)[0] for i in range(rVal.n_clusters)} 
	
	applyUserOnSongDistance = pairwise_distances(userSongFrameScaled,centers,metric='euclidean')
	print('applyUserOnSongDistance -------------------- ')
	print applyUserOnSongDistance
	userSongBelongsToClusters = numpy.argmin(applyUserOnSongDistance,axis=1)
	print('userSongBelongsToClusters --------------------  ')
	print userSongBelongsToClusters

	userFavouriteCluster = clusterArray[userSongBelongsToClusters]
	print ('userFavouriteCluster --------------------- ' ) 
	print userFavouriteCluster
	distWithinCluster = pairwise_distances(userSongFrameScaled,userFavouriteCluster,metric='euclidean')
	medianSong = numpy.median(distWithinCluster,axis=1)
	print ('median -----------------------------------')
	print medianSong
		
	#plotSamples = PCA(n_components=2).fit_transform(songDataFrameScaled)
	#plotting all songs with 2 components
	#plotPoints = PCA(n_components=2).fit_transform(songDataFrameScaled)
	
	#plotClusters(plotSamples,clusters)
	#plotAllSongs(plotPoints)
	#plotPitchVsTimbre(songDataFrameScaled)

def plotClusters(plotSamples,clusters):
	x = plotSamples[:,0]
	y = plotSamples[:,1]
	fig = plt.figure(1,figsize=(10,8))
	plt.scatter(x,y,c=clusters,alpha=0.5)
	plt.savefig("./plots/clusters")


def plotAllSongs(plotPoints):
	x = plotPoints[:,0]
	y = plotPoints[:,1]

	fig = plt.figure(1, figsize=(10, 8))
	plt.xlim(-8,8)
	plt.ylim(-8,8)
	plt.scatter(x,y,c="blue",alpha = 0.5)
	plt.savefig("./plots/allsongs")

	
if __name__ == "__main__":
	main()
