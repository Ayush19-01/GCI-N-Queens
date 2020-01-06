# GCI-N-Queens
### User Defined Functions and their purpose

### 1) printboard():

  Prints the 20x20 board. Creates the basic structure of the board and inserts ___asterix(*)___ and ___Queens(Q)___ in their 
  respective places according to the logic. Stops the recursion after getting 20 possible solutions and prints a random solution 
  out of the 20 solutions.
  
  Arguments Passed: self and current position of the cursor, that is, where the ___asterix(*)___ or  ___Queen(Q)___ has to be 
  placed.
  
### 2) solve():

  It is called to solve the N Queen problem and calls other function thus creating a recursive construct until all the possible 
  cases are computerised.
  
  Arguments Passed: self

### 3) enterq():

  Tries to place a ___Queen(Q___) in the targeted row by checking all N possible cases. If a valid place is found the function
  calls itself trying to place a queen on the next row until all 20 queens are placed on the NxN board. Moves onto the next 
  possible solution when the base case is satisfied, that is, filling all the 20 rows with ___Queens(Q)___. This is the main logic 
  to enter the ___Queen(Q)___.
  
  Arguments Passed: self, position of the cursor, and the targeted row, that is, the nth row where the ___Queen(Q)___ has to be 
  placed

### 4) checkq():
  
  Checks if a given position is under attack from any of the previously placed queens. Checks the corresponding rows, columns and 
  diagonals. It is called inside the enterq() function and returns True if ___Queen(Q___ can be placed, else False.
  
  Arguments Passed: self, pos, targeted row and targeted column, that is, the exact address to be attacked, which is the nth
  row and the nth column postion.
