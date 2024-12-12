import pymysql

# Database connection details
db_config = {
    'host': 'automated-mysql-server-group9.mysql.database.azure.com',
    'user': 'dbroot',
    'password': 'Secret55',
    'database': 'database1',
    'port': 3306  # Make sure to include the correct port if necessary
}

def insert_query(cursor):
    cursor.execute("INSERT INTO ClimateData (location, date, temperature, humidity) VALUES ('Paris', '2023-01-02', 10.0, 75)")
    print("Insert Query Executed Successfully!")

def select_query(cursor):
    cursor.execute("SELECT * FROM ClimateData WHERE temperature > 20")
    results = cursor.fetchall()  # Fetch all results
    for row in results:
        print(row)

def update_query(cursor):
    cursor.execute("UPDATE ClimateData SET humidity = 60 WHERE location = 'Toronto'")
    print("Update Query Executed Successfully!")

def main():
    # Create the connection and cursor once, and pass the cursor to each query
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            insert_query(cursor)
            select_query(cursor)
            update_query(cursor)
            connection.commit()  # Save any changes after the queries
    finally:
        connection.close()  # Always close the connection

if __name__ == "__main__":
    main()
