# db-capstone-project
Meta database engineer capstone Stalk course

# Install Python Virtual Env
## python -m venv env
# activate this env
## source env/bin/activate

# install requirement file
## pip install -r requirements.txt

# create a  stored procedure to getMaxQuantity

DELIMITER //

CREATE PROCEDURE GetMaxQuantityInOrder()
BEGIN
    SELECT MAX(quantity) AS Max_Quantity_in_Order FROM orders;
END //

DELIMITER ;


# Create a prepared statement GetOrderDetail

DELIMITER //

CREATE PROCEDURE GetOrderDetail(IN customerIdValue INT)
BEGIN
    PREPARE stmt FROM 'SELECT OrderID, Quantity, Cost FROM orders WHERE CustomerID = ?';
    SET @customerId = customerIdValue;
    EXECUTE stmt USING @customerId;
    DEALLOCATE PREPARE stmt;
END //

DELIMITER ;

# Create a stored procedure CancelOrder
DELIMITER //

CREATE PROCEDURE CancelOrder(IN orderIdValue INT)
BEGIN
    DELETE FROM orders WHERE OrderID = orderIdValue;
END //

DELIMITER ;

# Create a Updated booking table
DELIMITER //

CREATE PROCEDURE UpdateBooking()
BEGIN
    SELECT customerID, tableID, BookingSlot FROM Customers;
END //

DELIMITER ;
# Create a Updatebooking
DELIMITER //

CREATE PROCEDURE UpdateBooking(
    IN table_number INT,
    IN booking_date DATE
)
BEGIN
    UPDATE Bookings
    SET TableNumber = table_number, BookingDate = booking_date
    WHERE BookingID = BookingID;
END //

DELIMITER ;

# Create cancel booking procedure
DELIMITER //

CREATE PROCEDURE CancelBooking(
    IN table_number INT
)
BEGIN
    DELETE FROM Bookings
    WHERE TableNumber = table_number;
END //

DELIMITER ;
