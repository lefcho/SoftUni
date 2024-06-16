SELECT 
	deposit_group,
	sum(deposit_interest) as deposit_interest
FROM 
	wizard_deposits
GROUP BY deposit_group
ORDER BY deposit_interest DESC;