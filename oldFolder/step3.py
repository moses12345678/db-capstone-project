import mysql.connector
from mysql.connector import Error

try:
    # Step one: Write a SQL CREATE PROCEDURE query for GuestStatus
    dbconfig = {"database": "little_lemon_db", "user": "root", "password": ""}
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()

    # Set multi=True to allow executing multiple statements
    cursor.execute("SET @@SQL_SAFE_UPDATES = 0;", multi=True)

    create_procedure_query = """
    CREATE PROCEDURE GuestStatus()
    BEGIN
        SELECT CONCAT(GuestFirstName , ' ', GuestLastName) AS GuestName,
        CASE
            WHEN Role IN ('Manager', 'Assistant Manager') THEN 'Ready to pay'
            WHEN Role = 'Head Chef' THEN 'Ready to serve'
            WHEN Role = 'Assistant Chef' THEN 'Preparing Order'
            WHEN Role = 'Head Waiter' THEN 'Order served'
            ELSE 'Unknown'
        END AS OrderStatus
        FROM Bookings
        LEFT JOIN Employees ON Bookings.EmployeeID = Employees.EmployeeID;
    END
    """

    cursor.execute(create_procedure_query, multi=True)

    # Step two: Run the stored procedure query by invoking execute module on the cursor.
    cursor.execute("CALL GuestStatus()")

    # Step three: Invoke callproc to call the stored procedure.
    # cursor.callproc("GuestStatus")

    # Step four: Fetch the results in a variable called dataset.
    dataset = cursor.fetchall()

    # Step five: Extract the names of the columns.
    column_names = [desc[0] for desc in cursor.description]

    # Step six: Print the names of the columns.
    print("Column Names:", column_names)

    # Step seven: Print the sorted data using for loop.
    for row in dataset:
        print(row)

    # Step eight: Close the connection to return it back to the pool.
    cursor.close()
    connection.close()

except Error as e:
    print("Error while connecting to MySQL:", e)

