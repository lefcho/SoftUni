SELECT 
	id, 
	first_name,
	last_name
from 
	employees 
WHERE
	middle_name IS NULL
LIMIT 3;