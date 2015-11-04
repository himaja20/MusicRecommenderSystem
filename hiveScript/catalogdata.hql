use user_taste_profile;

drop table userCatalog;

create external table userCatalog (userId string, catalogId string)
row format delimited fields terminated by ' '
stored as textfile
location '/user/hr970/catalogData';

describe userCatalog;

-- LOAD data inpath '/user/hr970/catalogData' overwrite into table userCatalog;

select * from userCatalog limit 10;
