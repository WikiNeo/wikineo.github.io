---
title: "[Graph] Undirected Path"
published: true
tags: Graph
---

Write a function, undirectedPath, that takes in an array of edges for an undirected graph and two nodes (nodeA, nodeB).
The function should return a boolean indicating whether or not there exists a path between nodeA and nodeB.

## DFS Recursive, DFS, BFS

```javascript
// ------------------------ DFS recursive ---------------------
const undirectedPath = (edges, nodeA, nodeB) => {
	const graph = buildGraph(edges);
	return hasPath(graph, nodeA, nodeB, new Set())
};

const hasPath = (graph, src, dst, visited) => {
	// if we find the path, return true
	if(src === dst) return true;
	// if we have already visited the node, return false.
	if(visited.has(src)) return false;

	// add the node to the visited
	visited.add(src)

	// then we visit the neighbors
	for(let neighbor of graph[src]) {
		if(hasPath(graph, neighbor, dst, visited) === true) {
			return true
		}
	}

	return false
}

// -------------------- DFS stack ----------------------------
const undirectedPathDFS = (edges, nodeA, nodeB) => {
	const graph = buildGraph(edges);
	return hasPathDFS(graph, nodeA, nodeB)
};

const hasPathDFS = (graph, src, dst) => {
	// we have visited src
	const visited = new Set()
	visited.add(src)
	
	// for DFS, we use stack to store the data
	// initialize the stack with src
	const stack = [src]
	
	// while it is not empty
	while(stack.length > 0) {
		// get top
		const current = stack.pop()
		// return true if we have found the node
		if(current === dst) return true;
		
		for(let neighbor of graph[current]) {
			// skip if we have visited the node
			if(visited.has(neighbor)) continue;
			
			// add the unvisited node to Set & Stack
			visited.add(neighbor)
			stack.push(neighbor)
		}
	}
	
	return false;
}

// --------------------BFS queue--------------------
const undirectedPathBFS = (edges, nodeA, nodeB) => {
	const graph = buildGraph(edges);
	return hasPathBFS(graph, nodeA, nodeB)
};

const hasPathBFS = (graph, src, dst) => {
	// we have visited src
	const visited = new Set()
	visited.add(src)

	// for DFS, we use stack to store the data
	// initialize the stack with src
	const queue = [src]

	// while it is not empty
	while(queue .length > 0) {
		// get top
		const current = queue.shift()
		// return true if we have found the node
		if(current === dst) return true;

		for(let neighbor of graph[current]) {
			// skip if we have visited the node
			if(visited.has(neighbor)) continue;

			// add the unvisited node to Set & Stack
			visited.add(neighbor)
			queue.push(neighbor)
		}
	}

	return false;
}


const buildGraph = (edges) => {
	const graph = {}

	for(let edge of edges) {
		const [a, b] = edge;

		if(!(a in graph)) graph[a] = []
		if(!(b in graph)) graph[b] = []

		graph[a].push(b)
		graph[b].push(a)
	}

	return graph;
}


const edges = [
	['i', 'j'],
	['k', 'i'],
	['m', 'k'],
	['k', 'l'],
	['o', 'n']
];

console.log('-----DFS Recursion---------')
console.log(undirectedPath(edges, 'j', 'm')); // -> true
console.log(undirectedPath(edges, 'm', 'j')); // -> true
console.log(undirectedPath(edges, 'l', 'j')); // -> true
console.log(undirectedPath(edges, 'k', 'o')); // -> false
console.log(undirectedPath(edges, 'i', 'o')); // -> false

console.log('-----DFS Stack---------')
console.log(undirectedPathDFS(edges, 'j', 'm')); // -> true
console.log(undirectedPathDFS(edges, 'm', 'j')); // -> true
console.log(undirectedPathDFS(edges, 'l', 'j')); // -> true
console.log(undirectedPathDFS(edges, 'k', 'o')); // -> false
console.log(undirectedPathDFS(edges, 'i', 'o')); // -> false

console.log('-----BFS Queue---------')
console.log(undirectedPathBFS(edges, 'j', 'm')); // -> true
console.log(undirectedPathBFS(edges, 'm', 'j')); // -> true
console.log(undirectedPathBFS(edges, 'l', 'j')); // -> true
console.log(undirectedPathBFS(edges, 'k', 'o')); // -> false
console.log(undirectedPathBFS(edges, 'i', 'o')); // -> false

```

## Reference

- [https://www.youtube.com/watch?v=tWVWeAqZ0WU](https://www.youtube.com/watch?v=tWVWeAqZ0WU)