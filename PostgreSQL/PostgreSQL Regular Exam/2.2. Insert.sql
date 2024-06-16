INSERT INTO addresses(street, town, country, account_id)
SELECT
	a.username,
	a."password",
	a.ip,
	a.age
FROM
	accounts As a
WHERE
	a.gender = 'F'
;