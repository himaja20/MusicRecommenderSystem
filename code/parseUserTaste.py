from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row

APP_NAME = "Music Recommender Systems"

def main(sc):

        sqlContext = SQLContext(sc)
        tasteProfileRdd = sc.textFile("hiveIp/insertStmtsFile13")

        # Load a text file and convert each line to a Row.
        tasteProfile = tasteProfileRdd.filter(lambda l:len(l) > 0)
        parsedSplits = tasteProfile.map(lambda l: l.split('|'))
        userTaste = parsedSplits.map(lambda p: Row(songId=p[0], songName=p[1], artistName=p[2], playCount=p[3], lastModified=p[4], dateAdded=p[5], artistId=p[6], foreignId=p[7], catalogId=p[8]))

        # Infer the schema, and register the DataFrame as a table.
        schemaUserTaste = sqlContext.inferSchema(userTaste)
        schemaUserTaste.registerTempTable("userTaste")

        test1 = sqlContext.sql("SELECT songId FROM userTaste WHERE playCount >= 5 AND playCount <= 10")

        songIds = test1.map(lambda p: "songIds: " + p.songId)
        for i in songIds.collect():
                print i

if __name__ == "__main__":
        conf = SparkConf().setAppName(APP_NAME)
        sc   = SparkContext(conf=conf)

        # Execute Main functionality
        main(sc)

