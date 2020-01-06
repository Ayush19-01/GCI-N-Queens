#Made for the sole purpose of GCI 2019
import random
x=0
man=[]

class NQueens:
    
    def __init__(self, size):
        self.size = size
        self.solve()

  
    def printboard(self, pos):
        l=[]
        global x
        line=""
        for row in range(self.size):
            for column in range(self.size):
                if pos[row] == column:
                    line += "Q "
                else:
                    line += "* "
            line+="\n"
        l.append(line)
        man.append(l)
        x+=1
        if x==80:
            y=random.choice(man)
            print("Possible Solution : \n")
            for i in y:
                print(i)
            quit()



    def enterq(self, pos, target_row):
        if target_row == self.size:
            self.printboard(pos)
        else:
            for column in range(self.size): 
                if self.checkq(pos, target_row, column):
                    pos[target_row] = column
                    self.enterq(pos, target_row + 1)


            
    def checkq(self, pos, occupied,column):
        for i in range(occupied):
            if pos[i] == column or pos[i] - i == column - occupied or pos[i] + i == column + occupied:
                return False
        return True

    def solve(self):
        pos = [-1] * self.size
        self.enterq(pos, 0)
        
NQueens(20)
