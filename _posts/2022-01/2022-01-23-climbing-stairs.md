---
title: '[LeetCode 70] Climbing Stairs'
published: true
tags: DynamicProgramming
---

## Problem

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### Example 1:

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

### Example 2:

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```
 
### Constraints:

```
1 <= n <= 45
```

## TypeScript

### Top Down

```typescript
function climbStairs(n: number): number {
    // how many ways to climb to step
    const stepToCount: Map<number, number> = new Map<number, number>();
    
    const climb = (step: number): number => {
        if(step === 0 || step === 1) return 1;
        if(stepToCount.has(step)) return stepToCount.get(step)
        
        const step1: number = climb(step - 1)
        const step2: number = climb(step - 2)
        if(!stepToCount.has(step - 1)) stepToCount.set(step - 1, step1)
        if(!stepToCount.has(step - 2)) stepToCount.set(step - 2, step2)
        
        return step1 + step2
    }
    
    return climb(n)
};
```

### Bottom Up

```typescript
function climbStairs(n: number): number {
    // store number of ways to climb nth stair
    let table: number[] = Array(n + 1).fill(0);
    // there is only 1 way to climb 0 or 1 stairs
    table[0] = 1;
    table[1] = 1;
    
    for(let i = 2; i <= n; i++) {
	// the way to climb ith stair comes from the sum of i - 1 and i - 2 ways
        table[i] = table[i - 1] + table[i - 2];
    }
    return table[n]
};
```

## Reference

- [https://leetcode.com/problems/climbing-stairs/](https://leetcode.com/problems/climbing-stairs/)