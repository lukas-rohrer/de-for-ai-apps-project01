#### Purpose of this database
JSON logs and JSON metadata of a music streaming app is given. A database schema and ETL pipeline is created to enable song play analysis.

#### How to run the Python scripts
1. Run create_tables.py
2. Run etl.py

#### Explanation of the files in the repository
- create_tables.py: creates a cursor and connection to the database, then drops all tables and creates them again.
- etl.ipynb: notebook for preliminary tests of the etl pipeline
- etl.py: executably file to perfor ETL on the whole dataset
- sql_queries.py: collection of queries that get imported in the other files
- test_queries.pgsql: query to check if the results are correct
- test.ipynb: given notebook to run several checks

#### Database schema and ETL pipeline
A star schema is used. 
- Dimension tables: users, songs, artist, time
- Fact tables: songplays

The metadata is processed first to fill the dimension tables. Afterwards the log data is processed.
