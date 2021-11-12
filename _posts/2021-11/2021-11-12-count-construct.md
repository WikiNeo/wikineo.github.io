---
title: "[Dynamic Programming] Count Construct"
published: true
tags: DynamicProgramming
---

Write a function `countConstruct(target, wordBank)` that accepts a target string
and an array of strings.

The function should return the number of ways that the `target` can be
constructed by concatenating elements of the `wordBank` array.

You may reuse elements of `wordBank` as many times as needed.

## Brute Force

```javascript
const countConstruct = (target, wordBank) => {
	// base case
	// if the target is empty, we have 1 way to construct it
	if (target === '') return 1;

	let totalCount = 0;

	for(let word of wordBank) {
		if(target.startsWith(word)) {
			let remainCount = countConstruct(target.slice(word.length), wordBank)
			totalCount += remainCount;
		}
	}

	return totalCount
}
```

## Memoization

```javascript
const countConstructMemo = (target, wordBank, memo = {}) => {
	if(target in memo) return memo[target]
	// base case
	// if the target is empty, we have 1 way to construct it
	if (target === '') return 1;

	let totalCount = 0;

	for(let word of wordBank) {
		if(target.startsWith(word)) {
			let remainCount = countConstructMemo(target.slice(word.length), wordBank, memo)
			totalCount += remainCount;
		}
	}

	memo[target] = totalCount
	return totalCount
}
```

## Tabulation

```javascript
const countConstructTab = (target, wordBank) => {
	let table = Array(target.length + 1).fill(0)
	table[0] = 1;

	for (let i = 0; i <= target.length; i++) {
		if(table[i]) {
			for(let word of wordBank) {
				if(target.slice(i, i + word.length) === word) {
					table[i + word.length] += table[i]
				}
			}
		}
	}

	return table[target.length]
}
```

## Reference

- [https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11656s](https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11656s)