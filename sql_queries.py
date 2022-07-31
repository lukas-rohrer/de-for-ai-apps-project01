# DROP TABLES

songplay_table_drop = """DROP TABLE IF EXISTS songplays"""
user_table_drop = """DROP TABLE IF EXISTS users"""
song_table_drop = """DROP TABLE IF EXISTS songs"""
artist_table_drop = """DROP TABLE IF EXISTS artists"""
time_table_drop = """DROP TABLE IF EXISTS time"""

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(
    songplay_id serial primary key,
    start_time timestamp references time(start_time),
    user_id integer references users(user_id),
    level varchar(255),
    song_id varchar(255) references songs(song_id),
    artist_id varchar(255) references artists(artist_id),
    session_id int,
    location varchar(255),
    user_agent text
)
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
    user_id integer primary key,
    first_name varchar(255),
    last_name varchar(255),
    gender character (1),
    level varchar(255)
)    
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
    song_id varchar(255) primary key,
    title varchar(255) NOT NULL,
    artist_id varchar(255),
    year int,
    duration double precision NOT NULL
)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
    artist_id varchar(255) primary key,
    name varchar(255) NOT NULL,
    location varchar(255),
    latitude double precision,
    longitude double precision
)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(
    start_time timestamp primary key,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday varchar(255)
)
""")

# INSERT RECORDS


songplay_table_insert = ("""INSERT INTO songplays (start_time, song_id, artist_id, user_id, level, session_id, location, user_agent) \
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) \
                            VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) \
                            VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) \
                            VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) \
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""SELECT songs.song_id, songs.artist_id FROM artists JOIN songs on artists.artist_id = songs.artist_id \
                    WHERE songs.title = %s AND songs.duration = %s AND artists.name = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create,song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]