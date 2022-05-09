---
title: '[LeetCode 380] Insert Delete GetRandom O(1)'
published: true
tags: Map
---

## Problem

Implement the `RandomizedSet` class:

- `RandomizedSet()` Initializes the `RandomizedSet` object.
- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
- `int getRandom()` Returns a random element from the current set of elements
  (it's guaranteed that at least one element exists when this method is
  called). Each element must have the **same probability** of being returned.

You must implement the functions of the class such that each function works in **average** `O(1)` time complexity.

### Example 1:

```
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
```
 
#### Constraints:

- `-2^31 <= val <= 2^31 - 1`
- At most `2 * 10^5` calls will be made to `insert`, `remove`, and `getRandom`.
- There will be **at least one** element in the data structure when
  `getRandom` is called.

## Thoughts

- `getRandom` requires an array to store the values
- `O(1)` deletion requires a map to store value to index

## TypeScript

```typescript
class RandomizedSet {
    valueToIndex: Map<number, number>;
    valuesArray: number[];
    
    constructor() {
        this.valueToIndex = new Map<number, number>();
        this.valuesArray = []       
    }

    insert(val: number): boolean {
        const hasVal: boolean = this.valueToIndex.has(val)
        if(!hasVal){
            this.valuesArray.push(val);
            this.valueToIndex.set(val, this.valuesArray.length - 1)
        }
        return !hasVal
    }

    remove(val: number): boolean {
        const hasVal: boolean = this.valueToIndex.has(val)
        
        if(hasVal){
            const valIndex: number = this.valueToIndex.get(val)
            const lastVal: number = this.valuesArray[this.valuesArray.length - 1];
            
            // replace removed value with last & update index
            this.valuesArray[valIndex] = lastVal
            this.valueToIndex.set(lastVal, valIndex);
            // remove last
            this.valuesArray.pop();
            // update map
            this.valueToIndex.delete(val);
        }
        
        return hasVal;
    }

    getRandom(): number {
        return this.valuesArray[Math.floor(Math.random()*this.valuesArray.length)]
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
```

## Reference

- [https://leetcode.com/problems/insert-delete-getrandom-o1/](https://leetcode.com/problems/insert-delete-getrandom-o1/)