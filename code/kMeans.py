import numpy
from sklearn.cluster import KMeans
#from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import pairwise_distances
from scipy import stats
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
	print len(clusters)
	
	applyUserOnSongDistance = pairwise_distances(userSongFrameScaled,centers,metric='euclidean')
	userSongBelongsToClusters = numpy.argmin(applyUserOnSongDistance,axis=1)
	userFavCluster = int(stats.mode(userSongBelongsToClusters)[0][0])

	userFavouriteCluster = clusterArray[userFavCluster]
	songsInFavCluster = numpy.empty([len(userFavouriteCluster),25])
	for i in range(len(userFavouriteCluster)):
		songsInFavCluster[i] = songDataFrameScaled[userFavouriteCluster[i]]
		
	distWithinCluster = pairwise_distances(userSongFrameScaled,songsInFavCluster,metric='euclidean')
	medianSong =  numpy.median(distWithinCluster,axis=1)
	print ('median -----------------------------------')
	print medianSong
	recoSongs = [0 for a in range(len(medianSong))]
	for k in range(len(medianSong)):
		recoSongs[k] = find_nearest(distWithinCluster[k],medianSong[k])

	print recoSongs	
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

def find_nearest(array,value):
    idx = (numpy.abs(array-value)).argmin()
    return idx

def arg_median(a,axis):
        if len(a) % 2 == 1:
                return numpy.where( a == numpy.median(a,axis))
        else:
                l,r = len(a)/2 -1, len(a)/2
                left = numpy.partition(a, l)[l]
                right = numpy.partition(a, r)[r]
                return numpy.where(a == left)[0][0]
	
if __name__ == "__main__":
	main()
