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
		
		keys['trackId'] = get.get_track_id(h5)
		keys['analysisSampleRate'] = get.get_analysis_sample_rate(h5)

		keys['artistMbTags'] = arrToStr(get.get_artist_mbtags(h5))
		keys['artistMbId'] = get.get_artist_mbid(h5)
		keys['artistName'] = get.get_artist_name(h5)
		keys['artistPlayMeId'] = get.get_artist_playmeid(h5)
		
		keys['artistTermsWeightArr'] = arrToStr(get.get_artist_terms_weight(h5)) #array
                keys['artistTermsFreqArr'] = arrToStr(get.get_artist_terms_freq(h5))  #array
                keys['artistTermsArr'] = arrToStr(get.get_artist_terms(h5)) # array"""

		keys['audioMd5'] = get.get_audio_md5(h5)
		
                keys['barsConfidence'] = arrToStr(get.get_bars_confidence(h5)) #
		keys['barsStart'] = arrToStr(get.get_bars_start(h5)) #

		keys['beatsConfidence'] = arrToStr(get.get_beats_confidence(h5)) #
		keys['beatsStart']= arrToStr(get.get_beats_start(h5)) #

		keys['danceability'] = get.get_danceability(h5)
		keys['duration'] = get.get_duration(h5)
		keys['endofFadeIn'] = get.get_end_of_fade_in(h5)
		keys['energy'] = get.get_energy(h5)
		keys['key'] = get.get_key(h5)
		keys['loudness'] = get.get_loudness(h5)
		keys['keyConfidence'] = get.get_key_confidence(h5)
		keys['mode'] = get.get_mode(h5)
		keys['release'] = get.get_release(h5)
		keys['release7DigitalId'] = get.get_release_7digitalid(h5)
		keys['modeConfidence'] = get.get_mode_confidence(h5)

		keys['sectionsConfidenceArr'] = arrToStr(get.get_sections_confidence(h5)) #
		keys['sectionsStartArr'] = arrToStr(get.get_sections_start(h5))
	
		#Segments data begin
		keys['segmentsStartArr'] = arrToStr(get.get_segments_start(h5)) #
		keys['segmentsConfidenceArr'] = arrToStr(get.get_segments_confidence(h5)) #
		keys['segmentsLoudnessMaxArr'] = arrToStr(get.get_segments_loudness_max_time(h5)) #
		keys['segmentsLoudnessMaxTimeArr'] = arrToStr(get.get_segments_loudness_max_time(h5)) #
		keys['segmentsLoudnessStartArr'] = arrToStr(get.get_segments_loudness_start(h5)) #
		keys['segmentsPitchesArr'] = arrToStr(np.array(get.get_segments_pitches(h5).flatten())) #
		keys['segmentsTimbreArr'] = arrToStr(np.array(get.get_segments_timbre(h5).flatten())) #Timbre data	
		#Segments data End
		keys['similarArtists'] = arrToStr(get.get_similar_artists(h5))	
		keys['songHotness'] = get.get_song_hotttnesss(h5)
		keys['songId'] = get.get_song_id(h5)	
		keys['startOfFadeOut'] = get.get_start_of_fade_out(h5)
                keys['tatumsConfidence'] = arrToStr(get.get_tatums_confidence(h5)) #
		keys['tatumsStart'] = arrToStr(get.get_tatums_start(h5)) #
		keys['tempo'] = get.get_tempo(h5)
		keys['timeSignature'] = get.get_time_signature(h5)
                keys['timeSignatureConfidence'] = get.get_time_signature_confidence(h5)
                keys['title'] = get.get_title(h5)
                keys['track7DigitalId'] = get.get_track_7digitalid(h5)
                keys['year'] = get.get_year(h5)
	
            	
		

		with open('sData2', 'a') as f:
			for key in keys.keys():
				f.write('{0}\t'.format(keys[key]))
			f.write('\n')
		"""
		for key in keys:
			print key 
			print "--->  " 
			print keys[key]
		"""
		h5.close()

def arrToStr(inputArr):
	retStr = ''
	for him in inputArr:		
		if (him != inputArr[len(inputArr) - 1]):
			retStr += str(him)+","
			continue
		else:
			retStr += str(him)
	return retStr

if __name__ == "__main__":
	get_all_data("../data/MillionSongSubset/data/A/A/A", '.h5')

#print get.get_song_id(h5)
