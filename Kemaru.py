import pygame
import random
from tkinter import *
from tkinter import messagebox
pygame.init()
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
YELLOW   = ( 255, 246, 71)
GREEN    = (   183, 255,   173)
DGREEN   = (23,150,35)
RED      = ( 255,  48,  48)
BLUE     = (   191,   216, 255)
GREY     = ( 169, 169, 169) 
TURQ     = (182,240,223)
PURP=(55,196,152)
size = (625, 475)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kemaru by Shannon")
close=False
clock=pygame.time.Clock()
width=50
height=50
firstrun=0
global ntext,r,count,starttime
grid = []
sgrid=[]
numgrid=[]
count=10
ntext=''
x=0
y=0
r=0
set=0
text=''
starttime=pygame.time.get_ticks()
Tk().wm_withdraw()                                                  #hides the tk window
messagebox.showinfo('Rules - Close this message to begin playing','Instructions: Use the numbers 1-5 on your keyboard or numberpad to enter values in the grid. \n\n 1) Each area can be filled with numbers upto the size of the area. (An area of size 3 can have the numbers 1, 2, and 3) \n 2) A number cannot have itself in any of the cells surrounding it. (A cell that has 5 cannot have 5 in any of its surrounding cells) \n 3) You have ten hints available to use per game. \n 4) Use the check button at anytime to see if any of the cells are filled incorrectly.')

for row in range(9):             #intitalizes grids
        grid.append([])
        sgrid.append([])
        for column in range(9):
            grid[row].append(0)
            sgrid[row].append(0)

def makegrid():                     #draws the grid
    global starttime
    screen.fill(WHITE)
    pygame.draw.rect(screen,BLACK,[10,10,450,450],5)
    pygame.draw.rect(screen,BLUE,[10,10,450,450])
    y_offset=0
    y = 0
    x=0
    cells=0
    while cells<81:
        for y in range(0,9):
            x_offset=0
            if cells>0:
                y_offset = y_offset + 50   
            for x in range(0,9):
                pygame.draw.rect(screen,GREY,[10+x_offset,10+y_offset,height,width],2)
                x_offset = x_offset + 50
                cells+=1
    starttime=pygame.time.get_ticks()
    lines()
                
def solution(grid,hint=0):          #checks if grid is solved, displays initial values in grid, produces hints
    global r,firstrun
    sgrid=[[[3,4,2,5,1,3,2,4,1],[2,5,1,3,4,5,1,3,2],[1,3,4,2,1,3,2,5,4],[5,2,1,3,5,4,1,3,1],[1,4,5,4,2,3,2,4,2],[5,2,1,3,5,1,5,1,5],[4,3,4,2,4,2,3,4,2],[1,2,1,5,3,5,1,5,1],[3,4,3,2,1,4,2,3,4]],
           [[3,1,2,4,2,1,5,4,3],[2,4,3,1,5,4,3,1,2],[3,1,2,4,2,1,2,4,3],[2,4,3,1,3,5,3,1,2],[1,5,2,4,2,1,2,4,3],[4,3,1,3,5,4,3,5,1],[1,2,4,2,1,2,1,4,3],[4,5,1,3,4,5,3,2,1],[3,2,4,2,1,2,1,4,3]],
           [[1,5,2,3,4,3,1,2,5],[4,3,4,1,2,5,4,3,1],[1,5,2,3,4,1,2,5,2],[2,3,4,1,2,3,4,1,3],[1,5,2,3,4,1,5,2,4],[4,3,4,1,2,3,4,3,5],[2,1,5,3,4,1,2,1,2],[3,4,2,1,2,3,5,3,4],[2,1,3,4,5,4,1,2,1]],
           [[2,5,2,4,1,3,2,4,3],[1,3,1,3,2,4,1,5,1],[5,4,2,4,1,3,2,3,2],[3,1,3,5,2,4,1,4,1],[4,5,2,1,3,5,3,5,2],[2,1,3,4,2,4,2,4,1],[4,5,2,1,3,1,3,5,3],[3,1,4,5,2,4,2,1,2],[4,2,3,1,3,1,3,4,5]],
           [[4,3,1,5,1,4,2,3,2],[2,5,4,3,2,3,1,5,1],[1,3,2,5,1,5,4,2,4],[4,5,1,4,3,2,1,5,3],[3,2,3,2,1,5,3,4,1],[5,1,4,5,4,2,1,2,5],[2,3,2,1,3,5,4,3,1],[4,5,4,5,2,1,2,5,2],[3,2,1,3,4,3,4,1,4]],
           [[3,5,3,2,3,2,1,3,1],[1,2,1,5,1,5,4,2,4],[4,3,4,2,4,2,3,5,3],[1,2,5,1,3,1,4,2,1],[4,3,4,2,4,2,5,3,5],[1,5,1,3,1,3,1,4,2],[2,3,2,4,2,4,2,3,1],[4,1,5,3,5,1,5,4,2],[3,2,4,1,2,4,3,1,3]],
           [[2,4,3,1,2,1,2,1,5],[3,1,2,5,3,4,3,4,3],[4,5,4,1,2,1,2,5,1],[1,3,2,3,5,4,3,4,2],[2,5,4,1,2,1,2,1,3],[3,1,2,3,4,3,5,4,2],[4,5,4,1,2,1,2,3,1],[3,1,2,5,3,5,4,5,4],[2,4,3,1,2,1,2,3,1]],
           [[2,1,4,5,1,4,1,2,5],[4,5,3,2,3,2,3,4,3],[3,2,1,4,1,5,1,2,1],[1,4,5,2,3,2,3,5,3],[5,2,3,1,5,4,1,2,1],[4,1,5,4,3,2,3,4,3],[3,2,3,2,1,4,1,2,5],[1,4,5,4,3,2,5,3,4],[3,2,3,2,1,4,1,2,1]],
           [[3,1,4,2,4,2,4,3,2],[4,2,3,1,3,1,5,1,4],[1,5,4,2,4,2,3,2,3],[3,2,1,3,1,5,1,4,1],[1,4,5,2,4,3,2,3,5],[2,3,1,3,1,5,1,4,1],[1,5,2,4,2,3,2,3,2],[2,4,1,3,5,1,4,1,5],[1,3,5,2,4,3,2,3,2]]]
    test=1
    for row in range(9):
        for col in range(9):
            if sgrid[r][row][col]!=grid[row][col]:
                test=0
    
    if test==1:             #checks if grid is solved and shows winner message
        Tk().wm_withdraw()                      #hides tk window
        timewin=pygame.time.get_ticks()-starttime
        formatwintime=str(int((timewin/60000))).zfill(2)+':'+str(int((timewin/1000%60))).zfill(2)
        result=messagebox.askyesno('Winner!','Congratulations! \n You completed this grid in: '+formatwintime+'\n Do you want to play again?')
        if result==False:
            pygame.quit()
            quit()
        else:
            randomize()
            makegrid()
            solution(numgrid)
    
    if firstrun==0:         #produces intial values in the grid
        firstrun=1
        for i in range(9):
            for j in range(2):
                ran=random.randrange(9)
                font = pygame.font.SysFont('Calibri', 25, True, False)
                nstr=str(sgrid[r][i][ran])
                nval=font.render(nstr,True,BLACK)
                screen.blit(nval, [(ran+1)*width-23, (i+1)*height-23])
                grid[i][ran]=sgrid[r][i][ran]
            
    if hint==1:         #produces hints        
            j=0
            while j < 1:
                ranrow=random.randrange(9)
                rancol=random.randrange(9)
                if grid[ranrow][rancol]!=sgrid[r][ranrow][rancol]:
                    j+=1
                    pygame.draw.rect(screen,BLUE,[rancol*width+15,ranrow*height+15,width-10,height-10])
                    font = pygame.font.SysFont('Calibri', 25, True, False)
                    nstr=str(sgrid[r][ranrow][rancol])
                    nval=font.render(nstr,True,DGREEN)
                    screen.blit(nval, [(rancol+1)*width-23, (ranrow+1)*height-23])
                    grid[ranrow][rancol]=sgrid[r][ranrow][rancol]
            solution(grid)
                    
    if hint==2:
        for i in range(9):
            for j in range(9):
                if grid[i][j]!=0 and grid[i][j]!=sgrid[r][i][j]:
                    pygame.draw.rect(screen,BLUE,[j*width+15,i*height+15,width-10,height-10])
                    font = pygame.font.SysFont('Calibri', 25, True, False)
                    nstr=str(grid[i][j])
                    nval=font.render(nstr,True,RED)
                    screen.blit(nval, [(j+1)*width-23, (i+1)*height-23])
                
def lines():            #draws the borders for each area/group
    global r
    newgrid=[[[0,1,10,20,30],[2,11,12,13,22],[3,4,5,6,14],[7,16,17,18,27],[8],[15,24,25,26,35],[21,31,41,40],[23,33,32,34,43],[28,37,38,48,58],[36,46,45,47,56],[42,52,62,61,63],[44,54,53,55,64],[50,51,60,70,80],[57,67,66,68,77],[65,75,74,76,85],[71,72,73,81,82],[78,86,87,88],[83,84]],
             [[0,1,10,11],[2,3,12,13,14],[4,5,6,7,8],[24,25,15,16],[17,18,27,28],[20,21,22,23],[26,36,37],[30,40,50,51],[31,32,33,41,42],[34,35,43,44,45],[38,48,58,47,57],[46,56,55,54,64],[52,53,62,63],[60,61,70,80],[65,66,74,75,76],[67,68,77,78],[71,72,73,81,82],[83,84],[85,86,87,88]],
             [[0,1,2,3,10],[4,5,6,7,8],[11,12,13,14,15],[16,17,25,26,27],[18,28,38,48,58],[20,21,22,23,24],[30,40,50,51],[31,32,33,34,41],[35,36,37,47],[42,43,52,53],[44,45,46,54,55],[56,57,66,76,86],[60,61,62,63,64],[65,74,75,84,85],[67,68,77,78],[70,71,80,81],[72,73,82,83],[87,88]],
             [[0,10,11,20,21],[1,2,3,4,5],[6,7,8,18],[12,22,23,32,33],[13,14,15,16,17],[24,25,26],[27,28,37,38,47],[30,31,40,41,42],[34,35,43,44],[36,46,56,57,67],[45,54,55,63,64],[48,58,68],[50,51,52,53],[60,61,62,70,71],[65,66,75,76],[72,73,74,84,85],[77,78,86,87,88],[80,81,82,83]],
             [[0,1,2,3,10],[4,5,6,7,17],[8,18],[11,12,13,14,24],[15,16,25,26,27],[20,21,22,23,33],[28,38,48,58,57],[30,31,32,40,41],[34,35,36,37,47],[42,43,44,52,53],[45,46,54,55,56],[50,51,60,70,80],[61,71,72,81,82],[62,63,64,65,66],[67,68,78,88],[73,74,75,83,84],[76,77,85,86,87]],
             [[0,1,10,11,20],[2,3,12,22,32],[4,5,6,16],[7,8,17],[13,14,23,24,34],[15,25,26,35,36],[18,28,38,48,58],[21,30,31,40],[27,37,47,56,57],[33,41,42,43],[44,54,64,74,73],[45,46,55,65,75],[50,51,60,61,70],[52,53,62,63],[66,67,68],[71,72,80,81,82],[76,77,78,87,88],[83,84,85,86]],
             [[0,1,2,3,13],[4,5,14,15],[6,7,8,16,17],[10,11,12],[18,28,38],[20,21,30,40,50],[22,23,31,32],[24,25],[26,27,36,37,47],[33,34,35,45,46],[41,42,51,52,53],[43,44,54,55,56],[48,58,68,77,78],[57,65,66,67,75],[60,70,71,72,73],[61,62,63,64,74],[76,86,87,88],[80,81,82,83],[84,85]],
             [[0,1,10,11,12],[2,3,4,13,14],[5,6,7,8,18],[15,16,26],[17,27,28,37,38],[20,21,22,31,32],[23,24,25,35,36],[30,40,50,60,61],[33,34,44,45,46],[41,42,43,53],[47,48,58,68,78],[51,52,62,63,73],[54,55,64,65],[56,57,66,67],[70,80,81],[71,72,82,83,84],[74,75,76,85,86],[77,87,88]],
             [[0,1,2,3],[4,5,14,15,16],[6,7,17,27],[8,18,28,38,48],[10,11,20,30],[12,13,21,22,23],[24,25,26,34],[31,32,33],[35,36,37,45,46],[40,50],[41,42,43,52,53],[44,54,55,64,65],[47,57,58,68,78],[51,60,61,70,71],[56,66,67],[62,63,72,73,74],[75,76,85,86],[77,87,88],[80,81,82,83,84]]]
    
    for x in range(len(newgrid[r])):
        for ele in newgrid[r][x]:
            if ele<10:
                row=0
            else:
                row=ele//10
            column=ele%10
            nextcell=(row*10)+(column+1)
            prevcell=(row*10)+(column-1)
            upcell=((row-1)*10)+column
            downcell=((row+1)*10)+column
            if nextcell not in newgrid[r][x]:
                pygame.draw.line(screen, BLACK, [(column+1)*width+10,row*height+10], [(column+1)*width+10,(row+1)*height+10], 5)
            if prevcell not in newgrid[r][x]:
                pygame.draw.line(screen, BLACK, [column*width+10,row*height+10], [column*width+10,(row+1)*height+10], 5)
            if upcell not in newgrid[r][x]:
                pygame.draw.line(screen, BLACK, [column*width+10,row*height+10], [(column+1)*width+10,row*height+10], 5)
            if downcell not in newgrid[r][x]:
                pygame.draw.line(screen, BLACK, [column*width+10,(row+1)*height+10], [(column+1)*width+10,(row+1)*height+10], 5)
    
def randomize(clear=0):                          #randomly picks a grid each time, resets the grid list when a new game starts
    global ntext,count,r,firstrun
    if clear==0:
        x=r
        while r==x:
            r=random.randrange(9)
    firstrun=0
    count=10
    numgrid.clear()
    for row in range(9):
        numgrid.append([])
        for column in range(9):
            numgrid[row].append(0)
    
while not close:
    playedtime=pygame.time.get_ticks()-starttime
    pygame.draw.rect(screen,BLACK,[500,10,85,50],2)
    font = pygame.font.SysFont('timesnewroman', 25, True, False)
    formattime=str(int((playedtime/60000))).zfill(2)+':'+str(int((playedtime/1000%60))).zfill(2)
    currtime = font.render(formattime, True, BLACK)
    pygame.draw.rect(screen,WHITE,[510,15,70,40])
    screen.blit(currtime, (512, 20))                                    #display time
    pygame.draw.rect(screen,BLACK,[500,80,80,50],2)
    pygame.draw.rect(screen,RED,[502,82,77,47])
    font = pygame.font.SysFont('timesnewroman', 25, False, False)
    quittext=font.render('Quit',False,BLACK)
    screen.blit(quittext, [515, 90])                                   #display quit
    pygame.draw.rect(screen,BLACK,[485,150,125,50],2)
    pygame.draw.rect(screen,YELLOW,[487,152,122,47])
    font = pygame.font.SysFont('timesnewroman', 25, False, False)
    restext=font.render('New Game',False,BLACK)
    screen.blit(restext, [491, 160])                                    #display reset
    pygame.draw.rect(screen,BLACK,[495,220,100,50],2)
    pygame.draw.rect(screen,GREEN,[497,222,97,47])
    font = pygame.font.SysFont('timesnewroman', 25, False, False)
    hinttext=font.render('Hints:'+str(count),False,BLACK)
    screen.blit(hinttext, [503, 230])                                   #display hint
    pygame.draw.rect(screen,BLACK,[500,290,80,50],2)
    pygame.draw.rect(screen,PURP,[502,292,77,47])
    font = pygame.font.SysFont('timesnewroman', 25, False, False)
    checktext=font.render('Check',False,BLACK)
    screen.blit(checktext, [508, 300])
    pygame.draw.rect(screen,BLACK,[500,360,80,50],2)
    pygame.draw.rect(screen,TURQ,[502,362,77,47])
    font = pygame.font.SysFont('timesnewroman', 25, False, False)
    restext=font.render('Reset',False,BLACK)
    screen.blit(restext, [512, 370])                                #clear grid
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0]<460 and pos[1]<460:               #only grabs clicks inside the grid
                x=column*width+15
                y=row*height+15
                x1=(column+1)*width-23
                y1=(row+1)*height-23
                pygame.draw.rect(screen,BLUE,[x,y,width-10,height-10])
                if numgrid[row][column]!=0:
                    ntext=str(numgrid[row][column])
                    pygame.draw.rect(screen,BLUE,[x,y,width-10,height-10])
                    font = pygame.font.SysFont('Calibri', 25, True, False)
                    newval=font.render(ntext,True,BLACK)
                    screen.blit(newval, [x1, y1])
                column = (pos[0]-10) // (width)
                row = (pos[1]-10) // (height)
                pygame.draw.rect(screen,YELLOW,[column*width+15,row*height+15,width-10,height-10])
            if pos[0]>500 and pos[0]<580 and pos[1]>80 and pos[1]<130:             #quit button function
                pygame.quit()
                quit()
            if pos[0]>485 and pos[0]<610 and pos[1]>150 and pos[1]<200:             #reset button function
                randomize()
                makegrid()
                solution(numgrid)
            if pos[0]>495 and pos[0]<595 and pos[1]>220 and pos[1]<270:             #hint button function
                if count>0:
                    count-=1
                    solution(numgrid,1)
            if pos[0]>500 and pos[0]<580 and pos[1]>290 and pos[1]<340:             #reset button function
                solution(numgrid,2)
            if pos[0]>500 and pos[0]<580 and pos[1]>360 and pos[1]<410:             #reset button function
                randomize(1)
                makegrid()
                solution(numgrid)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    text='1'
                    numgrid[row][column] = 1
                    grid[row][column] = 1
            elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    text='2'
                    numgrid[row][column] = 2
                    grid[row][column] = 1
            elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    text='3'
                    numgrid[row][column] = 3
                    grid[row][column] = 1
            elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    text='4'
                    numgrid[row][column] = 4
                    grid[row][column] = 1
            elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    text='5'
                    numgrid[row][column] = 5
                    grid[row][column] = 1
    
    if set==0:                                              #initialize first grid
        set=1
        randomize()
        makegrid()
        solution(numgrid)

    if grid[row][column] != 0:
       pygame.draw.rect(screen,BLUE,[column*width+15,row*height+15,width-10,height-10])
       font = pygame.font.SysFont('Calibri', 25, True, False)
       numval=font.render(text,True,BLACK)
       screen.blit(numval, [(column+1)*width-23, (row+1)*height-23])
       grid[row][column]=0
       text=''
       solution(numgrid)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
quit()