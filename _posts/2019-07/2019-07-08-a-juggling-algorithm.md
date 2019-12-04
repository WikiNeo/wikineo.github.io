---
title:  "A Juggling Algorithm"
published: true
categories: tech
tags: Algorithm
---

A juggling algorithm is to rotate an array of size N in place, with time complexity of O(N) and auxiliary space O(1).

## A Juggling Algorithms

1. Divide the array to several sets, and set count equals the GCD of array size and distance.
2. Rotate elements in each set by one.

### Sample Code

```cpp
/*
1. find gcd of v.size() and distance
2. divide v to gcd sets
3. move within each set
*/
void rotateWithJuggling(vector<int>& v, int distance) {
	auto arraySize = v.size();
	auto setCount = gcd(arraySize, distance);

	// since we will rotate each element in the divided sets, a total number of setCount outer loop is needed
	for (auto i = 0; i < setCount; i++) {
		// since we will rotate each element in the divided sets, the first element in each set will be replaced.
		auto temp = v[i];
		// v[j] is the element in set to be replaced by its next value
		auto j = i;

		while (1) {
			// v[k] is the element to the right of v[j] in a set
			auto k = j + distance;

			// if k goes beyond the array, it starts from the left. We use subtraction here because mod operation is slow
			if (k >= arraySize) {
				k -= arraySize;
			}
			// we have roated each element in a set
			if (k == i) {
				break;
			}
			// at this time, v[k] is the element to the right of v[j]
			v[j] = v[k];
			// update j to the next element
			j = k;
		}
		// in the end, put the temp value back
		v[j] = temp;
	}
}
```

### Analysis

We try to move each element in the array by `distance` to the left, and moving each element in the set to the left by one just achieves it.
