import copy
import random
class GreenBitSolver:
    def __init__(self,maxcol=23,maxrow=23,bombs=2,arr=None):
        self.maxcol=maxcol
        self.maxrow=maxrow
        self.bombs=bombs
        self.grid = list()
        if arr == None:
            self.genarr()
        else:
            self.grid=arr
        #self.printarr(arr)
        
    
    def genarr(self):   
        for row in range(self.maxrow):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(self.maxcol):
                self.grid[row].append(8)  # Append a cell
            
    def printarr(self):
        for row in range(self.maxrow):
            print()
            for column in range(self.maxcol):
                print(self.grid[row][column],end='')

    def printarr(self,arr=None):
        if arr ==None:
            arr=self.grid
        for row in range(self.maxrow):
            print()
            for column in range(self.maxcol):
                print(arr[row][column],end='')

    def red(self,x,y):
        self.grid[y][x] = 2
                
    def bomb(self,x,y):
        #print()
        
        for row in range(0,self.maxrow): #bomb vertically
            #print(row,end=' ')
            if(self.grid[row][x]!=9):
                self.grid[row][x]=5
        for col in range(0,self.maxcol): #bomb horizonally
            #print(row,end=' ')
            if(self.grid[y][col]!=9):
                self.grid[y][col]=5
        for row in range(0,min(y,x)+1): #(to left upper corner)
            #(6,5):(5,4),(4,3),(3,2),(2,1),(1,0)
            #(6,6):(5,5),(4,4),(3,3),(2,2),(1,1),(0,0)
            #(8,6):(7,5),(6,4),(5,3),(4,2),(3,1),(2,0)
            #(6,8):(5,7),(4,6),(3,5),(2,4),(1,3),(0,2)
            if(self.grid[y-row][x-row]!=9):
                self.grid[y-row][x-row]=5
        
        for row in range(0,min(y,self.maxcol-1-x)+1): #(to right upper corner)
            #(6,5):(5,6),(4,7),(3,8),(2,9)
            #(8,6):(7,7),(6,8),(5,9)
            #(6,8):(5,9)
            #(2,3):(1,4),(0,5)
            if(self.grid[y-row][x+row]!=9):
                self.grid[y-row][x+row]=5
        
        for row in range(0,min(self.maxrow-1-y,x)+1): #(to left bottom corner)
            #(6,5):(7,4),(8,3),(9,2)
            #(8,6):(9,5)
            #(6,8):(7,7),(8,6)
            #(2,3):(3,2),(4,1),(5,0)
            if(self.grid[y+row][x-row]!=9):
                self.grid[y+row][x-row]=5
        
        for row in range(0,min(self.maxcol-1-y,self.maxrow-1-x)+1): #(to right bottom corner)
            #(6,5):(5,4),(4,3),(3,2),(2,1),(1,0)
            #(6,6):(5,5),(4,4),(3,3),(2,2),(1,1),(0,0)
            #(8,6):(7,5),(6,4),(5,3),(4,2),(3,1),(2,0)
            #(6,8):(5,7),(4,6),(3,5),(2,4),(1,3),(0,2)
            if(self.grid[y+row][x+row]!=9):
                self.grid[y+row][x+row]=5
                    
        self.grid[y][x]=9
        #print()
        
    def bomb(self,x,y,arr,b=9):
        #print()
        #print("x:",x,"y:",y,"end")
        if(arr[y][x]==2 or arr[y][x]==9):
            return
        #print("x:",x,"y:",y,"end")
        for row in range(0,self.maxrow): #bomb vertically
            #print(row,end=' ')
            #print(row,x)
            if(arr[row][x]!=9):
                arr[row][x]=5
        for col in range(0,self.maxcol): #bomb horizonally
            #print(row,end=' ')
            if(arr[y][col]!=9):
                arr[y][col]=5
        for row in range(0,min(y,x)+1): #(to left upper corner)
            #(6,5):(5,4),(4,3),(3,2),(2,1),(1,0)
            #(6,6):(5,5),(4,4),(3,3),(2,2),(1,1),(0,0)
            #(8,6):(7,5),(6,4),(5,3),(4,2),(3,1),(2,0)
            #(6,8):(5,7),(4,6),(3,5),(2,4),(1,3),(0,2)
            if(arr[y-row][x-row]!=9):
                arr[y-row][x-row]=5
        
        for row in range(0,min(y,self.maxcol-1-x)+1): #(to right upper corner)
            #(6,5):(5,6),(4,7),(3,8),(2,9)
            #(8,6):(7,7),(6,8),(5,9)
            #(6,8):(5,9)
            #(2,3):(1,4),(0,5)
            if(arr[y-row][x+row]!=9):
                arr[y-row][x+row]=5
        
        for row in range(0,min(self.maxrow-1-y,x)+1): #(to left bottom corner)
            #(6,5):(7,4),(8,3),(9,2)
            #(8,6):(9,5)
            #(6,8):(7,7),(8,6)
            #(2,3):(3,2),(4,1),(5,0)
            if(arr[y+row][x-row]!=9):
                arr[y+row][x-row]=5
        
        for row in range(0,min(self.maxcol-1-y,self.maxrow-1-x)+1): #(to right bottom corner)
            #(6,5):(5,4),(4,3),(3,2),(2,1),(1,0)
            #(6,6):(5,5),(4,4),(3,3),(2,2),(1,1),(0,0)
            #(8,6):(7,5),(6,4),(5,3),(4,2),(3,1),(2,0)
            #(6,8):(5,7),(4,6),(3,5),(2,4),(1,3),(0,2)
            if(arr[y+row][x+row]!=9):
                arr[y+row][x+row]=5
                    
        arr[y][x]=b
        #print()
    def checkresult(self):
        result = True
        for row in range(self.maxrow):
            for column in range(self.maxcol):
                if (self.grid[column][row]==2):
                    result = False
                    break
        return result
    def checkresult(self,arr):
        result = True
        #printarr(arr)
        for row in range(self.maxrow):
            for column in range(self.maxcol):
                if (arr[column][row]==2):
                    #print("I'm there")
                    #print(column,row)
                    result = False
                    break
        return result
    def solver(self,arr = None):
        if arr == None:
            arr=self.grid
        cord=list()
        backuparr=copy.deepcopy(arr)
            #print(arr)
        while(True):
            
    #     maxcell=(self.maxcol-1)*(self.maxrow-1)
    #     for i in range(maxcell):
    #         print(i,i+1)
#             for bomb in range(self.bombs):
#                 bcol=random.randint(0,self.maxcol-1)
#                 brow=random.randint(0,self.maxrow-1)
#                 tupl = (bcol,brow)
#                 cord.append(tupl)
#                 self.bomb(bcol,brow,arr)
#                 brow1=0
#                 bcol1=0
#                 brow1=0
#                 bcol1=0
            for row1 in range(self.maxrow):
                for col1 in range(self.maxcol):
                    for row2 in range(self.maxrow):
                        for col2 in range(self.maxcol):
                            self.bomb(col1,row1,arr)
                            bcol1=col1
                            brow1=row1
                            self.bomb(col2,row2,arr)
                            bcol2=col2
                            brow2=row2
                            if(self.checkresult(arr)):
                                arr2 = copy.deepcopy(arr)
                                print("Solution(x,y) start at zero:")
                                print('bomb 1:',brow1,bcol1)
                                print('bomb 2:',brow2,bcol2)
                #                     for bomb in range(self.bombs):
                #                         print('bomb',bomb+1,cord[bomb])
                                self.printarr(arr2)
                                return arr2
                                break
                            elif (row1>=self.maxrow-1 and col1 >= self.maxcol-1):
                                print("not found")
                                break
                                
                            else:
                                #self.printarr(arr)
                                #print("-----------------")
                                
                                arr=copy.deepcopy(backuparr)
    #         col1=2
    #         col2=6
    #         row1=3
    #         row2=7
            #bomb(2,3)
            #bomb(6,7)
        #printarr(arr)

                
            
        #print("No solution!")
if __name__=="__main__":
    p1 = GreenBitSolver(23,23,5)
    p1.solver()


