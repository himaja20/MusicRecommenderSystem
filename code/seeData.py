#from matplotlib.mlab import PCA
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import hdf5_getters as get
import numpy as np
#./A/A/A/TRAAAVO128F93133D4.h5
h5 = get.open_h5_file_read('../data/MillionSongSubset/data/B/I/I/TRBIIAL128F4252C04.h5')
segStart = get.get_segments_start(h5) 
pitch = np.array(get.get_segments_pitches(h5))
pitch_flatten = pitch.flatten()
#timbrePCA = PCA(timbre)

#timbrePCA.fracs

#print timbrePCA.Y
print pitch.shape
print len(segStart)
print len(pitch_flatten)
#print get.get_song_id(h5)



"""
timbre = get.get_segments_timbre(h5,0)
timbre.shape()
print timbre[:1]"""
