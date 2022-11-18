### Server for math operations on users

Server provides API to get data from another server and make math operations on it: calculate median of users age, 
count amount of unique users names, filter users records by age range. Endpoints for this functional:
- **/median**
- **/unique_names_histogram**
- **/age_range?frm={int}&to={int}** - query parameter ***frm** - left border of age range, ***to*** right border.

All requirements of project in **requirements.txt**. To launch servers locally:
1. Clone repo 
2. Run from directory with files
```
python3 main.py
python3 math_operations_server.py
```
Commands launch two servers: one for providing crud-operations on users records, second - provides API for math operations.
CRUD-server by default works with **data.jsonl**-file, lies in the same directory. Math API server by default starts on ***http://127.0.0.1:8766***.