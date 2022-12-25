"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
import bitsolverClass
import bitsolverClasstest
import copy
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255,69,0)
colormode=2
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
screenwidth = 820
screenheight = 820
# This sets the margin between each cell
MARGIN = 5
maxcolumn=23
maxrow=23
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
#button
# light shade of the button
color_light = (170,170,170)
# dark shade of the button
color_dark = (100,100,100)


for row in range(maxrow):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(maxcolumn):
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
#grid[1][5] = 1
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [screenwidth, screenheight]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("green bit sim")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#button
# stores the width of the
# screen into a variable
width = screen.get_width()
# stores the height of the
# screen into a variable
height = screen.get_height()
# defining a font
smallfont = pygame.font.SysFont('Corbel',20)
# rendering a text written in this font
thestring = 'test'
text = smallfont.render(thestring , True , WHITE)
#predefine text position
textpos1 = ((width/4)*4)/2
textpos2 = height-100+40/3
textpos3 = (width/4)
buttonwidthmin=(width/4)
buttonwidthmax=(width/4)*3
buttonheightmin=height-100
buttonheightmax=height-100+40

def printarr(arr=None):
    if arr ==None:
        arr=grid
    for row in range(maxrow):
        print()
        for column in range(maxcolumn):
            print(arr[row][column],end='')


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            #print(pos)
            #if button clicked
            switch = False
            if buttonwidthmin <= mouse[0] <= buttonwidthmax and buttonheightmin <= mouse[1] <= buttonheightmax:
                gridbackup=copy.deepcopy(grid)
                #printarr(grid)
                if (switch):
                  grid = copy.deepcopy(gridbackup) 
                if (not switch):
                    switch = True
                    p1 = bitsolverClass.GreenBitSolver(maxcolumn,maxrow,2,grid)
                    p2 = bitsolverClasstest.GreenBitSolver(maxcolumn,maxrow,2,grid)
                    #p1.printarr()
                    newgrid=p2.solver()
                    grid=newgrid
                    #print("-----------------------")
                    
 
                    
                #thestring = "x="+(str)(result[0])+"y="+(str)(result)[1]
                text = smallfont.render(thestring , True , WHITE)
                textpos1=textpos3
            # Change the x/y screen coordinates to grid coordinates 
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            if pos[0] <(MARGIN + WIDTH) * maxcolumn + MARGIN and pos[1]<(MARGIN + HEIGHT) * maxrow + MARGIN:
                grid[row][column] = colormode
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(maxrow):
        for column in range(maxcolumn):
            color = WHITE
            if grid[row][column] == 2:
                color = RED
            if grid[row][column] == 9:
                color = BLUE
            if grid[row][column] == 3:
                color = GREEN
            if grid[row][column] == 5:
                color = ORANGE  
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    #Draw the button
    mouse = pygame.mouse.get_pos()
    if buttonwidthmin <= mouse[0] <= buttonwidthmax and buttonheightmin <= mouse[1] <= buttonheightmax:
        pygame.draw.rect(screen,color_light,[(width/4),height-100,(width/4)*2,40])
    else:
        pygame.draw.rect(screen,color_dark,[(width/4),height-100,(width/4)*2,40])
    
    #superimpose the text onto the button
    screen.blit(text , (textpos1,textpos2))
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()