SELECT 
	name,
	start_date
from 
	projects
WHERE
	name IN ('Mountain', 'Road', 'Touring' )
LIMIT 20;