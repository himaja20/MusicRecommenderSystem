#!/bin/bash
#PBS -l walltime=30:00
#PBS -l nodes=1:ppn=1
#PBS -l mem=4gb
#PBS -t 1-2
#PBS -M mk5376@nyu.edu
#PBS -N process_data

if [ "$PBS_ARRAYID" == "" ]; then exit; fi

RUNDIR=/scratch/mk5376/music-recommender-system/songData/data
dirs=(A B)
#dirs=(C  D  F  G  I  J  K  L  M  N  Q  R  T  Z)
SCRIPTDIR=/home/mk5376/MusicRecommenderSystem/code
#DATADIR=/scratch/mk5376/music-recommender-system/songData/data/${dirs[$PBS_ARRAYID]}
OUTFILE=/home/mk5376/MusicRecommenderSystem/code/sDataFiles/file-${dirs[$PBS_ARRAYID]}
DATADIR=/home/mk5376/MillionSongSubset/data/${dirs[$PBS_ARRAYID]}
python ${SCRIPTDIR}/trackProcessing.py ${DATADIR} ${OUTFILE}
exit

