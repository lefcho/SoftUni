SELECT
	CONCAT(a.id, ' ', a.username) as id_username,
	email
FROM
	accounts AS a
JOIN
	accounts_photos AS ap
ON
	a.id = ap.account_id
WHERE
	ap.account_id = ap.photo_id
ORDER BY
	a.id
	;
