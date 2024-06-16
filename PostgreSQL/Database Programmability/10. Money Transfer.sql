CREATE OR REPLACE PROCEDURE sp_transfer_money(
	sender_id INT,
	reciever_id INT,
	money_amount NUMERIC(4)
)
AS
$$
DECLARE
	current_balance NUMERIC;
BEGIN
	
	CALL sp_withdraw_money(sender_id, money_amount);
	CALL sp_deposit_money(reciever_id, money_amount);

	current_balance := (SELECT balance FROM accounts WHERE id = sender_id);
	IF current_balance < 0 THEN
		rollback;
	END IF;
END;
$$
LANGUAGE plpgsql;

