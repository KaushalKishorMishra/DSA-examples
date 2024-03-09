# Find First Palindromic String in the Array
# def is_palindrome(s):
#     print(f"Testing {s}")
#     return s == s[::-1]

# def main():
#     # arr = input("Enter a list of strings: ").split()
#     arr = ["hello", "world", "madam", "racecar", "python", "java"]
#     for s in arr:
#         if is_palindrome(s):
#             print(f"The first palindromic string is {s}")
#             break
#     else:
#         print("No palindromic string found")
# main()


#  Implement Stack using Queues
# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# class MyStack:

#     def __init__(self):
#         self.q1 = []
#         self.q2 = []

#     def push(self, x: int) -> None:
#         self.q1.append(x)

#     def pop(self) -> int:
#         while len(self.q1) > 1:
#             self.q2.append(self.q1.pop(0))
#         x = self.q1.pop(0)
#         self.q1, self.q2 = self.q2, self.q1
#         return x

#     def top(self) -> int:
#         while len(self.q1) > 1:
#             self.q2.append(self.q1.pop(0))
#         x = self.q1.pop(0)
#         self.q2.append(x)
#         self.q1, self.q2 = self.q2, self.q1
#         return x

#     def empty(self) -> bool:
#         return len(self.q1) == 0

#     def __str__(self):
#         return str(self.q1)

# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    n = input("Enter the number of steps: ")

    def climbStairs(self, n: int) -> int:
        if n < 3:
            print("n = ",n)
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
            print("b = ",b)
