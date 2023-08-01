import mysql.connector
from mysql.connector import Error
from mysql.connector.pooling import MySQLConnectionPool

try:
    # Define your database configurations as a Python dictionary
    dbconfig = {
        "database": "little_lemon_db",
        "user": "root",
        "password": "",
       
    }

    # Create a connection pool with two connections
    pool_b = MySQLConnectionPool(pool_name="pool_b", pool_size=2, **dbconfig)

    # Test the connections in the pool
    connection1 = pool_b.get_connection()
    connection2 = pool_b.get_connection()

    # Close the connections after testing
    connection1.close()
    connection2.close()

    print("Connection pool 'pool_b' has been established successfully.")

except Error as err:
    print("Error:", err)
