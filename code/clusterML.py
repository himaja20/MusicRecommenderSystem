from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark import SparkConf, SparkContext 
from numpy import array
from math import sqrt

APP_NAME = "Music Recommender Systems"

def main(sc):
	# Load and parse the data
	data = sc.textFile("./featureSet")
	parsedData = data.map(lambda line: array([x for x in line.split(',')]))

	# Build the model (cluster the data)
	clusters = KMeans.train(parsedData, 2, maxIterations=10,
		runs=10, initializationMode="random")

	# Evaluate clustering by computing Within Set Sum of Squared Errors
	def error(point):
	    center = clusters.centers[clusters.predict(point)]
	    return sqrt(sum([x**2 for x in (point - center)]))

	WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
	print("Within Set Sum of Squared Error = " + str(WSSSE))

	# Save and load model
	clusters.save(sc, "myModelPath")
	sameModel = KMeansModel.load(sc, "myModelPath")

if __name__ == "__main__":
        conf = SparkConf().setAppName(APP_NAME)
        sc   = SparkContext(conf=conf)

        # Execute Main functionality
        main(sc)
 
