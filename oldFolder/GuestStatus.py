import mysql.connector

try:
    # Database configurations
    dbconfig = {
        "database": "little_lemon_db",
        "user": "root",
        "password": ""
    }

    # Connect to the database
    connection = mysql.connector.connect(**dbconfig)

    # Create a cursor object
    cursor = connection.cursor()

    # Step one: Write a SQL CREATE PROCEDURE query for GuestStatus
    
    cursor.execute("""
        CREATE PROCEDURE GuestStatus()
        BEGIN
            SELECT CONCAT(GuestFirstName, ' ', GuestLastName) AS GuestName,
            CASE
                WHEN Role = 'Manager' OR Role = 'Assistant Manager' THEN 'Ready to pay'
                WHEN Role = 'Head Chef' THEN 'Ready to serve'
                WHEN Role = 'Assistant Chef' THEN 'Preparing Order'
                WHEN Role = 'Head Waiter' THEN 'Order served'
                ELSE 'Unknown Status'
            END AS OrderStatus
            FROM Bookings
            LEFT JOIN Employees ON Bookings.EmployeeID = Employees.EmployeeID;
        END;
    """)
    
    # Step two: Invoke callproc to call the stored procedure.
    cursor.callproc("GuestStatus")

    # Step three: Fetch the results in a variable called dataset.
    dataset = list(cursor.stored_results())[0]

    # Step four: Extract the names of the columns.
    columns = [desc[0] for desc in dataset.description]

    # Step five: Print the names of the columns.
    print("Column names:", columns)

    # Step six: Print the sorted data using a for loop.
    for row in dataset.fetchall():
        print(row)

    # Step seven: Close the cursor and connection to return it back to the pool.
    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print("Error:", err)
