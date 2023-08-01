import mysql.connector
from mysql.connector import Error
from mysql.connector.pooling import MySQLConnectionPool

try:
    # Define your database configurations as a Python dictionary
    dbconfig = {
        "database": "little_lemon_db",
        "user": "root",
        "password": "",
        #"host": "your_host",
        #"port": "your_port"  # If using a non-default port, include this line, otherwise omit it
    }

    # Create a connection pool with two connections
    pool_b = MySQLConnectionPool(pool_name="pool_b", pool_size=2, **dbconfig)

    # Get connections from the pool
    connection1 = pool_b.get_connection()
    connection2 = pool_b.get_connection()

    # Insert data for Guest 1
    query_guest1 = "INSERT INTO Bookings (TableNo, GuestFirstName, GuestLastName, BookingSlot, EmployeeID) VALUES (%s, %s, %s, %s, %s)"
    data_guest1 = (8, 'Anees', 'Java', '18:00', 6)
    cursor1 = connection1.cursor()
    cursor1.execute(query_guest1, data_guest1)
    connection1.commit()

    # Insert data for Guest 2
    query_guest2 = "INSERT INTO Bookings (TableNo, GuestFirstName, GuestLastName, BookingSlot, EmployeeID) VALUES (%s, %s, %s, %s, %s)"
    data_guest2 = (5, 'Bald', 'Vin', '19:00', 6)
    cursor2 = connection2.cursor()
    cursor2.execute(query_guest2, data_guest2)
    connection2.commit()

    # Get a third connection from the pool
    try:
        connection3 = pool_b.get_connection()

        # Insert data for Guest 3
        query_guest3 = "INSERT INTO Bookings (TableNo, GuestFirstName, GuestLastName, BookingSlot, EmployeeID) VALUES (%s, %s, %s, %s, %s)"
        data_guest3 = (12, 'Jay', 'Kon', '19:30', 6)
        cursor3 = connection3.cursor()
        cursor3.execute(query_guest3, data_guest3)
        connection3.commit()

        # Return all connections to the pool
        cursor1.close()
        cursor2.close()
        cursor3.close()
        connection1.close()
        connection2.close()
        connection3.close()

    except mysql.connector.errors.PoolError as pool_error:
        print("PoolError:", pool_error)

except Error as err:
    print("Error:", err)
