# Write your MySQL query statement below
select m.name 
from Employee e

JOIN Employee m

ON e.managerId = m.id
GROUP BY(e.managerId)
HAVING COUNT(m.id)>=5



