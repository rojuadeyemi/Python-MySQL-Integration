import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd

# CREATE A CONNECTION TO MYSQL SERVER OR DATABASE
def create_server_conn(hostname, user_name, password, database=None):
    """
    Establish a connection to the MySQL server or a specific database.

    :param hostname: MySQL server hostname
    :param user_name: MySQL username
    :param password: MySQL password
    :param database: Name of the database (optional)
    :return: MySQL connection object or None if connection failed
    """
    connection = None
    try:
        connection = mysql.connect(
            host=hostname,
            user=user_name,
            passwd=password,
            database=database
        )
        if database:
            print(f"MySQL Database connection to '{database}' established successfully\n\n")
        else:
            print("MySQL server connection established successfully\n\n")
    except Error as err:
        print(f"Error: {err}")
    return connection

def create_db(connection, name):
    """
    Create a new MySQL database.

    :param connection: MySQL connection object
    :param name: Name of the database to create
    """
    
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE {name}")
        print(f"Database '{name}' created successfully")
    except Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def execute_query(connection, query):
    """
    Execute a SQL query on the MySQL server.

    :param connection: MySQL connection object
    :param query: SQL query to execute
    """
    
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as err:
        print(f"Error: {err}")
        execute_query(connection, query)
    finally:
        cursor.close()

def import_csv(connection, sql, csv_path):
    """
    Import data from a pandas DataFrame into a MySQL table.

    :param connection: MySQL connection object
    :param sql: SQL INSERT query to execute
    :param csv_path: path containing the data to import
    """
    
    try:
        cursor = connection.cursor()
        print("Importing CSV data into database...")
        pd.read_csv(csv_path)
        dataframe=data_tuples = [tuple(row) for row in dataframe.itertuples(index=False, name=None)]
        cursor.executemany(sql, data_tuples)  # Use `executemany` for batch insertion
        connection.commit()
        print(f"Successfully imported {cursor.rowcount} rows")
    except Error as err:
        connection.rollback()
        print(f"Error during CSV import: {err}")
    finally:
        cursor.close()