---
title: '[LeetCode 210] Course Schedule II'
published: true
tags: Graph
---

## Problem

There are a total of `numCourses` courses you have to take, labeled from `0`
to `numCourses - 1`. You are given an array `prerequisites` where
`prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if
you want to take course `ai`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have
  to first take course `1`.

Return the ordering of courses you should take to finish all courses. If there
are many valid answers, return **any** of them. If it is impossible to finish all
courses, return **an empty array**.

### Example 1:

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
```

### Example 2:

```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
```

### Example 3:

```
Input: numCourses = 1, prerequisites = []
Output: [0]
```
#### Constraints:

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- `ai != bi`
- All the pairs `[ai, bi]` are distinct.

## Thoughts

- Topological Sort

## TypeScript

### DFS

```typescript
function findOrder(numCourses: number, prerequisites: number[][]): number[] {
    const res: Set<number> = new Set<number>();
    
    const graph: number[][] = Array.from({length: numCourses}, () => []);
    const visited: Set<number> = new Set<number>();
    
    for(const [course, pre] of prerequisites){
        graph[course].push(pre);
    }
    
    const dfs = (course: number): boolean => {
        if(graph[course].length === 0){
            res.add(course);
            return true;
        }
        if(visited.has(course)) return false;
        
        visited.add(course);
        for(const pre of graph[course]){
            if(dfs(pre) === false){
                return false;
            }
        }
       
        graph[course] = [];
        res.add(course);
        
        return true;
    }
    
    for(let i = 0; i < numCourses; i++){
        if(dfs(i) === false){
            return []
        }
    }
    
    return [...res];
};
```

### BFS

```typescript
function findOrder(numCourses: number, prerequisites: number[][]): number[] {
    const res: number[] = [];
    const coursePreCounts: number[] = Array(numCourses).fill(0);
    const graph: number[][] = Array.from({length: numCourses}, () => []);
    const queue: number[] = [];
    
    for(let [course, pre] of prerequisites){
        graph[pre].push(course);
        coursePreCounts[course]++;
    }
    
    coursePreCounts.forEach((count, index) => {
        if(count === 0){
            res.push(index);
            queue.push(index)
        }
    })
    
    while(queue.length > 0){
        const curCourse = queue.shift();
        numCourses--;
        
        graph[curCourse].forEach(course => {
            if(--coursePreCounts[course] === 0){
                res.push(course);
                queue.push(course)
            }
        })
    }
    
    return numCourses ? [] : res;
};
```

## Reference

- [https://leetcode.com/problems/course-schedule-ii/](https://leetcode.com/problems/course-schedule-ii/)