---
title: "[Graph] Connected Components Count"
published: true
tags: Graph
---

## Problem

Write a function, connectedComponentsCount, that takes in the adjacency list of an undirected graph.
The function should return the number of connected components within the graph.

## Thoughts

We can start DFS or BFS for a component, and return true when it has done exploration, then increase the count by 1.

Since the graph is undirected, we will use a Set to store visited node.

And note the key value type by default in Hash is String, and the value in graph array is integer, so we may need
conversion for the value in Set

## DFS Recursion, DFS Stack, BFS Queue

```javascript
// --------------------- DFS Recursion ----------------------
const connectedComponentsCount = (graph) => {
	const visited = new Set();
	let count = 0

	// the in command will get key of the hash
	for(let node in graph) {
		// let's be explicit here
		if(explore(graph, node, visited) === true) {
			count += 1
		}
	}

	return count;
};

// explore function return true when it has finished exploring the graph
const explore = (graph, current, visited) => {
	// return if has visiited the node to avoid cycle
	if(visited.has(parseInt(current))) return false;

	// update visited Set
	visited.add(parseInt(current))

	// explore current neighbor
	for(let neighbor of graph[current]) {
		explore(graph, neighbor, visited)
	}

	return true
}

// --------------------------- DFS Stack -----------------------------
const connectedComponentsCountDFS = (graph) => {
	const visited = new Set();
	let count = 0

	// the in command will get key of the hash
	for(let node in graph) {
		// let's be explicit here
		if(exploreDFS(graph, node, visited) === true) {
			count += 1
		}
	}

	return count;
};

// explore function return true when it has finished exploring the graph
const exploreDFS = (graph, src, visited) => {
	if(visited.has(parseInt(src))) return false;

	const stack = [src]

	while(stack.length > 0) {
		const current = stack.pop()
		// update visited Set
		visited.add(parseInt(current))

		// explore current neighbor
		for(let neighbor of graph[current]) {
			// return if has visited the node to avoid cycle
			if(visited.has(parseInt(neighbor))) continue;

			stack.push(neighbor)
		}
	}

	return true
}

// --------------------------- BFS Queue -----------------------------
const connectedComponentsCountBFS = (graph) => {
	const visited = new Set();
	let count = 0

	// the in command will get key of the hash
	for(let node in graph) {
		// let's be explicit here
		if(exploreBFS(graph, node, visited) === true) {
			count += 1
		}
	}

	return count;
};

// explore function return true when it has finished exploring the graph
const exploreBFS = (graph, src, visited) => {
	if(visited.has(parseInt(src))) return false;

	const queue = [src]

	while(queue .length > 0) {
		const current = queue.shift()
		// update visited Set
		visited.add(parseInt(current))

		// explore current neighbor
		for(let neighbor of graph[current]) {
			// continue if has visited the node to avoid cycle
			if(visited.has(parseInt(neighbor))) continue;
			queue.push(neighbor)
		}
	}

	return true
}

console.log('-------------DFS----------------------')
console.log(connectedComponentsCount({
	0: [8, 1, 5],
	1: [0],
	5: [0, 8],
	8: [0, 5],
	2: [3, 4],
	3: [2, 4],
	4: [3, 2]
})); // -> 2

console.log(connectedComponentsCount({
	1: [2],
	2: [1,8],
	6: [7],
	9: [8],
	7: [6, 8],
	8: [9, 7, 2]
})); // -> 1

console.log(connectedComponentsCount({})); // -> 0

console.log('-------------DFS Stack----------------------')
console.log(connectedComponentsCountDFS({
	0: [8, 1, 5],
	1: [0],
	5: [0, 8],
	8: [0, 5],
	2: [3, 4],
	3: [2, 4],
	4: [3, 2]
})); // -> 2

console.log(connectedComponentsCountDFS({
	1: [2],
	2: [1,8],
	6: [7],
	9: [8],
	7: [6, 8],
	8: [9, 7, 2]
})); // -> 1

console.log(connectedComponentsCountDFS({})); // -> 0

console.log('-------------BFS Stack----------------------')
console.log(connectedComponentsCountBFS({
	0: [8, 1, 5],
	1: [0],
	5: [0, 8],
	8: [0, 5],
	2: [3, 4],
	3: [2, 4],
	4: [3, 2]
})); // -> 2

console.log(connectedComponentsCountBFS({
	1: [2],
	2: [1,8],
	6: [7],
	9: [8],
	7: [6, 8],
	8: [9, 7, 2]
})); // -> 1

console.log(connectedComponentsCountBFS({})); // -> 0
```

## Reference

- [https://www.youtube.com/watch?v=tWVWeAqZ0WU](https://www.youtube.com/watch?v=tWVWeAqZ0WU)