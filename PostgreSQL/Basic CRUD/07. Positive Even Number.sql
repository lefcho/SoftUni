SELECT
	concat(number, ' ', street) AS address,
	city_id
FROM
	addresses
WHERE
	city_id > 0 and city_id % 2 = 0
ORDER by city_id;