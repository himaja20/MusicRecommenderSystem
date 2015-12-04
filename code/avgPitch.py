import sys
import pprint

def process_tracks():
	f = open('/home/mk5376/workspace/sample1')
	linesInFile = f.readlines()
	for i in range(len(linesInFile)):
		load_track(linesInFile[i])

def load_track(line):	
	t = {}
	f = line.split('\t')
	seg_pitches = f[32].split(',')
	track_id = f[0]
	PITCH_COUNT = 12
	numOfSegments = len(seg_pitches)/PITCH_COUNT#len(seg_start)
	print("track_id", track_id, " se_pitches ", len(seg_pitches), " number of segments is ", numOfSegments)
	count = 0
	sum = [0 for s in range(12)]
	avg = [0 for a in range(12)]
	for i in range(0,numOfSegments):
		seg = {}
		segs{}
		segs['pitch'] = for p in seg_pitches[i * PITCH_COUNT: i * PITCH_COUNT + PITCH_COUNT]
		seg['pitch'] = [float(p) for p in seg_pitches[i * PITCH_COUNT: i * PITCH_COUNT + PITCH_COUNT]]
		
		for k in range(0, 12):
			sum[k] = (sum[k] + seg['pitch'][k])

	for av in range(0, 12):
		avg[av] = sum[av]/numOfSegments	
	with open("pitchAvg",'a') as f:
        	for av in range(len(avg)):
			f.write('{0},{1}'.format(track_id,avg[av]))
        	f.write('\n')
	
	
if __name__ == '__main__':
    process_tracks()
