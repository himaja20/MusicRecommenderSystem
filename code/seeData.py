import hdf5_getters as get
h5 = get.open_h5_file_read('../data/MillionSongSubset/data/A/A/A')
timbre = get.get_segments_timbre(h5,0)
timbre.shape()
print timbre[:1]
