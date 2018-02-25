# 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
**Example 1:**  
Input:
```
0 0 0
0 1 0
0 0 0
```
Output:
```
0 0 0
0 1 0
0 0 0
```
**Example 2:**   
Input:
```
0 0 0
0 1 0
1 1 1
```
Output:
```
0 0 0
0 1 0
1 2 1
```
**Note:**
1. The number of elements of the given matrix will not exceed 10,000.
2. There are at least one 0 in the given matrix.
3. The cells are adjacent in only four directions: up, down, left and right.

---

* Difficulty: Medium
* Topics: Depth-first Search, Breadth-first Search
* Companies: Google
* LeetCode: [542. 01 Matrix](https://leetcode.com/problems/01-matrix/description/)
