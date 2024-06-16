SELECT 
	concat(address, ' ', apartments.address_2) AS apartment_address,
	booked_for as nights
FROM
	apartments
JOIN
	bookings
USING (booking_id)
ORDER BY
 apartments.apartment_id;