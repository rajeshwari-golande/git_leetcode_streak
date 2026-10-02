// Pattern: not optimal solution for the fibonacci but a basic prob of recursion
// Difficulty: Easy
// Problem: 509. Fibonacci Number
// Link: https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1 :
            return n
        return self.fib(n-1)+self.fib(n-2)


# | Complexity | Value     |
# |------------|-----------|
# | **Time**   | **O(2ⁿ)** |
# | **Space**  | **O(n)**  |

        