---
title: "[Graph] Island Count"
published: true
tags: Graph
---

## Problem

Write a function, islandCount, that takes in a grid containing Ws and Ls. W represents water and L represents land.
The function should return the number of islands on the grid. An island is a vertically or horizontally connected
region of land.

## Thoughts

1. The grid is 2D array, so we can +1 -1 for row & col to move
    - bound check
2. DFS with true/false for island
3. visited Set for undirected graph
4. main driver to count number of islands

## DFS Recursion

```javascript

const islandCount = (grid) => {
	let count = 0;
	const visited = new Set()

	for(let row = 0; row < grid.length; row++) {
		for(let col = 0; col < grid[0].length; col++) {
			if(explore(grid, row, col, visited) === true) {
				count++;
			}
		}
	}

	return count;
};

const explore = (grid, row, col, visited) => {
	// bound check here
	const rowInbound = 0 <= row && row < grid.length;
	const columnInbound = 0 <= col && col < grid[0].length;
	if(!rowInbound || !columnInbound) return false;

	// water check
	if(grid[row][col] === 'W') return false;

	// visited check
	const pos = row + ',' + col
	if(visited.has(pos)) return false

	// visited update
	visited.add(pos)

	// continue to explore
	explore(grid, row - 1, col, visited)
	explore(grid, row + 1, col, visited)
	explore(grid, row, col - 1, visited)
	explore(grid, row, col + 1, visited)

	// final~
	return true
}


const grid0 = [
	['W', 'L', 'W', 'W', 'W'],
	['W', 'L', 'W', 'W', 'W'],
	['W', 'W', 'W', 'L', 'W'],
	['W', 'W', 'L', 'L', 'W'],
	['L', 'W', 'W', 'L', 'L'],
	['L', 'L', 'W', 'W', 'W'],
];

console.log(
islandCount(grid0)); // -> 3

const grid1 = [
	['L', 'W', 'W', 'L', 'W'],
	['L', 'W', 'W', 'L', 'L'],
	['W', 'L', 'W', 'L', 'W'],
	['W', 'W', 'W', 'W', 'W'],
	['W', 'W', 'L', 'L', 'L'],
];

console.log(
islandCount(grid1)); // -> 4

const grid2 = [
	['L', 'L', 'L'],
	['L', 'L', 'L'],
	['L', 'L', 'L'],
];

console.log(
islandCount(grid2)); // -> 1

const grid3 = [
	['W', 'W'],
	['W', 'W'],
	['W', 'W'],
];

console.log(
islandCount(grid3)); // -> 0
```

## Reference

- [https://www.youtube.com/watch?v=tWVWeAqZ0WU](https://www.youtube.com/watch?v=tWVWeAqZ0WU)