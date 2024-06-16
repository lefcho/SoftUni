CREATE or REPLACE FUNCTION fn_calculate_future_value (
	initial_sum decimal,
	yearly_interest_rate decimal,
	number_of_years int
) RETURNS DECIMAL
AS
$$
DECLARE
    future_value DECIMAL;
BEGIN
    future_value := initial_sum * ((1 + yearly_interest_rate)^number_of_years);
    RETURN TRUNC(future_value, 4);
END;
$$
LANGUAGE plpgsql;