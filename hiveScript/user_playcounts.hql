use user_taste_profile;

drop table userplaycounts;

create external table userplaycounts (userId string, songId string, playcount int)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
stored as textfile
location '/user/hr970/projData';

describe userplaycounts;


select * from userplaycounts limit 10;
