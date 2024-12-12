import mysql.connector
from concurrent.futures import ThreadPoolExecutor

# Database connection details
db_config = {
    'host': 'automated-mysql-server-group9.mysql.database.azure.com',
    'user': 'dbroot',
    'password': 'Secret55',
    'database': 'database1'
}

def insert_query(cursor):
    cursor.execute("INSERT INTO ClimateData (location, date, temperature, humidity) VALUES ('Paris', '2023-01-02', 10.0, 75)")

def select_query(cursor):
    cursor.execute("SELECT * FROM ClimateData WHERE temperature > 20")
    return cursor.fetchall()

def update_query(cursor):
    cursor.execute("UPDATE ClimateData SET humidity = 60 WHERE location = 'Toronto'")

def execute_queries():
    with mysql.connector.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            with ThreadPoolExecutor() as executor:
                futures = [
                    executor.submit(insert_query, cursor),
                    executor.submit(select_query, cursor),
                    executor.submit(update_query, cursor)
                ]
                for future in futures:
                    print(future.result())

if __name__ == "__main__":
    execute_queries()
