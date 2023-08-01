import mysql.connector
from mysql.connector import pooling

try:
    # Step one: Import MySQLConnectionPool

    # Step two: Import Error

    # Step three: Create a pool named pool_a with two connections.
    # Use a try-except block to handle any possible errors.

    # Database configurations
    dbconfig = {
        "database": "little_lemon_db",
        "user": "root",
        "password": ""
    }

    # Create the connection pool with two connections
    pool_a = pooling.MySQLConnectionPool(pool_name="pool_a", pool_size=2, **dbconfig)

    # Step four: Obtain a connection from pool_a and create a cursor object to communicate with the database.
    connection = pool_a.get_connection()
    cursor = connection.cursor()

    # Example query (replace with your actual SQL query)
    query = "SELECT * FROM Employees"
    cursor.execute(query)

    # Fetch and print the results (replace with your desired data processing)
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and release the connection back to the pool
    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print("Error:", err)

