---
title: "[Graph] Minimum Island"
published: true
tags: Graph
---

## Problem

Write a function, minimumIsland, that takes in a grid containing Ws and Ls. W represents water and L represents land.
The function should return the size of the smallest island. An island is a vertically or horizontally connected
region of land.

You may assume that the grid contains at least one island.

## Thoughts

1. Nested loop main driver function to iterate the graph row by row
2. getSize function to get the size of island starting from each node
   - do comparison with the previous
   - visited Set to prevent infinite loop
   - variation to DFS to get size
   - boundary check
   - water check

## DFS Recursion

```javascript
const minimumIsland = (grid) => {
	let visited = new Set()
	let res = Infinity;

	for(let row = 0; row < grid.length; row++) {
		for (let col = 0; col < grid[0].length; col++) {
			const size = getSize(grid, row, col, visited)
			if(size !== 0 && size < res) {
				res = size;
			}
		}
	}

	return res;
};

const getSize = (grid, row, col, visited) => {
	// for recursion, think of the return type & the base case
	if(row < 0 || row >= grid.length) return 0;
	if(col < 0 || col >= grid[0].length) return 0;

	// water check
	if(grid[row][col] === 'W') return 0;

	// visited check & update
	const pos = row + ',' + col
	if(visited.has(pos)) return 0;
	visited.add(pos)


	// initialize the size to 1 as we are on (row, col) now
	let size = 1;
	size += getSize(grid, row - 1, col, visited)
	size += getSize(grid, row + 1, col, visited)
	size += getSize(grid, row, col - 1, visited)
	size += getSize(grid, row, col + 1, visited)

	return size;
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
minimumIsland(grid0)); // -> 2


const grid1 = [
	['L', 'W', 'W', 'L', 'W'],
	['L', 'W', 'W', 'L', 'L'],
	['W', 'L', 'W', 'L', 'W'],
	['W', 'W', 'W', 'W', 'W'],
	['W', 'W', 'L', 'L', 'L'],
];

console.log(
minimumIsland(grid1)); // -> 1


const grid2 = [
	['L', 'L', 'L'],
	['L', 'L', 'L'],
	['L', 'L', 'L'],
];

console.log(
minimumIsland(grid2)); // -> 9


const grid3 = [
	['W', 'W'],
	['L', 'L'],
	['W', 'W'],
	['W', 'L']
];

console.log(
minimumIsland(grid3)); // -> 1
```

## Reference

- [https://www.youtube.com/watch?v=tWVWeAqZ0WU](https://www.youtube.com/watch?v=tWVWeAqZ0WU)