# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE songplays(songplay_id serial PRIMARY KEY, start_time varchar NOT NULL, user_id int NOT NULL, level varchar, song_id varchar, artist_id varchar, session_id int NOT NULL, location varchar, user_agent text);
""")

user_table_create = ("""CREATE TABLE users(user_id varchar PRIMARY KEY, first_name varchar NOT NULL, last_name varchar, gender varchar, level varchar);
""")

song_table_create = ("""CREATE TABLE songs(song_id varchar PRIMARY KEY, title VARCHAR NOT NULL, artist_id VARCHAR NOT NULL, year varchar, duration FLOAT);
""")

artist_table_create = ("""CREATE TABLE artists(artist_id varchar PRIMARY KEY, name varchar NOT NULL, location varchar, latitude varchar, longitude varchar);
""")

time_table_create = ("""CREATE TABLE time(start_time varchar primary key, hour int NOT NULL, day int NOT NULL, week int NOT NULL, month int NOT NULL, year int NOT NULL, weekday int NOT NULL)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays(start_time,user_id,level,song_id,artist_id,session_id,location,user_agent) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""INSERT INTO users(user_id,first_name,last_name,gender,level) values(%s,%s,%s,%s,%s)
ON CONFLICT(user_id) DO UPDATE SET first_name=excluded.first_name,last_name=excluded.last_name,gender=excluded.gender,level=excluded.level;
""")

song_table_insert = ("""INSERT INTO songs(song_id,title,artist_id,year,duration) VALUES(%s,%s,%s,%s,%s) ON CONFLICT(song_id) DO UPDATE SET title=excluded.title,artist_id=excluded.artist_id,year=excluded.year,duration=excluded.duration;
""")

artist_table_insert = ("""INSERT INTO artists(artist_id,name,location,latitude,longitude) VALUES(%s,%s,%s,%s,%s) ON CONFLICT(artist_id) DO UPDATE SET name=excluded.name , location=excluded.location,latitude=excluded.latitude,longitude=excluded.longitude;
""")


time_table_insert = ("""INSERT INTO time(start_time,hour,day,week,month,year,weekday) VALUES(%s,%s,%s,%s,%s,%s,%s) ON CONFLICT(start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""SELECT song_id,songs.artist_id 
FROM artists
INNER JOIN songs ON songs.artist_id = artists.artist_id
WHERE songs.title = %s AND artists.name = %s AND duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
