from peewee import PostgresqlDatabase


user = 'root'
password = 'root'
db_name = 'postgresql_database'

db = PostgresqlDatabase(
    db_name, user=user,
    password=password,
    host='localhost'
)
