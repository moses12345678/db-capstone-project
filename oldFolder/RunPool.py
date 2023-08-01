import mysql.connector

# Step three: Invoke callproc to call the stored procedure.

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

    # Step two: Run the stored procedure query by invoking execute module on the cursor.
    #cursor.execute("CREATE PROCEDURE PeakHours() BEGIN SELECT HOUR(BookingSlot) AS Hour, COUNT(*) AS Bookings FROM Bookings GROUP BY Hour ORDER BY Bookings DESC; END;")

    # Step three: Invoke callproc to call the stored procedure.
    cursor.callproc("PeakHours")

    # Step four: Fetch the results in a variable called dataset.
    dataset = cursor.stored_results()

        # Step four: Fetch the results in a variable called dataset.
    dataset = list(cursor.stored_results())[0]

    # Step five: Extract the names of the columns.
    columns = [desc[0] for desc in dataset.description]

    # Step six: Print the names of the columns.
    print("Column names:", columns)

    # Step seven: Print the sorted data using a for loop.
    for row in dataset.fetchall():
        print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print("Error:", err)







