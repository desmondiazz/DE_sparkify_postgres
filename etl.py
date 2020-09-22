import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
        -Takes a db cur and filepath as perameters where filepath is the location of the json file containing the   song data , this data is then processed and stored in songs/artists table
    """
    
    df = pd.read_json(filepath,typ='series')

    song_data = df[['song_id','title','artist_id','year','duration']]
    song_data = song_data.values.tolist()
    cur.execute(song_table_insert, song_data)
    
    artist_data = df[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']]
    artist_data = artist_data.values.tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
        -Takes a db cur and filepath as perameters where filepath is the location of the json file containing the songplays log data , this data is then processed to extract detailed time , song details , artist details. And formated to store the data in songplays and time table.
    """
    
    df = pd.read_json(filepath,lines=True)
    df = df[df['page']=='NextSong']
    t = pd.DataFrame({'start_time':df.ts,'timestamp':pd.to_datetime(df.ts,unit='ms')})
    time_data = pd.DataFrame({'start_time':t.start_time,'hour':t.timestamp.dt.hour,'day':t.timestamp.dt.day,'week':t.timestamp.dt.week, 'month':t.timestamp.dt.month, 'year':t.timestamp.dt.year, 'weekday':t.timestamp.dt.weekday})
    column_labels = ['start_time','hour','week','month','year','weekday']
    time_df = time_data

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    user_df = df[['userId','firstName','lastName','gender','level']]
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    for index, row in df.iterrows():
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        songplay_data = [row.ts,row.userId,row.level,songid,artistid,row.sessionId,row.location,row.userAgent]
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
        -Takes db cur and conn as perameters , along with filepath to get list of songs/log data locations , and also requires a callback function that takes db cursor and a file location as perameters.
    """
    
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
        -The main entry point of the project , which connects to the db and calls the process_data functions to process log/songs data.
    """
    
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()