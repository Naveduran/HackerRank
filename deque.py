"""
Task

Perform append, pop, popleft and appendleft methods on an empty deque .

Input Format
The first line contains an integer n, the number of operations.
The next n lines contains the space separated names of methods and their values.

Output Format
Print the space separated elements of deque .

Sample Input
6
append 1
append 2
append 3
appendleft 4
pop
popleft

Sample Output
1 2
"""
from collections import deque

n_operations = int(input())
deq = deque()
for n in range(n_operations):
    s = input()
    try:
        separator = s.index(" ")
    except ValueError:
        pass
    if separator:
        method = s[0:separator]
        value = s[separator+1:]
        exec("deq." + method + "(" + value + ")")
    else:
        exec("deq." + s + "()")

for d in deq:
    print(d, end=" ")
