
import hdf5_getters
h5 = hdf5_getters.open_h5_file_read("../data/MillionSongSubset/data/A/A/A/TRAAAEF128F4273421.h5")
pitch = hdf5_getters.get_segments_pitches(h5)
print pitch.shape
#print hdf5_getters.get_segments_loudness_start(h5, 0).shape
print pitch[:1]
h5.close()

