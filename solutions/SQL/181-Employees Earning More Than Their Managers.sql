// Pattern: joins
// Difficulty: Easy
// Problem: 181. Employees Earning More Than Their Managers
// Link: https://leetcode.com/problems/employees-earning-more-than-their-managers

# Write your MySQL query statement below
-- way 1:
-- SELECT name as Employee FROM Employee e WHERE e.salary>(SELECT salary FROM Employee e1 where e1.id=e.managerID)
-- way 2 --> using joins:
SELECT e.name as Employee from Employee e JOIN Employee m on e.managerID=m.id WHERE e.salary>m.salary
