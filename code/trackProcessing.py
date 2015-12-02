import os
import glob
import hdf5_getters as get
import numpy as np

def get_all_data(dir,ext):
    for root, dirs, files in os.walk(dir):
	files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
		h5 = get.open_h5_file_read(f)
		keys = {}
		keys['analysisSampleRate'] = get.get_analysis_sample_rate(h5)
		keys['artistMbId'] = get.get_artist_mbid(h5)
		keys['artistName'] = get.get_artist_name(h5)
		keys['artistPlayMeId'] = get.get_artist_playmeid(h5)
		keys['audioMd5'] = get.get_audio_md5(h5)
		keys['danceability'] = get.get_danceability(h5)
		keys['duration'] = get.get_duration(h5)
		keys['energy'] = get.get_energy(h5)
		keys['key'] = get.get_key(h5)
		keys['keyConfidence'] = get.get_key_confidence(h5)
		keys['loudness'] = get.get_loudness(h5)
		keys['mode'] = get.get_mode(h5)
		keys['modeConfidence'] = get.get_mode_confidence(h5)
		keys['release'] = get.get_release(h5)
		keys['release7DigitalId'] = get.get_release_7digitalid(h5)
	
		#Segments data begin
		keys['segmentsConfidenceArr'] = get.get_segments_confidence(h5) #
		#keys['segmentsLoudnessMaxArr'] 
		#print  get.get_segments_loudness_max_time(h5) #
		keys['segmentsLoudnessMaxTimeArr'] = get.get_segments_loudness_max_time(h5) #
		keys['segmentsLoudnessStartArr'] = get.get_segments_loudness_start(h5) #
		keys['segmentsPitchesArr'] = get.get_segments_pitches(h5) #
		keys['segmentsStartArr'] = get.get_segments_start(h5) #
#		keys['segmentsTimbreArr'] =
		#print np.array(get.get_segments_timbre(h5)) #Timbre data	
		#Segments data End
	
		keys['songHotness'] = get.get_song_hotttnesss(h5)
		keys['songId'] = get.get_song_id(h5)	
		keys['startOfFadeOut'] = get.get_start_of_fade_out(h5)
		keys['endofFadeIn'] = get.get_end_of_fade_in(h5)
		keys['tempo'] = get.get_tempo(h5)
		keys['timeSignature'] = get.get_time_signature(h5)
		keys['timeSignatureConfidence'] = get.get_time_signature_confidence(h5)
		keys['title'] = get.get_title(h5)
		keys['track7DigitalId'] = get.get_track_7digitalid(h5)
		keys['trackId'] = get.get_track_id(h5)
		keys['year'] = get.get_year(h5)
            	
		
		#artistMbTags = get.get_artist_mbtags(h5) # arrayi
		#print artistMbTags
		#keys['artistMbTags'] = arrToStr(artistMbTags)
		
		"""keys['tatumsStart'] = get.get_tatums_start(h5) #
		keys['tatumsConfidence'] = get.get_tatums_confidence(h5) #
		keys['similarArtists'] = get.get_similar_artists(h5) #	"""
		#keys['sectionsStartArr']=
		stri = ''
		for str in  get.get_sections_start(h5):
			stri += str(str)+','
		print stri
		"""
		keys['sectionsConfidenceArr'] = get.get_sections_confidence(h5) #
		keys['beatsStart']= get.get_beats_start(h5) #
		keys['beatsConfidence'] = get.get_beats_confidence(h5) #
		keys['barsStart'] = get.get_bars_start(h5) #
		keys['barsConfidence'] = get.get_bars_confidence(h5) #
		keys['artistTermsWeightArr'] = get.get_artist_terms_weight(h5) #array
		keys['artistTermsFreqArr'] = get.get_artist_terms_freq(h5)  #array
		keys['artistTermsArr'] = get.get_artist_terms(h5) # array"""

		h5.close()

"""		i = 1
		s1 = ""
		s2 = ""
		for d in keys:
			s1 += "{i}|"
			s2 += keys[d]
		
		print s1
		print s2		
"""


"""
def arrToStr(inputArr):
	retStr = ''
	for i in inputArr:
		retStr += inputArr[i]
		if (i != 0):
			retStr += ','
	return retStr	
"""			
				

if __name__ == "__main__":
	get_all_data("../data/MillionSongSubset/data/A/A/A", '.h5')

#print get.get_song_id(h5)
