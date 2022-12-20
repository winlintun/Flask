import sqlite3


conn = sqlite3.connect('database.db');

print('Database is successfully connected.')

conn.execute('CREATE TABLE students (name TEXT , addr TEXT, city TEXT, pin TEXT)');
print('Tabable cretaed successfully')

conn.close()