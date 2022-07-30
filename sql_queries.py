# DROP TABLES

songplay_table_drop = """DROP TABLE IF EXISTS songplays"""
user_table_drop = """DROP TABLE IF EXISTS users"""
song_table_drop = """DROP TABLE IF EXISTS songs"""
artist_table_drop = """DROP TABLE IF EXISTS artists"""
time_table_drop = """DROP TABLE IF EXISTS time"""

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(
    songplay_id varchar(255) primary key,
    start_time bigint references time(start_time),
    user_id int references users(user_id),
    level varchar(255),
    song_id varchar(255) references songs(song_id),
    artist_id varchar(255) references artists(artist_id),
    session_id int,
    location varchar(255),
    user_agent text
)
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
    user_id int primary key,
    first_name varchar(255),
    last_name varchar(255),
    gender character (1),
    level varchar(255)
)    
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
    song_id varchar(255) primary key,
    title varchar(255),
    artist_id varchar(255),
    year int,
    duration double precision
)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
    artist_id varchar(255) primary key,
    name varchar(255),
    location varchar(255),
    latitude decimal(8,6),
    longitude decimal(8,6)
)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(
    start_time bigint primary key,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday varchar(255)
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]