SELECT
	department_id,
	count(*),
	CASE
		WHEN avg(salary) > 50000 THEN 'Above average'
		WHEN avg(salary) < 50000 THEN 'Below average'
	END AS salary_level
	
FROM
	employees
GROUP BY
	department_id
HAVING 
	AVG(salary) > 30000
ORDER BY 
	department_id;