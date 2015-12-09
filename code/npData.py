import os
import glob
import sys
import hdf5_getters as get
import numpy as np

ordering = ['trackId', 'loudness', 'segmentsStartArr', 'segmentsPitchesArr', 'segmentsTimbreArr', 'songId', 'title']

#iterate over the array - key
#get the value corresponding to the key
# write dict[key] to file followed by \t
 
featureSet = np.empty([10000,25])
def get_all_data(dir,ext,outDir):
	songsDict = {}
	i = 0
  	for root, dirs, files in os.walk(dir):
		files = glob.glob(os.path.join(root,'*'+ext))
        	for f in files:
			h5 = get.open_h5_file_read(f)
			songId = get.get_song_id(h5)
			pitchAr = (np.array(get.get_segments_pitches(h5))).mean(axis=0)
			timbreAr = (np.array(get.get_segments_pitches(h5))).mean(axis=0)
			loudness = get.get_loudness(h5)
			concatenatedArr = np.append([pitchAr,timbreAr],loudness)
			
			featureSet[i] = concatenatedArr
			songsDict[songId] = featureSet[i]
			print i
			i += 1
			h5.close()

	with open(outDir, "a") as f:
		for key in songsDict.keys():
			f.write("{0}|{1}".format(key,songsDict[key]))
			f.write("\n")

	#np.savetxt(outputDirPath,featureSet,delimiter = ',')

if __name__ == "__main__":
	inputDirPath = sys.argv[1]
	outputDirPath = sys.argv[2]
	print (inputDirPath + "   " + outputDirPath)
	get_all_data(inputDirPath, '.h5', outputDirPath)

#
