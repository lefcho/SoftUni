CREATE OR REPLACE FUNCTION udf_accounts_photos_count(
	account_username VARCHAR(30)
) RETURNS INT
AS
$$
DECLARE
	ph_count INT;
BEGIN
	ph_count := (
	SELECT
		COUNT(*)
	FROM
		accounts as a
	JOIN
		accounts_photos as ac
	ON
		ac.account_id = a.id
	WHERE
		a.username = account_username
	GROUP BY 
		a.id);

	IF ph_count IS NULL THEN
		ph_count = 0;
	END IF;
	RETURN ph_count;
END;
$$
LANGUAGE plpgsql;