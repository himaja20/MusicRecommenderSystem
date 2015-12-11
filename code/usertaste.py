import pyen
from pyen import PyenException
en = pyen.Pyen("KO5QUBGMUVJZA0PFA")
k = 0;

for fileNum in range(40,41):
	with open("../data/chunks/file"+str(fileNum)) as catalogIds:
		print "../data/chunks/file"+str(fileNum)
        	for line in catalogIds:
			try:
				catalogId = line.strip()
				uCatalog = en.get('tasteprofile/read', format='json',id=line.strip())
				uCatalogLength = len(uCatalog['catalog']['items'])
				print uCatalogLength
				print "user  " + str(k)
				for i in range(uCatalogLength):
					print "song  " + str(i)
					songId = uCatalog['catalog']['items'][i]['song_id'] if (u'song_id' in uCatalog['catalog']['items'][i].keys()) else None
					songName = uCatalog['catalog']['items'][i]['song_name'] if (u'song_name' in uCatalog['catalog']['items'][i].keys()) else None
					artistName = uCatalog['catalog']['items'][i]['artist_name'] if (u'artist_name' in uCatalog['catalog']['items'][i].keys()) else None
					playCount = uCatalog['catalog']['items'][i]['play_count'] if (u'play_count' in uCatalog['catalog']['items'][i].keys()) else None
					lastModified = uCatalog['catalog']['items'][i]['last_modified'] if (u'last_modified' in uCatalog['catalog']['items'][i].keys()) else None
					dateAdded = uCatalog['catalog']['items'][i]['date_added'] if (u'date_added' in uCatalog['catalog']['items'][i].keys()) else None
					artistId = uCatalog['catalog']['items'][i]['artist_id'] if (u'artist_id' in uCatalog['catalog']['items'][i].keys()) else None
					foreignId = uCatalog['catalog']['items'][i]['foreign_id'] if (u'foreign_id' in uCatalog['catalog']['items'][i].keys()) else None

					"""insertStmt = u"INSERT INTO TABLE extendedUserCatalogInfo VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')".format(songId, songName, artistName, playCount, lastModified, dateAdded, artistId, foreignId)"""
					insertStmt = u"{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}".format(songId, songName, artistName, playCount, lastModified, dateAdded, artistId, foreignId,catalogId)
					with open("insertsDir/insertStmtsFile"+str(fileNum), "a") as myfile:
						myfile.write("\n")
						myfile.write(insertStmt.encode('utf-8'))
				
			except PyenException, p:
				with open("insertsDir/outliers"+str(fileNum), "a") as myfile1:
					myfile1.write("\n")
					myfile1.write(line.strip())
					myfile1.write("\n")
					myfile1.write(p.msg)
					myfile1.write("-----------------")
			finally:
				k = k + 1
				print "--------------"
	
