import sqlite3
conn = sqlite3.connect('schedule_group.sql')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISIS groups (id int auto_increment primary key, groups_id varchar(50) ')