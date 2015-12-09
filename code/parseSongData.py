from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import Row

APP_NAME = "Music Recommender Systems"

def main(sc):

        sqlContext = SQLContext(sc)
        songRdd = sc.textFile("processedSongData/")

        # Load a text file and convert each line to a Row.
        individualSong = songRdd.map(lambda l:l.split('\t'))
        songData = individualSong.map(lambda p: Row(trackId=p[0], loudness=(float(p[1]) if p[1] != u'' else 0), songId=p[36], title=p[43], pitches=p[32], timbre=p[33]))

        # Infer the schema, and register the DataFrame as a table.
        schemaSongData = sqlContext.inferSchema(songData)
        schemaSongData.registerTempTable("songData")

        #test1 = sqlContext.sql("SELECT * FROM userTaste WHERE playCount >= 5 AND playCount <= 10")
        test1 = sqlContext.sql("SELECT * FROM songData WHERE songId = ''")

        songIds = test1.map(lambda p: "songIds: " + p.songId)
        for i in songIds.collect():
                print i

if __name__ == "__main__":
        conf = SparkConf().setAppName(APP_NAME)
        sc   = SparkContext(conf=conf)

        # Execute Main functionality
        main(sc)


