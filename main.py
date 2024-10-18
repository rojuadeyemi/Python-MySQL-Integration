from mysql.connector import connection
import modules
import re

def get_input(prompt, input_type=str, validation_fn=None, error_msg="Invalid input, try again"):
    """Prompt the user for input with validation."""
    while True:
        try:
            value = input_type(input(prompt).strip())
            if validation_fn and not validation_fn(value):
                raise ValueError()
            return value
        except (ValueError, TypeError):
            print(error_msg)

def is_valid_option(code):
    """Validate that the option is 0, 1, 2, or 3."""
    return bool(re.match(r'^[0123]$', str(code)))

def is_valid_name(name):
    """Validate that the database name is alphanumeric."""
    return bool(re.match(r'^[A-Za-z]+\d*$', name))

def create_db(connect):
    """Create a new database."""
    print(''.rjust(45,"="))
    print("CREATE A DATABASE USING THIS PROGRAM")
    print(''.rjust(45,"="))
    db_name = get_input("Enter your desired database name: ", validation_fn=is_valid_name)
    modules.create_db(connect, db_name)

def query_db(connect, hostname, user_name, password):
    """Query an existing database."""
    print(''.rjust(20,"="))
    print("QUERY A DATABASE")
    print(''.rjust(20,"="))

    db_name = input("Enter the name of the database you want to connect to: ").strip()
    query = input("Enter the SQL query statement here: ").strip()
    connection = modules.create_server_conn(hostname, user_name, password, db_name)
    modules.execute_query(connection, query)

def import_data(connect, hostname, user_name, password):
    """Import CSV data into a database."""
    print(''.rjust(30,"="))
    print("IMPORT CSV INTO TABLE")
    print(''.rjust(30,"="))
    csv_path = input("Enter the CSV file location to be imported: ").strip()
    db_name = input("Enter the database you want to load into: ").strip()
    sql = input("Enter the INSERT statement here: ").strip()
    connection = modules.create_server_conn(hostname, user_name, password, db_name)
    modules.import_csv(connection, sql, csv_path)

def main():

    print(''.rjust(61,"="))
    print("CREATE A CONNECTION TO MYSQL WORKBENCH USING THIS PROGRAM")
    print(''.rjust(61,"="))

    hostname = input("Hostname: ").strip()
    user_name = input("Username: ").strip()
    password = input("Password: ").strip()
    
    # Establish initial connection to the server
    connect = modules.create_server_conn(hostname, user_name, password)
    
    while True:
        option = get_input("""
            Provide Your Option:

            1: Create a Database
            2: Query a Database
            3: Import Data
            0: To exit

            """, input_type=int, validation_fn=is_valid_option)
        
        if option == 1:
            create_db(connect)
        elif option == 2:
            query_db(connect, hostname, user_name, password)
        elif option == 3:
            import_data(connect, hostname, user_name, password)
        elif option == 0:
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()
