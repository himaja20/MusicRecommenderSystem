from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row

APP_NAME = "Music Recommender Systems"

def main(sc):

        sqlContext = SQLContext(sc)
        tasteProfileRdd = sc.textFile("userTaste/*")
	songRdd = sc.textFile("songsDict/*")
        # Load a text file and convert each line to a Row.
        tasteProfile = tasteProfileRdd.filter(lambda l:len(l) > 0)
        parsedSplits = tasteProfile.map(lambda l: l.split('\t'))
        userTaste = parsedSplits.map(lambda p: Row(userId=p[0], songId=p[1], playCount=p[2]))

	individualSong = songRdd.map(lambda l:l.split('|'))
        songData = individualSong.map(lambda s: Row(songId=s[0],featureSet=s[1]))

        # Infer the schema, and register the DataFrame as a table.
        schemaUserTaste = sqlContext.inferSchema(userTaste)
        schemaUserTaste.registerTempTable("userTaste")

	schemaSongData = sqlContext.inferSchema(songData)
        schemaSongData.registerTempTable("songData")

	test2 = sqlContext.sql("select * from songData limit 5")
	songIds = test2.map(lambda p: "songIds: " + s.songId)
        #test1 = sqlContext.sql("SELECT distinct * FROM userTaste limit 5")

        #songIds = test1.map(lambda p: "songIds: " + p.songId)
        for i in songIds.collect():
               print i

if __name__ == "__main__":
        conf = SparkConf().setAppName(APP_NAME)
        sc   = SparkContext(conf=conf)

        # Execute Main functionality
        main(sc)

