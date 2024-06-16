CREATE OR REPLACE PROCEDURE udp_modify_account(
	address_street VARCHAR(30), 
    address_town VARCHAR(30))
AS
$$
BEGIN
	UPDATE
	    accounts AS acc
	SET 
	    job_title = CONCAT('(Remote) ', job_title)
	FROM
	    addresses AS add
	WHERE
	    add.account_id = acc.id
	    	AND 
		add.street = address_street
	    	AND 
		add.town = address_town;
END;
$$
LANGUAGE plpgsql;