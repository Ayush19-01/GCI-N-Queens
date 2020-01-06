# GCI-N-Queens

## What is the N Queen Problem?
_The n queens puzzle is the problem of placing n chess queens on an n×n chessboard so that no two queens threaten each 
other; thus, a solution requires that no two queens share the same row, column, or diagonal. The n queens puzzle is an 
example of the more general n queens problem of placing n non-attacking queens on an n×n chessboard, for which solutions exist 
for all natural numbers n with the exception of n = 2 and n = 3._

_Here is a 8 Queens Solution as an example:_

![alt text](https://github.com/Ayush19-01/GCI-N-Queens/blob/master/img1.png)

In this task the given N was 20, the concept of backtracking and a genetic algorithm is used here. For every queen placed, the
program checks if the previously placed queen causes no harm to the current one which is reffered as backtracking.

## User Defined Functions and their purpose
### 1) printboard():

  _Prints the 20x20 board. Creates the basic structure of the board and inserts ___asterix(*)___ and ___Queens(Q)___ in their 
  respective places according to the logic. Stops the recursion after getting 20 possible solutions and prints a random solution 
  out of the 20 solutions._
  
 _Arguments Passed: self and current position of the cursor, that is, where the ___asterix(*)___ or  ___Queen(Q)___ has to be 
  placed._
  
### 2) solve():

  _It is called to solve the N Queen problem and calls other function thus creating a recursive construct until all the possible 
  cases are computerised._
  
  _Arguments Passed: self_

### 3) enterq():

  _Tries to place a ___Queen(Q___) in the targeted row by checking all N possible cases. If a valid place is found the function
  calls itself trying to place a queen on the next row until all 20 queens are placed on the NxN board. Moves onto the next 
  possible solution when the base case is satisfied, that is, filling all the 20 rows with ___Queens(Q)___. This is the main 
  logic to enter the ___Queen(Q)___._
  
  _Arguments Passed: self, position of the cursor, and the targeted row, that is, the nth row where the ___Queen(Q)___ has to be 
  placed_

### 4) checkq():
  
  _Checks if a given position is under attack from any of the previously placed queens. Checks the corresponding rows, columns 
  and diagonals. It is called inside the enterq() function and returns True if ___Queen(Q___ can be placed, else False._
  
  _Arguments Passed: self, pos, targeted row and targeted column, that is, the exact address to be attacked, which is the nth
  row and the nth column postion._
