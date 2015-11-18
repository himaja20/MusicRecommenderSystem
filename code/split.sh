#!/bin/bash

read -p "Enter the file location > " FILELOC
read -p "enter number of chunks > " CHUNKS
read -p "enter location where to create the new file > " DIR
NUMLINES=$(cat "$FILELOC/catalogIds.tsv" | wc -l)
echo $NUMLINES

CHUNKSIZE=$(($NUMLINES/$CHUNKS))
if [ ! -d $DIR ]; then
{
	mkdir $DIR
}	 
fi
num=$(find $DIR -type f | wc -l)


if [ $num -gt 0 ]; then
{
	rm -r $DIR/*
}
fi

$(split --lines=${CHUNKSIZE} -d "$FILELOC/catalogIds.tsv" "$DIR/file")
