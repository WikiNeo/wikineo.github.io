---
title: "How to solve a Dynamic Programming Problem ?"
published: true
tags: DynamicProgramming
---

Dynamic Programming (DP) is a technique that solves some particular type of
problems in Polynomial Time. Dynamic Programming solutions are faster than the
exponential brute method and can be easily proved for their correctness.

## Overlapping Sub-problems

Dynamic Programming is an algorithmic paradigm that solves a given complex
problem by breaking it into sub-problems and stores the results of sub-problems to
avoid computing the same results again.

Like Divide and Conquer, Dynamic Programming combines solutions to sub-problems.
Dynamic Programming is mainly used when solutions of the same sub-problems are
needed again and again. In Dynamic Programming, computed solutions to
sub-problems are stored in a table so that these don't have to be recomputed. So
Dynamic Programming is not useful when there are not common (overlapping)
sub-problems because there is no point storing the solutions if they are not
needed again.

```python
# a simple recursive program for Fibonacci numbers
def fib(n):
	if n <= 1:
		return n

	return fib(n - 1) + fib(n - 2)
```

### Memoization (Top Down)

The memoized program for a problem is similar to the recursive version with a
small modification that looks into a lookup table before computing solutions.

```python
# a program for Memoized version of nth Fibonacci number
 
# function to calculate nth Fibonacci number
def fib(n, lookup):
 
    # base case
    if n <= 1 :
        lookup[n] = n
 
    # if the value is not calculated previously then calculate it
    if lookup[n] is None:
        lookup[n] = fib(n-1 , lookup)  + fib(n-2 , lookup)
 
    # return the value corresponding to that value of n
    return lookup[n]
# end of function
 
# Driver program to test the above function
def main():
    n = 34
    # Declaration of lookup table
    # Handles till n = 100
    lookup = [None] * 101
    print "Fibonacci Number is ", fib(n, lookup)
 
if __name__=="__main__":
    main()
```

### Tabulation (Bottom Up) 

The tabulated program for a given problem builds a table in bottom-up fashion
and returns the last entry from the table.

```python
# Python program Tabulated (bottom up) version
def fib(n):

	# array declaration
	f = [0] * (n + 1)

	# base case assignment
	f[1] = 1

	# calculating the fibonacci and storing the values
	for i in xrange(2 , n + 1):
		f[i] = f[i - 1] + f[i - 2]
	return f[n]

# Driver program to test the above function
def main():
	n = 9
	print "Fibonacci number is " , fib(n)

if __name__=="__main__":
	main()

# This code is contributed by Nikhil Kumar Singh (nickzuck_007)
```

## Optimal Substructure Property

A given problem has Optimal Substructure Property if optimal solution of the
given problem can be obtained by using optimal solutions of its sub-problems.

## How to Solve a Dynamic Programming Problem

```Steps to solve a DP
1) Identify if it is a DP problem
2) Decide a state expression with least parameters
3) Formulate state relationship
4) Do tabulation (or add memoization)
```

### Step 1: How to classify a problem as a Dynamic Programming Problem?

- Typically, all the problems that requires maximizing or minimizing certain
  quantities or counting problems that say to count the arrangements under
  certain conditions or certain probability problems can be solved by using
  Dynamic Programming.
- All dynamic programming problems satisfy the overlapping sub-problems property
  and most of the classic dynamic problems also satisfy the optimal substructure
  property.

### Step 2: Deciding the state

DP problems are all about state and their transition. This is the most basic
step which must be done very carefully because the state transition depends on
the choice of state definition you make.

A state can be defined as the set of parameters that can uniquely identify a
certain position or standing in the given problem. This set of parameters should
be as small as possible to reduce state space.

### Step 3: Formulating a relation among the states

```shell
Given 3 numbers {1, 3, 5}, we need to tell
the total number of ways we can form a number 'N' 
using the sum of the given three numbers.
(allowing repetitions and different arrangements).

Total number of ways to form 6 is: 8
1+1+1+1+1+1
1+1+1+3
1+1+3+1
1+3+1+1
3+1+1+1
3+3
1+5
5+1
```

Let’s think dynamically about this problem. So, first of all, we decide a state
for the given problem. We will take a parameter n to decide state as it can
uniquely identify any subproblem. So, our state dp will look like state(n).
Here, state(n) means the total number of arrangements to form n by using {1, 3,
5} as elements.

#### 1) Adding 1 to all possible combinations of state (n = 6) 

```shell
Eg : [ (1+1+1+1+1+1) + 1] 
[ (1+1+1+3) + 1] 
[ (1+1+3+1) + 1] 
[ (1+3+1+1) + 1] 
[ (3+1+1+1) + 1] 
[ (3+3) + 1] 
[ (1+5) + 1] 
[ (5+1) + 1] 
```

#### 2) Adding 3 to all possible combinations of state (n = 4);

```shell
Eg : [(1+1+1+1) + 3] 
[(1+3) + 3] 
[(3+1) + 3] 
```

#### 3) Adding 5 to all possible combinations of state(n = 2) 

```shell
Eg : [ (1+1) + 5]
```

In general

```shell
state(n) = state(n-1) + state(n-3) + state(n-5)
```

```python3
# Returns the number of arrangements to
# form 'n'
def solve(n):

# Base case
if n < 0:
	return 0
if n == 0:
	return 1

return (solve(n - 1) +
		solve(n - 3) +
		solve(n - 5))

```

### Step 4: Adding memoization or tabulation for the state

```python3
# This function returns the number of
# arrangements to form 'n'

# lookup dictionary/hashmap is initialized
def solve(n, lookup = {}):
	
	# Base cases
	# negative number can't be
	# produced, return 0
	if n < 0:
		return 0

	# 0 can be produced by not
	# taking any number whereas
	# 1 can be produced by just taking 1
	if n == 0:
		return 1

	# Checking if number of way for
	# producing n is already calculated
	# or not if calculated, return that,
	# otherwise calulcate and then return
	if n not in lookup:
		lookup[n] = (solve(n - 1) +
					solve(n - 3) +
					solve(n - 5))
					
	return lookup[n]
```

## Reference

- [https://www.geeksforgeeks.org/solve-dynamic-programming-problem/](https://www.geeksforgeeks.org/solve-dynamic-programming-problem/)
- [https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/](https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/)
- [https://www.geeksforgeeks.org/optimal-substructure-property-in-dynamic-programming-dp-2/](https://www.geeksforgeeks.org/optimal-substructure-property-in-dynamic-programming-dp-2/)