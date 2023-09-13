# db_operations.py
import mysql.connector

def get_db_connection(host_b, userd_db, password_db, db_name):
    """
    Create and return a MySQL database connection.

     Args:
        host_db (str): host name of the MySQL database server.
        user_db (str): username to authenticate with MySQL server.
        password_db (str): password to authenticate with MySQL server.
        db_name (str): name of the database.

    Returns:
        MySQL connection object
    """
    try:
        db_connection = mysql.connector.connect(
            host= host_b,
            user= userd_db,
            password= password_db,
            database= db_name
        )
        return db_connection
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
        return None

def close_db_connection(db_connection):
    """
    Close the MySQL database connection.

    Args:
        db_connection: MySQL connection object

    Returns:
        None
    """
    if db_connection:
        db_connection.close()
