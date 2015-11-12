
Progress from last week - 

Set up the development environment in HPC and loaded data into HIVE

	. All packages required for processing Million song dataset and User Taste Profile data set were not available on HPC
	. Worked on setting virtual environment in HPC to set up and install required packages in HPC.
	. Established virtual environment for my Project folder using "virtualenv" 
	. Loaded the following modules - 
		. libhdf5 library
		. python tables
		. numpy
	. All the code is working fine now in HPC.
	. Working on gathering data from pyechonest API. 

Work in Progress - 

	. Have to run the userToMsd.py on all the ~4 million users to collate information on User-Song related information
	. Process the json and dump the data into the database.

 		
