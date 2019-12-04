---
title: "Knight's Tour"
published: true
---

A **knight's tour** is a sequence of moves of a knight on a chessboard such that the
knight visit every square only once. If the knight ends on a square that is one knight's
move from the beginning square (so that it could tour the board again immediately,
following the same path), the tour is closed, otherwise it is open.

## Thoughts

1. The chessboard/solution can be represented with a 8x8 array
2. There are a total of eight possible moves for the knight, which can be represented by
   array of pairs.
3. We can use backtracking to find a possible solution.

## Code

```cpp
/*
## Thoughts

1. The chessboard/solution can be represented with a 8x8 array
2. There are a total of eight possible moves for the knight, which can be represented by
   array of pairs.
3. We can use backtracking to find a possible solution
*/

#include <iostream>
#include <vector>
#include <chrono>

#define N 8
#define TOTAL_STEP 64

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

// a move is valid if it is within the chessboard and the position is unvisited
bool isValidMove(int nextX, int nextY, vector<vector<int>>& sol) {
	return nextX >= 0 && nextX <= 7 && nextY >= 0 && nextY <= 7 && sol[nextX][nextY] == -1;
}

bool solveKTHelper(vector<vector<int>>& sol, const vector<pair<int, int>>& moves, int curX, int curY, int step) {
	if (step == TOTAL_STEP) {
		return true;
	}

	for (auto move : moves) {
		auto nextX = curX + move.first;
		auto nextY = curY + move.second;

		if (isValidMove(nextX, nextY, sol)) {
			// we move to the new position
			sol[nextX][nextY] = step;

			// we try to move to the next position
			if (solveKTHelper(sol, moves, nextX, nextY, step + 1)) {
				return true;
			}
			else {
				// backtrack here
				sol[nextX][nextY] = -1;
			}
		}
	}

	return false;
}

void solveKT() {
	// initialize the solution as 
	vector<vector<int>> sol(N, vector<int>(N, -1));

	// eight possbile moves for the knight
	vector<pair<int, int>> moves{
		make_pair(2, 1), make_pair(1, 2), 
		make_pair(-1, 2), make_pair(-2, 1),
		make_pair(-2, -1), make_pair(-1, -2),
		make_pair(1, -2), make_pair(2, -1)
	};

	// start with the (0, 0)
	sol[0][0] = 0;

	if (solveKTHelper(sol, moves, 0, 0, 1)) {
		printSol(sol);
	}
	else {
		cout << "No solution for Knight's Tour found" << endl;
	}

}

int main() {
	auto start = chrono::steady_clock::now();
	solveKT();
	auto end = chrono::steady_clock::now();
	auto diff = end - start;
	cout << "Total execuation time ";
	cout << chrono::duration<double, milli>(diff).count() << " ms" << endl;
	return 0;
}

```

References:

- [https://en.wikipedia.org/wiki/Knight%27s_tour](https://en.wikipedia.org/wiki/Knight%27s_tour)
- [https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/](https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/)
