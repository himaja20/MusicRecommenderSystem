import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

f = open('/home/mk5376/MusicRecommenderSystem/code/featureSet')
linesInFile = f.readlines()

pitch = []
timbre = []
val = linesInFile[1].split(',')
for i in range(0, 12):
	pitch.append(val[i])
        timbre.append(val[i+12])
print pitch
print timbre

#radius = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
#area = [3.14159, 12.56636, 28.27431, 50.26544, 78.53975, 113.09724]
plt.plot(pitch, timbre)
        #plt.xlabel('Pitch')
        #plt.ylabel('Timbre')
#       plt.title('Area of a Circle')
        #plt.show()
plt.savefig('PVST.png')

