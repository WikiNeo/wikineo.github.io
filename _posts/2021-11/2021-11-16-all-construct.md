---
title: "[Dynamic Programming] All Construct"
published: true
tags: DynamicProgramming
---

## Problem

Write a function `allConstruct(target, wordBank)` that accepts a target string
and an array of strings

The function should return a 2D array containing all of the ways that the
`target` can be constructed by concatenating elements of the `wordBank` array.
Each element of the 2D array should represent on combination that constructs the
`target`.

You may reuse elements of `wordBank` as many times as needed.

## Brute Force

```javascript
const allConstruct = (target, wordBank) => {
	// base case
	// think of the return type, it should be the same as the last return line
	if(target === '') return [[]]

	let res = []

	for(let word of wordBank) {
		if(target.startsWith(word)) {
			let remainRes = allConstruct(target.slice(word.length), wordBank)
			let temp = remainRes.map(x => [word, ...x])
			res.push(...temp)
		}
	}

	// the return type should be the same as the base type
	return res;
}
```

## Memoization

```javascript
const allConstructMemo = (target, wordBank, memo = {}) => {
	if(target in memo) return memo[target]
	// base case
	// think of the return type, it should be the same as the last return line
	if(target === '') return [[]]

	let res = []

	for(let word of wordBank) {
		if(target.startsWith(word)) {
			let remainRes = allConstructMemo(target.slice(word.length), wordBank, memo)
			let temp = remainRes.map(x => [word, ...x])
			res.push(...temp)
		}
	}

	memo[target] = res;
	// the return type should be the same as the base type
	return res;
}
```

## Tabulation

```javascript
const allConstructTab = (target, wordBank) => {
	// default value & base case
	let table = Array(target.length + 1).fill().map(x => [])
	console.log(table)

	for(let i = 0; i <= target.length; i++) {
		// if we can construct at table i
		if(table[i].length !== 0) {
			for(let word of wordBank) {
				if(target.slice(i, i + word.length) === word) {
					// [['a', 'b']]
					let temp = table[i].map(x => [...x, word])
					if(i + word.length <= target.length) {
						// [['ab']]
						table[i + word.length].push(...temp)
					}
				}
			}
		}
	}
	
	return table[target.length]
}
```

## Reference

- [https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11656s](https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11656s)