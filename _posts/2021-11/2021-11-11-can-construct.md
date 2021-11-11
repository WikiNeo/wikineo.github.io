---
title: "[Dynamic Programming] Can Construct"
published: true
tags: DynamicProgramming
---

## Problem

Write a function `canConstruct(target, wordBank)` that accepts a target string
and an array of strings.

The function should return a boolean indicating whether or not the `target` can
be constructed by concatenating elements of the `wordBank` array.

You may reuse elements of `wordBank` as many times as needed.

## Brute Force

```javascript
const canConstruct = (target, wordBank) => {
	// base case
	if(target === '') return true;

	for(let word of wordBank) {
		// if target starts with word, try the remaining
		if(target.startsWith(word)) {
			if(canConstruct(target.slice(word.length), wordBank)) {
				return true
			}
		}
	}

	return false;
}
```

## Memoization

```javascript
const canConstructMemo = (target, wordBank, memo = {}) => {
	if(target in memo) return memo[target]

	// base case
	if(target === '') return true;

	for(let word of wordBank) {
		if(target.startsWith(word)) {
			if(canConstructMemo(target.slice(word.length), wordBank, memo)) {
				memo[target] = true
				return true
			}
		}
	}

	memo[target] = false
	return false;
}
```

## Tabulation

```javascript
const canConstructTab = (target, wordBank) => {
	// table stores if it is possible to construct the target up to index
	let table = Array(target.length + 1).fill(false)
	// empty string is true, and this is our base case.
	table[0] = true;

	for(let i = 0; i <= target.length; i++) {
		// table at i is true, then word.length later is also true
		if(table[i] === true) {
			for(let word of wordBank) {
				if(target.slice(i, i + word.length) === word) {
					table[i + word.length] = true
				}
			}
		}
	}

	return table[target.length]
}
```

## Reference

- [https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11656s](https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11656s)