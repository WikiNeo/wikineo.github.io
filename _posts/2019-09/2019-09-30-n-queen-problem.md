---
title: "N Queen Problem"
published: true
---

The N Queen Problem is the problem of placing N chess queens on an NxN chessboard so that
no two queens attack each other.

## Code

```cpp
#include <iostream>
#include <vector>
#include <chrono>

#define N 8

using namespace std;

void printSol(vector<vector<int>>& sol) {
	for (auto row : sol) {
		for (auto data : row) {
			cout << data << " ";
		}
		cout << endl;
	}
	cout << endl;
}

bool validQueen(vector<vector<int>>& sol, int row, int col) {

	for (auto i = 0; i < col; i++) {
		if (sol[row][i]) {
			return false;
		}
	}

	for (auto i = row, j = col; i >= 0 && j >= 0; i--, j--) {
		if (sol[i][j]) {
			return false;
		}
	}

	for (auto i = row, j = col; i < N && j >= 0; i++, j--) {
		if (sol[i][j]) {
			return false;
		}
	}

	return true;
}

bool solveNQHelper(vector<vector<int>>& sol, int col) {
	if (col >= N) {
		return true;
	}

	for (auto row = 0; row < N; row++) {
		if (validQueen(sol, row, col)) {
			sol[row][col] = 1;
			if (solveNQHelper(sol, col + 1)) {
				return true;
			}
			else {
				sol[row][col] = 0;
			}
		}
	}

	return false;
}

void solveNQ() {
	// initialize the solution as 
	vector<vector<int>> sol(N, vector<int>(N, 0));

	if (solveNQHelper(sol, 0)) {
		printSol(sol);
	}
	else {
		cout << "There is no answer for N Queen Problem with N = " << N << endl;
	}
}

int main() {
	auto start = chrono::steady_clock::now();
	solveNQ();
	auto end = chrono::steady_clock::now();
	auto diff = end - start;
	cout << "Total execuation time ";
	cout << chrono::duration<double, milli>(diff).count() << " ms" << endl;
	return 0;
}

```

## References

- [https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/](https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/)
