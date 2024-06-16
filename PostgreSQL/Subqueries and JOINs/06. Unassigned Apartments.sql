SELECT 
	booking_id,
	apartment_id,
	companion_full_name
FROM
	bookings as b
JOIN
	customers as c
USING 
	(customer_id)
WHERE 
	apartment_id IS NULL;