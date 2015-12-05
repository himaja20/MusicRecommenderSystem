
import sys
import pprint

def process_tracks():
	f = open('../data/processedSongData/out')
	linesInFile = f.readlines()
	for i in range(len(linesInFile)):
		load_track(linesInFile[i])

def load_track(line):	
	t = {}
	f = line.split('\t')
	seg_start = f[2].split(',')
	seg_pitches = f[3].split(',')
	seg_timbre = f[4].split(',')
	track_id = f[0]
	COF_COUNT = 12
	numOfSegments = len(seg_start)
	sumPitch = [0 for s1 in range(12)]
	sumTimbre = [0 for s2 in range(12)]
	avgTimbre = [0 for a1 in range(12)]
	avgPitch = [0 for a2 in range(12)]
	for i in range(0,numOfSegments):
		seg = {}
		seg['pitch'] = [float(p) for p in seg_pitches[i * COF_COUNT: i * COF_COUNT + COF_COUNT]]
		seg['timbre'] = [float(p) for p in seg_timbre[i * COF_COUNT: i * COF_COUNT + COF_COUNT]]
		for k in range(0, 12):
			sumPitch[k] = (sumPitch[k] + seg['pitch'][k])
			sumTimbre[k] = (sumTimbre[k] + seg['timbre'][k])
	for av in range(0, 12):
		avgPitch[av] = sumPitch[av]/numOfSegments
		avgTimbre[av] = sumTimbre[av]/numOfSegments	
	avgStrPitch = ''
	avgStrTimbre = ''
	i = 0
	for av in range(len(avgPitch)):
		if (i <= 10):
			print i
			avgStrPitch += str(avgPitch[av]) + ","
			avgStrTimbre += str(avgTimbre[av]) + ","
		else:
			avgStrPitch += str(avgPitch[av])
			avgStrTimbre += str(avgTimbre[av])
		i = i + 1
	with open("pitchAvg",'a') as f1:
		f1.write('{0},{1}'.format(track_id,avgStrPitch))
       		f1.write('\n')
	with open("timbreAvg",'a') as f2:
		f2.write('{0},{1}'.format(track_id,avgStrTimbre))
		f2.write('\n')

if __name__ == '__main__':
    process_tracks()
