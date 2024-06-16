CREATE TABLE
	bookings_calculation
AS
SELECT
	booked_for,
	CAST(bookings.booked_for * 50 AS NUMERIC) as multiplication,
	
	CAST(bookings.booked_for % 50 AS NUMERIC) as modulo
				
FROM
	bookings
WHERE
	apartment_id = 93;