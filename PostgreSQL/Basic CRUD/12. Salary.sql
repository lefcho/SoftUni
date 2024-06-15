SELECT 
	CONCAT(first_name, ' ', last_name) as full_name,
	job_title,
	salary
from 
	employees 
WHERE
	salary IN (12500, 14000, 23600, 25000)
ORDER BY salary DESC;