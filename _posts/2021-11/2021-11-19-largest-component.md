---
title: "[Graph] Largest Components"
published: true
tags: Graph
---

## Problem

Write a function, largestComponent, that takes in the adjacency list of an undirected graph. The function should return
the size of the largest connected component in the graph.

## Thoughts

When it comes to largest, we will always have a comparison logic.

We need get the size of each components with DFS or BFS, then compare and
return.

## DFS Recursion, DFS Stack, BFS Queue

```javascript
// ------------------ DFS Recursion -----------------------------------------
const largestComponent = (graph) => {
	const visited = new Set()
	let largestSize = 0;

	for(let node in graph) {
		const size = countComponentSize(graph, node, visited)
		if(size > largestSize) {
			largestSize = size;
		}
	}

	return largestSize;
};

const countComponentSize = (graph, src, visited) => {
	// the base case should also return the size
	if(visited.has(src)) return 0;

	// update visited & size here
	visited.add(src)
	let size = 1;

	for(let neighbor of graph[src]) {
		size += countComponentSize(graph, neighbor, visited)
	}

	return size;
}

// ------------------ DFS Stack ---------------------------------------
const largestComponentDFS = (graph) => {
	const visited = new Set()
	let largestSize = 0;

	for(let node in graph) {
		const size = countComponentSizeDFS(graph, node, visited)
		if(size > largestSize) {
			largestSize = size;
		}
	}

	return largestSize;
};

const countComponentSizeDFS = (graph, src, visited) => {
	// the base case should also return the size
	if(visited.has(src)) return 0;

	let size = 0;
	// add src to stack & visited.
	const stack = [src]
	visited.add(src)

	while(stack.length > 0) {
		const current = stack.pop();
		size += 1;

		for(let neighbor of graph[current]) {
			if(visited.has(neighbor)) continue;
			// if not visited, add it
			visited.add(neighbor)
			stack.push(neighbor)
		}

	}

	return size;
}

// ------------------ BFS Queue --------------------------------------
const largestComponentBFS = (graph) => {
	const visited = new Set()
	let largestSize = 0;

	for(let node in graph) {
		const size = countComponentSizeBFS(graph, node, visited)
		if(size > largestSize) {
			largestSize = size;
		}
	}

	return largestSize;
};

const countComponentSizeBFS = (graph, src, visited) => {
	// the base case should also return the size
	if(visited.has(src)) return 0;

	let size = 0;
	// add src to queue & visited
	const queue = [src]
	visited.add(src)

	while(queue.length > 0) {
		const current = queue.shift();
		size += 1;

		for(let neighbor of graph[current]) {
			if(visited.has(neighbor)) continue;
			// if not visited, add it
			visited.add(neighbor)
			queue.push(neighbor)
		}
	}

	return size;
}


console.log(largestComponent({
	0: ['8', '1', '5'],
	1: ['0'],
	5: ['0', '8'],
	8: ['0', '5'],
	2: ['3', '4'],
	3: ['2', '4'],
	4: ['3', '2']
})); // -> 4)

console.log(largestComponent({
	1: ['2'],
	2: ['1','8'],
	6: ['7'],
	9: ['8'],
	7: ['6', '8'],
	8: ['9', '7', '2']
})); // -> 6

console.log(largestComponent({
	3: [],
	4: ['6'],
	6: ['4', '5', '7', '8'],
	8: ['6'],
	7: ['6'],
	5: ['6'],
	1: ['2'],
	2: ['1']
})); // -> 5

console.log(largestComponent({})) // -> 0

console.log(largestComponent({
	0: ['4','7'],
	1: [],
	2: [],
	3: ['6'],
	4: ['0'],
	6: ['3'],
	7: ['0'],
	8: []
})); // -> 3)


console.log('------------DFS Stack-------')
console.log(largestComponentDFS({
	0: ['8', '1', '5'],
	1: ['0'],
	5: ['0', '8'],
	8: ['0', '5'],
	2: ['3', '4'],
	3: ['2', '4'],
	4: ['3', '2']
})); // -> 4)

console.log(largestComponentDFS({
	1: ['2'],
	2: ['1','8'],
	6: ['7'],
	9: ['8'],
	7: ['6', '8'],
	8: ['9', '7', '2']
})); // -> 6

console.log(largestComponentDFS({
	3: [],
	4: ['6'],
	6: ['4', '5', '7', '8'],
	8: ['6'],
	7: ['6'],
	5: ['6'],
	1: ['2'],
	2: ['1']
})); // -> 5

console.log(largestComponentDFS({})) // -> 0

console.log(largestComponentDFS({
	0: ['4','7'],
	1: [],
	2: [],
	3: ['6'],
	4: ['0'],
	6: ['3'],
	7: ['0'],
	8: []
})); // -> 3)

console.log('------------BFS Queue-------')
console.log(largestComponentBFS({
	0: ['8', '1', '5'],
	1: ['0'],
	5: ['0', '8'],
	8: ['0', '5'],
	2: ['3', '4'],
	3: ['2', '4'],
	4: ['3', '2']
})); // -> 4)

console.log(largestComponentBFS({
	1: ['2'],
	2: ['1','8'],
	6: ['7'],
	9: ['8'],
	7: ['6', '8'],
	8: ['9', '7', '2']
})); // -> 6

console.log(largestComponentBFS({
	3: [],
	4: ['6'],
	6: ['4', '5', '7', '8'],
	8: ['6'],
	7: ['6'],
	5: ['6'],
	1: ['2'],
	2: ['1']
})); // -> 5

console.log(largestComponentBFS({})) // -> 0

console.log(largestComponentBFS({
	0: ['4','7'],
	1: [],
	2: [],
	3: ['6'],
	4: ['0'],
	6: ['3'],
	7: ['0'],
	8: []
})); // -> 3)

```

## Reference

- [https://www.youtube.com/watch?v=tWVWeAqZ0WU](https://www.youtube.com/watch?v=tWVWeAqZ0WU)