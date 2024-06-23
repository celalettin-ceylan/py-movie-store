from peewee import PostgresqlDatabase

db = PostgresqlDatabase("pymoviestore", user="cc", password="12345", host="localhost", port=5432)
db.connect()