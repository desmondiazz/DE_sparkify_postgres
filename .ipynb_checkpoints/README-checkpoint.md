This Project extracts logs/songs data from a popular music steaming app sparkify. Then the data is transformed to store in the respective tables to perform further analysis.

### Contents
    * [create_tables.py] - When executed , this files connects to a default studentdb , than drops an existing sparkifydb if exists , and creates a new sparkifydb , with required tables.
    * [etl.ipynb] - used to run python code for storing data in sparkifydb using jupyter notebook
    * [etl.py] - used to run python code for storing data in sparkifydb using the terminal
    * [sql_queries.py] - contains set of sql  for creating tables and insert statements needed in create_tables.py ,  etl.py
    * [test.ipynb] - contains sql's to validat the data that has been stored in the sparkifydb.

### To Run this project

```sh
$ python create_tables.py
$ python etl.py
$ run test.ipynb
```