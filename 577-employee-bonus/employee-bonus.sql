# Write your MySQL query statement below

SELECT Employee.name , Bonus.bonus

FROM Employee 

left JOIN Bonus 

ON EMPLOYEE.empId = Bonus.empId

WHERE bonus < 1000 or bonus IS NULL 
