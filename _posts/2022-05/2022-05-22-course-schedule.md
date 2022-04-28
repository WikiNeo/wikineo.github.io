---
title: '[LeetCode 207] Course Schedule'
published: true
tags: Graph
---

## Problem

There are a total of `numCourses` courses you have to take, labeled from `0` to
`numCourses - 1`. You are given an array prerequisites where `prerequisites[i] =
[ai, bi]` indicates that you **must** take course `bi` first if you want to take
course `ai`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have
  to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

### Example 1:

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
```

### Example 2:

```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```
 
#### Constraints:

- `1 <= numCourses <= 105`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- All the pairs prerequisites[i] are **unique**.

## Thoughts

- DFS cycle detection
- BFS topological sort

## TypeScript

### DFS Cycle Detection

```typescript
function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    const graph: Map<number, number[]> = new Map<number, number[]>();
    const visited: Set<number> = new Set<number>();
    
    // construct map
    for(const [course, pre] of prerequisites){
        const preList: number[] = graph.get(course) || [];
        preList.push(pre);
        graph.set(course, preList);
    }
    
    // DFS cycle detection
    const hasCycle = (node: number): boolean => {
        // base case
        if(visited.has(node)) {
            return true;
        }
        
        // visit node
        visited.add(node)
        const neighbours = graph.get(node) || []
        for(let neighbour of neighbours){
            if(hasCycle(neighbour)){
                return true
            }
        }
        // unvisited node
        visited.delete(node)
        // no repeated work later
        graph.set(node, [])
        
        return false
    }
    
    for(let i = 0; i < numCourses; i++){
        if(hasCycle(i)){
            return false;
        }
    }
    
    return true;
};
```

### BFS Topological Sort

```typescript
function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    let finishedCourses = 0;
    
    let coursePreCount: number[] = [];
    const queue: number[] = [];
    const graph: Map<number, number[]> = new Map<number, number[]>()
    
    // init pres and graph
    for(let i = 0; i < numCourses; i++){
        coursePreCount[i] = 0;
        graph[i] = []
    }
    
    // update pres and graph
    for(const [course, pre] of prerequisites){
        coursePreCount[course]++
        graph[pre].push(course)
    }
    
    // start course with no pres
    for(let i = 0; i < numCourses; i++){
        if(coursePreCount[i] === 0){
            queue.push(i)
        }
    }
    
    // let's start BFS
    while(queue.length > 0){
        const course = queue.shift();
        
        finishedCourses++
        if(finishedCourses === numCourses) {
            return true
        }
        
        for(let node of graph[course]){
            coursePreCount[node]--;
            if(coursePreCount[node] === 0){
                queue.push(node);
            }
        }
    }
    
    return false;
};
```

## Reference

- [https://leetcode.com/problems/course-schedule/](https://leetcode.com/problems/course-schedule/)