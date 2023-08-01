import mysql.connector

# Define your database configurations as a Python dictionary
dbconfig = {
    "database": "little_lemon_db",
    "user": "root",
    "password": "",
}

try:
    # Establish a connection
    connection = mysql.connector.connect(**dbconfig)

    # Create a cursor object to communicate with the database
    cursor = connection.cursor()

    # Query 1: The name and EmployeeID of the Little Lemon manager
    cursor.execute("SELECT Name, EmployeeID FROM Employees WHERE Role = 'Manager'")
    manager_info = cursor.fetchone()
    print("Little Lemon Manager:")
    print("Name:", manager_info[0])
    print("EmployeeID:", manager_info[1])
    print()

    # Query 2: The name and role of the employee who receives the highest salary
    cursor.execute("SELECT Name, Role FROM Employees WHERE Annual_Salary = (SELECT MAX(Annual_Salary) FROM Employees)")
    highest_salary_employee = cursor.fetchone()
    print("Employee with the Highest Salary:")
    print("Name:", highest_salary_employee[0])
    print("Role:", highest_salary_employee[1])
    print()

    # Query 3: The number of guests booked between 18:00 and 20:00
    cursor.execute("SELECT COUNT(*) FROM Bookings WHERE TIME(BookingSlot) BETWEEN '18:00' AND '20:00'")
    number_of_guests = cursor.fetchone()[0]
    print("Number of Guests booked between 18:00 and 20:00:", number_of_guests)
    print()

    # Query 4: The full name and BookingID of all guests waiting to be seated with the receptionist
    cursor.execute("SELECT CONCAT(GuestFirstName, ' ', GuestLastName) AS FullName, BookingID FROM Bookings  ORDER BY BookingSlot")
    waiting_guests = cursor.fetchall()
    print("Guests Waiting to be Seated:")
    for guest in waiting_guests:
        print("FullName:", guest[0])
        print("BookingID:", guest[1])
        print()

    # Close the cursor and connection
    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print("Error:", err)
