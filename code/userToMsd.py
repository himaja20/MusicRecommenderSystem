
from pyechonest import catalog, config
import json

config.ECHO_NEST_API_KEY="KO5QUBGMUVJZA0PFA"

cat = catalog.Catalog('CACNYVZ1332EB0BA9D')
uCatalog = cat.get_item_dicts()

#print(uCatalog)
uCatalogLength = len(uCatalog)

#print( u'play_count' in uCatalog[0].keys())

for i in range(uCatalogLength):
	songId = uCatalog[i][u'song_id'] if (u'song_id' in uCatalog[i].keys()) else None
	songName = uCatalog[i][u'song_name'] if (u'song_name' in uCatalog[i].keys()) else None
	artistName = uCatalog[i][u'artist_name'] if (u'artist_name' in uCatalog[i].keys()) else None
	playCount = uCatalog[i][u'play_count'] if (u'play_count' in uCatalog[i].keys()) else None
	lastModified = uCatalog[i][u'last_modified'] if (u'last_modified' in uCatalog[i].keys()) else None
	dateAdded = uCatalog[i][u'date_added'] if (u'date_added' in uCatalog[i].keys()) else None
	artistId = uCatalog[i][u'artist_id'] if (u'artist_id' in uCatalog[i].keys()) else None
	foreignId = uCatalog[i][u'foreign_id'] if (u'foreign_id' in uCatalog[i].keys()) else None

	#insertStmt = "INSERT INTO TABLE extendedUserCatalogInfo VALUES (" + songId + "," +  songName + "," +  artistName + "," + ' playCount' + "," +  lastModified + ","+ dateAdded + "," +  artistId + "," +  foreignId + ");"
	#insertStmt = u' '.join(insertStmt).encode('utf-8').strip()
	insertStmt = u"INSERT INTO TABLE extendedUserCatalogInfo VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')".format(songId, songName, artistName, playCount, lastModified, dateAdded, artistId, foreignId) # + songId + "," +  songName + "," +  artistName + "," + ' playCount' + "," +  lastModified + ","+ dateAdded + "," +  artistId + "," +  foreignId + ");"
	with open("insertStmtsFile", "a") as myfile:
	   	myfile.write("\n")
		myfile.write(insertStmt.encode('utf-8'))

