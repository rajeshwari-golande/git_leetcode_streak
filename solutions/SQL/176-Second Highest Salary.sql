// Pattern: where condition and max func
// Difficulty: Medium
// Problem: 176. Second Highest Salary
// Link: https://leetcode.com/problems/second-highest-salary

# Write your MySQL query statement below
SELECT MAX(salary) as SecondHighestSalary FROM Employee e WHERE salary < (SELECT MAX(salary) FROM Employee)
