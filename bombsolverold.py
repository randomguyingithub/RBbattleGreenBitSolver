import copy
maxcol=25
maxrow=25
grid = list()
for row in range(maxrow):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(maxcol):
        grid[row].append(8)  # Append a cell
        
def printarr():
    for row in range(maxrow):
        print()
        for column in range(maxcol):
            print(grid[row][column],end='')

def printarr(arr):
    for row in range(maxrow):
        print()
        for column in range(maxcol):
            print(arr[row][column],end='')

def red(x,y):
    grid[y][x] = 2
            
def bomb(x,y):
    print()
    
    for row in range(0,maxrow): #bomb vertically
        #print(row,end=' ')
        if(grid[row][x]!=9):
            grid[row][x]=5
    for col in range(0,maxcol): #bomb horizonally
        #print(row,end=' ')
        if(grid[y][col]!=9):
            grid[y][col]=5
    for row in range(0,min(y,x)+1): #(to left upper corner)
        #(6,5):(5,4),(4,3),(3,2),(2,1),(1,0)
        #(6,6):(5,5),(4,4),(3,3),(2,2),(1,1),(0,0)
        #(8,6):(7,5),(6,4),(5,3),(4,2),(3,1),(2,0)
        #(6,8):(5,7),(4,6),(3,5),(2,4),(1,3),(0,2)
        if(grid[y-row][x-row]!=9):
            grid[y-row][x-row]=5
    
    for row in range(0,min(y,maxcol-1-x)+1): #(to right upper corner)
        #(6,5):(5,6),(4,7),(3,8),(2,9)
        #(8,6):(7,7),(6,8),(5,9)
        #(6,8):(5,9)
        #(2,3):(1,4),(0,5)
        if(grid[y-row][x+row]!=9):
            grid[y-row][x+row]=5
    
    for row in range(0,min(maxrow-1-y,x)+1): #(to left bottom corner)
        #(6,5):(7,4),(8,3),(9,2)
        #(8,6):(9,5)
        #(6,8):(7,7),(8,6)
        #(2,3):(3,2),(4,1),(5,0)
        if(grid[y+row][x-row]!=9):
            grid[y+row][x-row]=5
    
    for row in range(0,min(maxcol-1-y,maxrow-1-x)+1): #(to right bottom corner)
        #(6,5):(5,4),(4,3),(3,2),(2,1),(1,0)
        #(6,6):(5,5),(4,4),(3,3),(2,2),(1,1),(0,0)
        #(8,6):(7,5),(6,4),(5,3),(4,2),(3,1),(2,0)
        #(6,8):(5,7),(4,6),(3,5),(2,4),(1,3),(0,2)
        if(grid[y+row][x+row]!=9):
            grid[y+row][x+row]=5
                
    grid[y][x]=9
    print()
    
def bomb(x,y,arr):
    print()
    
    for row in range(0,maxrow): #bomb vertically
        #print(row,end=' ')
        if(arr[row][x]!=9):
            arr[row][x]=5
    for col in range(0,maxcol): #bomb horizonally
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
    
    for row in range(0,min(y,maxcol-1-x)+1): #(to right upper corner)
        #(6,5):(5,6),(4,7),(3,8),(2,9)
        #(8,6):(7,7),(6,8),(5,9)
        #(6,8):(5,9)
        #(2,3):(1,4),(0,5)
        if(arr[y-row][x+row]!=9):
            arr[y-row][x+row]=5
    
    for row in range(0,min(maxrow-1-y,x)+1): #(to left bottom corner)
        #(6,5):(7,4),(8,3),(9,2)
        #(8,6):(9,5)
        #(6,8):(7,7),(8,6)
        #(2,3):(3,2),(4,1),(5,0)
        if(arr[y+row][x-row]!=9):
            arr[y+row][x-row]=5
    
    for row in range(0,min(maxcol-1-y,maxrow-1-x)+1): #(to right bottom corner)
        #(6,5):(5,4),(4,3),(3,2),(2,1),(1,0)
        #(6,6):(5,5),(4,4),(3,3),(2,2),(1,1),(0,0)
        #(8,6):(7,5),(6,4),(5,3),(4,2),(3,1),(2,0)
        #(6,8):(5,7),(4,6),(3,5),(2,4),(1,3),(0,2)
        if(arr[y+row][x+row]!=9):
            arr[y+row][x+row]=5
                
    arr[y][x]=9
    print()
def checkresult():
    result = True
    for row in range(maxrow):
        for column in range(maxcol):
            if (grid[column][row]==2):
                result = False
                break
    return result
def checkresult(arr):
    result = True
    for row in range(maxrow):
        for column in range(maxcol):
            if (arr[column][row]==2):
                result = False
                break
    return result
def solver(arr):
    backuparr=copy.deepcopy(arr)
#     maxcell=(maxcol-1)*(maxrow-1)
#     for i in range(maxcell):
#         print(i,i+1)
    for row in range(maxrow):
        for col in range(maxcol-1):
                bomb(row,row,arr)
                bomb(row+col+1,row,arr)
                if(checkresult(arr)):
                    print("Solution(x,y):","(",col,",",row,") (",row+col+1,",",row,")")
                    printarr(arr)
                    return
                arr=copy.deepcopy(backuparr)
    print("No solution!")
                
            
            
            
    

#printarr()
#print("-----------------\n")
#grid[0][5]=9
#printarr()
print("-----------------\n")
red(1,2)
red(8,5)
red(3,3)
red(4,4)
red(6,6)
red(6,7)
# printarr()
# print("-----------------\n")
solver(grid)
# printarr()
# print("-----------------\n")
#grid[2][0]=0
#print("-----------------\n")
#printarr()
