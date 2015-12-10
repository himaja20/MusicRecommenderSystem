import numpy
from sklearn.cluster import KMeans
#from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import pairwise_distances
import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt

def getPCA():
	scaler = StandardScaler()
	songDataFrame = numpy.genfromtxt('./featureSetSample', delimiter=",")
	scaler.fit(songDataFrame)
	songDataFrameScaled = scaler.transform(songDataFrame)
		
	array = numpy.hsplit(songDataFrameScaled, [12, 24, 25])	
	
	pcaPitch = PCA(n_components=1).fit_transform(array[0])
	pcaTimbre = PCA(n_components=1).fit_transform(array[1])

	plt.scatter(pcaPitch, pcaTimbre)
	plt.savefig('pcaPVST.png')

if __name__ == "__main__":
	getPCA()        
