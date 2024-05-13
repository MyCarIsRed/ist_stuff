import random 
from graphics import *
#hi
def main():

# This is micah's very cool game


# IDE: Integrated Development Environment - In our case this is IDLE.
# Note the indentation. In python this is VERY important.
    
    #title()
    #movementinstruct()
    #maze1()
    #congrats1()
    #fake_end()
    #maze2()
    #congrats2()
    #button()
    #maze3()
    maze4()

def title():
    #prints the start button
    win = GraphWin('Lab Escape', 500, 500)
    start = Text(Point(250,400),'Click to continue')
    start.setSize(10)
    start.draw(win)
    #prints the tital
    title = Text(Point(250, 100), "LAB ESCAPE")
    title.setSize(30)
    title.draw(win)
    win.getMouse() # pause for click in window
    win.close()
    
def movementinstruct():
    win = GraphWin('Instruction', 500, 500)
    tital = Text(Point(250, 100), "Instructions")
    tital.setSize(30)
    tital.draw(win)
    h = Text(Point(250,250),'To move use the w a s d keys to control the character')
    h.setSize(15)
    h.draw(win)
    he = Text(Point(250,300),'you can also use arrow keys')
    he.setSize(15)
    he.draw(win)
    he = Text(Point(250,350),'if you get too annoyed you can press "p" to skip the level')
    he.setSize(15)
    he.draw(win)
    
    he = Text(Point(250,450),'Click to continue')
    he.setSize(10)
    he.draw(win)
    win.getMouse() # pause for click in window
    win.close()

def maze1():
    # Text to indicate the start
    win = GraphWin('Maze 1', 500, 500)
    start = Rectangle(Point(50,500), Point(0, 450))
    start.setFill("Light Green")
    start.draw(win)
    # Text to indicate the end
    end = Rectangle(Point(450,0), Point(500, 50))
    end.setFill("Red")
    end.draw(win)
    # First vertical line. Note, you can call the variables anything you want - except reserved words.
    vert1 = Rectangle(Point(0,0), Point(35,450))
    vert1.setFill('black')
    vert1.draw(win)
    
    w = Rectangle(Point(0,0), Point(450, 25))
    w.setFill('black')
    w.draw(win)
    
    vert = Rectangle(Point(25,400), Point(350, 450))
    vert.setFill('black')
    vert.draw(win)
    
    ww = Rectangle(Point(150,150), Point(500, 250))
    ww.setFill('black')
    ww.draw(win)
    
    wwa = Rectangle(Point(0,20), Point(450, 100))
    wwa.setFill('black')
    wwa.draw(win)
    # Player model
    player = Circle(Point(25, 475), 15)
    player.setFill("navy")
    player.draw(win)
    # Movement functions
    list_obstacles = {'a':[0,0,35,450],'b':[0,0,450,25],'c':[25,400,350,450],'d':[150,150,500,250],'e':[0,20,450,100]}
    end_space = [450,0,500,50]
    playerpoint = [25,475]
    while True:
        key = win.checkKey()
        if key == "w" or key == "Up":
            playerpoint[1] = playerpoint[1] - 20
            if ifcolide(list_obstacles,playerpoint[0],playerpoint[1]) == True:
                playerpoint[1] = playerpoint[1] + 10
                player.move(0, -10)  # Move up
            else:
                playerpoint[1] = playerpoint[1] + 20
        elif key == "a" or key == "Left":
            playerpoint[0] = playerpoint[0] - 20
            if ifcolide(list_obstacles,playerpoint[0],playerpoint[1]) == True:
                playerpoint[0] = playerpoint[0] + 10
                player.move(-10, 0)  # Move left
            else:
                playerpoint[0] = playerpoint[0] + 20
        elif key == "s" or key == "Down":
            playerpoint[1] = playerpoint[1] + 20
            if ifcolide(list_obstacles,playerpoint[0],playerpoint[1]) == True:
                playerpoint[1] = playerpoint[1] - 10
                player.move(0, 10)   # Move down
            else:
                playerpoint[1] = playerpoint[1] - 20
        elif key == "d" or key == "Right":
            playerpoint[0] = playerpoint[0] + 20
            if ifcolide(list_obstacles,playerpoint[0],playerpoint[1]) == True:
                playerpoint[0] = playerpoint[0] - 10
                player.move(10, 0)   # Move right
            else:
                playerpoint[0] = playerpoint[0] - 20
        elif key == "p":
            break  # Quit the program if '/' is pressed
        if ifin(end_space,playerpoint[0],playerpoint[1]) == True:
            break # Quit true loop (the same thing as above)
            
    win.close()
def ifcolide(list_obstacle,x,y):
    num = 0
    for i in list_obstacle:
        listy = list_obstacle[i]
        if x >= listy[0] and x <= listy[2] and y >= listy[1] and y <= listy[3]:
            num = num + 1
    
    if num > 0:
        return False
    else:
        return True
def ifin(endspace,x,y):
    if x >= endspace[0] and x <= endspace[2] and y >= endspace[1] and y <= endspace[3]:
        return True
    else:
        return False
def congrats1():
    win = GraphWin('You Won', 500, 500)
    start = Text(Point(250,400),'Click to continue')
    start.setSize(10)
    start.draw(win)
    #prints the tital
    title = Text(Point(250, 100), "Congradulation")
    title.setSize(30)
    title.draw(win)

    titele = Text(Point(250, 200), "you completed maze 1")
    titele.setSize(20)
    titele.draw(win)

    win.getMouse() # pause for click in window
    win.close()

def fake_end():
    win = GraphWin('Instruction', 500, 500)
    tital = Text(Point(250, 100), "Instructions")
    tital.setSize(30)
    tital.draw(win)
    h = Text(Point(250,250),'In the next level you will encounter fake doors')
    h.setSize(15)
    h.draw(win)
    he = Text(Point(250,300),'they have a difference in colour')
    he.setSize(15)
    he.draw(win)
    he = Text(Point(250,350),'hope you remember what the real one looked like')
    he.setSize(15)
    he.draw(win)
    
    he = Text(Point(250,400),'good luck.')
    he.setSize(15)
    he.draw(win)

    he = Text(Point(250,450),'Click to continue')
    he.setSize(10)
    he.draw(win)
    win.getMouse() # pause for click in window
    win.close()

    
def maze2():
    win = GraphWin('Maze 2', 500, 500)

    start = Rectangle(Point(10,500), Point(60, 450))
    start.setFill("Light Green")
    start.draw(win)

    tophoriz = Rectangle(Point(0,0), Point(500, 10))
    tophoriz.setFill("black")
    tophoriz.draw(win)

    bothoriz = Rectangle(Point(60,490), Point(500, 500))
    bothoriz.setFill("black")
    bothoriz.draw(win)

    lefvert = Rectangle(Point(0,0), Point(10, 500))
    lefvert.setFill("black")
    lefvert.draw(win)

    rvert = Rectangle(Point(490, 0), Point(500, 500))
    rvert.setFill("black")
    rvert.draw(win)

    lm = Rectangle(Point(60, 500), Point(70, 60))
    lm.setFill("black")
    lm.draw(win)

    tm = Rectangle(Point(70, 60), Point(440, 70))
    tm.setFill("black")
    tm.draw(win)

    rm = Rectangle(Point(440,70), Point(430, 440))
    rm.setFill("Black")
    rm.draw(win)

    bm = Rectangle(Point(430, 440), Point(120, 430))
    bm.setFill("Black")
    bm.draw(win)

    lmm = Rectangle(Point(120, 430), Point(130, 120))
    lmm.setFill("Black")
    lmm.draw(win)

    tmm = Rectangle(Point(130, 120), Point(380, 130))
    tmm.setFill("Black")
    tmm.draw(win)

    rmm = Rectangle(Point(380, 130), Point(370, 380))
    rmm.setFill("Black")
    rmm.draw(win)

    bmm = Rectangle(Point(370, 380), Point(180, 370))
    bmm.setFill("Black")
    bmm.draw(win)

    lastmid = Rectangle(Point(240, 240), Point(370, 260))
    lastmid.setFill("Black")
    lastmid.draw(win)

    fake_end = Rectangle(Point(320, 190), Point(370, 240))
    fake_end.setFill("maroon")
    fake_end.draw(win)

    end = Rectangle(Point(320, 260), Point(370, 310))
    end.setFill("red")
    end.draw(win)

    player = Circle(Point(35, 475), 15)
    player.setFill("navy")
    player.draw(win)

    listobby = {'tophoriz':[0,0,500,10],'bothhoriz':[60,490,500,500],'lefvert':[0,0,10,500],'rvert':[490,0,500,500],
                'lm':[60,60,70,500],'tm':[70,60,440,70],'rm':[430,70,440,440],'bm':[120,430,430,440],'lmm':[120,120,130,430],
                'tmm':[130,120,380,130],'rmm':[370,130,380,380],'bmm':[180,370,370,380],
                'lastmid':[240,240,370,260]}
    end_space = [320,260,370,310]
    fake_end = [320,190,370,240]
    playerpoint = [35,475]
    # Movement functions
    hm = True
    while True:
        key = win.checkKey()
        if key == "w" or key == "Up":
            playerpoint[1] = playerpoint[1] - 20
            if ifcolide(listobby,playerpoint[0],playerpoint[1]) == True:
                playerpoint[1] = playerpoint[1] + 10
                player.move(0, -10)  # Move up
            else:
                playerpoint[1] = playerpoint[1] + 20
        elif key == "a" or key == "Left":
            playerpoint[0] = playerpoint[0] - 20
            if ifcolide(listobby,playerpoint[0],playerpoint[1]) == True:
                playerpoint[0] = playerpoint[0] + 10
                player.move(-10, 0)  # Move left
            else:
                playerpoint[0] = playerpoint[0] + 20
        elif key == "s" or key == "Down":
            playerpoint[1] = playerpoint[1] + 20
            if ifcolide(listobby,playerpoint[0],playerpoint[1]) == True:
                playerpoint[1] = playerpoint[1] - 10
                player.move(0, 10)   # Move down
            else:
                playerpoint[1] = playerpoint[1] - 20
        elif key == "d" or key == "Right":
            playerpoint[0] = playerpoint[0] + 20
            if ifcolide(listobby,playerpoint[0],playerpoint[1]) == True:
                playerpoint[0] = playerpoint[0] - 10
                player.move(10, 0)   # Move right
            else:
                playerpoint[0] = playerpoint[0] - 20
        elif key == "p":
            break  # Quit the program if '/' is pressed
        elif ifin(end_space,playerpoint[0],playerpoint[1]) == True:
            break # Quit true loop (the same thing as above)
        elif ifin(fake_end,playerpoint[0],playerpoint[1]) == True:
            
            hm = False
            break
    if hm == True:      
        win.close()
    else:

        win.close()
        maze2()

def congrats2():
    win = GraphWin('You Won', 500, 500)
    start = Text(Point(250,400),'Click to continue')
    start.setSize(10)
    start.draw(win)
    #prints the tital
    title = Text(Point(250, 100), "Congradulation")
    title.setSize(30)
    title.draw(win)

    titele = Text(Point(250, 200), "you completed maze 2")
    titele.setSize(20)
    titele.draw(win)

    win.getMouse() # pause for click in window
    win.close()

def button():
    win = GraphWin('Instruction', 500, 500)
    tital = Text(Point(250, 100), "Instructions")
    tital.setSize(30)
    tital.draw(win)
    h = Text(Point(250,250),'In this next level you will encounter buttons')
    h.setSize(15)
    h.draw(win)
    he = Text(Point(250,300),'buttons are colour coded and concected to doors')
    he.setSize(15)
    he.draw(win)
    he = Text(Point(250,350),'stand on a button to deactivate or activate it.')
    he.setSize(15)
    he.draw(win)
    
    he = Text(Point(250,450),'Click to continue')
    he.setSize(10)
    he.draw(win)
    win.getMouse() # pause for click in window
    win.close()

def maze3():
    win = GraphWin(('Maze 3'),500,500)#window
    #start
    start = Rectangle(Point(50,500), Point(0, 450))
    start.setFill("Light Green")
    start.draw(win)
    #end
    end = Rectangle(Point(425,0), Point(475, 50))
    end.setFill("Red")
    end.draw(win)

    # First vertical line. Note, you can call the variables anything you want - except reserved words.
    blkrect(0,0,25,450,win)#a
    blkrect(75,450,500,500,win)#b
    blkrect(75,75,100,500,win)#c
    blkrect(0,0,425,25 ,win)#d
    blkrect(150,75,300,100 ,win)#e
    blkrect(300,0,325,100 ,win)#f
    blkrect(100,150,200,175 ,win)#g
    #-----
    blkrect(250,150,375,175,win)#h poop
    #-----
    blkrect(375,0,425,175,win)#i
    #_______button_____
    buttoncolour = Rectangle(Point(325, 50), Point(375, 0))
    buttoncolour.setFill('red')
    buttoncolour.draw(win)
    middlebutton = Circle(Point(350,25),(12))
    middlebutton.setFill('black')
    middlebutton.draw(win)
    #__________________
    blkrect(150,225,325,250,win)#j
    blkrect(375,175,425,400,win)#k
    blkrect(300,225,325,400,win)#l
    blkrect(150,375,400,400,win)#m
    blkrect(100,300,250,325,win)#n
    #__door___
    doorr = Rectangle(Point(350, 450), Point(375, 400))
    doorr.setFill('red')
    doorr.draw(win)
    #_________
    doorbit = Rectangle(Point(360,410), Point(365,440))#|door bit
    doorbit.setFill('black')
    doorbit.draw(win)
    blkrect(475,0,500,500,win)#p

    player = Circle(Point(35,475), 15)
    player.setFill("blue")
    player.draw(win)

    playerpoint = [35,475]
    listobby = {'a':[0,0,25,450],'b':[75,450,500,500],'c':[75,75,100,500],
                'd':[0,0,425,25],'e':[150,75,300,100],'f':[300,0,325,100],
                'g':[100,150,200,175],'h':[250,150,375,175],'i':[375,0,425,175],
                'j':[150,225,325,250],'k':[375,175,425,400],'l':[300,225,325,400],
                'm':[150,375,400,400],'n':[100,300,250,325],'p':[475,0,500,500]}
    button = [325,0,375,50]
    door = [350,400,375,450]
    end_space = [450,0,500,50]
    doorexist = True
    buttonpressed = False
    

    while True:
        key = win.checkKey()
        if key == "w" or key == "Up":
            playerpoint[1] = playerpoint[1] - 20
            if ifcolide(listobby,playerpoint[0],playerpoint[1]) == True:
                if doorexist == True:
                    if doorcolide(door,playerpoint[0],playerpoint[1]) == True:
                        playerpoint[1] = playerpoint[1] + 10
                        player.move(0, -10)  # Move up
                    else:
                        playerpoint[1] = playerpoint[1] + 20
                else:
                    playerpoint[1] = playerpoint[1] + 10
                    player.move(0, -10)  # Move up
            else:
                playerpoint[1] = playerpoint[1] + 20
        elif key == "a" or key == "Left":
            playerpoint[0] = playerpoint[0] - 20
            if ifcolide(listobby,playerpoint[0],playerpoint[1]) == True:
                if doorexist == True:
                    if doorcolide(door,playerpoint[0],playerpoint[1]) == True:
                        playerpoint[0] = playerpoint[0] + 10
                        player.move(-10, 0)  # Move left
                    else:
                        playerpoint[0] = playerpoint[0] + 20
                else:
                    playerpoint[0] = playerpoint[0] + 10
                    player.move(-10, 0)  # Move left
            else:
                playerpoint[0] = playerpoint[0] + 20
        elif key == "s" or key == "Down":
            playerpoint[1] = playerpoint[1] + 20
            if ifcolide(listobby,playerpoint[0],playerpoint[1]) == True:
                if doorexist == True:
                    if doorcolide(door,playerpoint[0],playerpoint[1]) == True:
                        playerpoint[1] = playerpoint[1] - 10
                        player.move(0, 10)   # Move down
                    else:
                        playerpoint[1] = playerpoint[1] - 20
                else:
                    playerpoint[1] = playerpoint[1] - 10
                    player.move(0, 10)   # Move down
            else:
                playerpoint[1] = playerpoint[1] - 20
        elif key == "d" or key == "Right":
            playerpoint[0] = playerpoint[0] + 20
            if ifcolide(listobby,playerpoint[0],playerpoint[1]) == True:
                if doorexist == True:
                    if doorcolide(door,playerpoint[0],playerpoint[1]) == True:               
                        playerpoint[0] = playerpoint[0] - 10
                        player.move(10, 0)   # Move right
                    else:
                        playerpoint[0] = playerpoint[0] - 20
                else:
                    playerpoint[0] = playerpoint[0] - 10
                    player.move(10, 0)   # Move right
            else:
                playerpoint[0] = playerpoint[0] - 20
        elif key == "p":
            break  # Quit the program if '/' is pressed
        elif ifin(end_space,playerpoint[0],playerpoint[1]) == True:
            break # Quit true loop (the same thing as above)
        elif buttonpressed == False:
            if ifin(button,playerpoint[0],playerpoint[1]) == True:
                middlebutton.undraw()
                middlebutton.setFill('white')
                middlebutton.draw(win)
                doorr.undraw()
                doorbit.undraw()
                doorexist = False
                buttonpressed = True
    win.close()
def doorcolide(door,x,y):
    if x >= door[0] and x <= door[2] and y >= door[1] and y <= door[3]:
        return False
    else:
        return True

def blkrect(x1,y1,x2,y2,win):
    rect = Rectangle(Point(x1,y1), Point(x2,y2))
    rect.setFill('black')
    rect.draw(win)
def maze4():
    win = GraphWin('Maze 4',700,600)

    start = Rectangle(Point(20,20),Point(60,60))
    start.setFill('light green')
    start.draw(win)

    end = Rectangle(Point(640,540),Point(680,580))
    end.setFill('red')
    end.draw(win)
    #ALL WALLS ARE 20 LONG AND ALL PATHWAYS ARE 40 LONG
    #borders
    blkrect(0,0,700,20,win)#ab roof
    blkrect(0,0,20,600,win)#bb left
    blkrect(0,580,700,600,win)#cb floor
    blkrect(680,0,700,600,win)#db right
    #
    blkrect(60,20,80,140,win)#leftvertupper
    blkrect(60,180,80,300,win)#leftvertlower
    blkrect(80,60,260,80,win)#topdend
    blkrect(120,120,140,240,win)#2nd vert middle part right of door
    #red door
    reddoor = Rectangle(Point(80,120),Point(120,140))
    reddoor.setFill('red')                  
    reddoor.draw(win)
    reddoormid = Rectangle(Point(87,127),Point(113,133))
    reddoormid.setFill('black')
    reddoormid.draw(win)
    #red button
    redbutt = Rectangle(Point(20,540),Point(60,580))
    redbutt.setFill('red')
    redbutt.draw(win)
    redbuttmid = Rectangle(Point(30,550),Point(50,570))
    redbuttmid.setFill('black')
    redbuttmid.draw(win)
    #
    blkrect(120,280,200,300,win)#middle wall
    blkrect(140,220,260,240,win)#a
    blkrect(240,220,260,600,win)#b
    blkrect(20,340,200,360,win)#c
    blkrect(120,240,140,300,win)#d
    blkrect(160,400,260,420,win)#e
    blkrect(100,400,120,460,win)#f
    blkrect(100,460,200,480,win)#g
    blkrect(180,480,200,540,win)#h
    blkrect(0,520,180,540,win)#i
    blkrect(60,400,100,420,win)#j
    blkrect(180,80,200,140,win)
    blkrect(240,140,260,220,win)
    blkrect(300,60,320,240,win)
    blkrect(300,280,360,300,win)
    blkrect(360,240,380,300,win)
    blkrect(320,180,420,200,win)
    blkrect(420,180,440,340,win)
    blkrect(300,300,320,460,win)
    blkrect(360,340,380,400,win)
    blkrect(380,380,440,400,win)#first line across
    #ouchie squares
    ouchie1 = Rectangle(Point(60,420),Point(100,460))
    ouchie1.setFill('maroon')
    ouchie1.draw(win)
    ouchie2 = Rectangle(Point(20,500),Point(60,520))
    ouchie2.setFill('maroon')
    ouchie2.draw(win)
    ouchie3 = Rectangle(Point(200,80),Point(260,100))
    ouchie3.setFill('maroon')
    ouchie3.draw(win)
    #yellow button
    ybutton = Rectangle(Point(140,480),Point(180,520))
    ybutton.setFill('yellow')
    ybutton.draw(win)
    ymidbutt = Rectangle(Point(150,490),Point(170,510))
    ymidbutt.setFill('black')
    ymidbutt.draw(win)
    #yellow door
    ydoor = Rectangle(Point(120,400),Point(160,420))
    ydoor.setFill('yellow')
    ydoor.draw(win)
    ydoormid = Rectangle(Point(127,407),Point(153,413))
    ydoormid.setFill('black')
    ydoormid.draw(win)
    
    
    
    


    
    yes = True
    player = Circle(Point(40,40), 12)
    player.setFill("blue")
    player.draw(win)
    playerpoint = [40,40]
    end_space = [640,540,680,580]
    list_obstacles = {'reddoor':[80,120,120,140],'ydoor':[120,400,160,420],'ab':[0,0,700,20],
                      'bb':[0,0,20,600],
                      'cb':[0,580,700,600,],
                      'db':[680,0,700,600],'leftvertupper':[60,20,80,140],
                      'leftvertlower':[60,180,80,300],'topdend':[80,60,260,80],
                      '2nd vermidparighdor':[120,120,140,240], 'middlewall':[120,280,200,300],
                      'a':[140,220,260,240],'b':[240,220,260,600],'c':[20,340,200,360],
                      'd':[120,240,140,300],'e':[160,400,260,420],'f':[100,400,120,460],
                      'g':[100,460,200,480],'h':[180,480,200,540],'i':[0,520,180,540],
                      'j':[60,400,100,420]}
               
    redbuttonpressed = False
    reddoorexist = True
    yelbuttonpressed = False
    yeldoorexist = True
    
    reddoorcoord = [80,120,120,140]
    ydoorcoord = [120,400,160,420]
    ouchiee1 = [60,420,100,460]
    ouchiee2 = [20,500,60,520]
    ouchiee3 = [200,80,260,100]
    ybuttoncoord = [140,480,180,520]
    redbuttoncoord = [20,540,60,580]
    
    

    
    
    while True:
        key = win.checkKey()
        #check red door
        

        
        if key == "w" or key == "Up":
            playerpoint[1] = playerpoint[1] - 20
            if ifcolide(list_obstacles,playerpoint[0],playerpoint[1]) == True:
                playerpoint[1] = playerpoint[1] + 10
                player.move(0, -10)  # Move up
            else:
                playerpoint[1] = playerpoint[1] + 20
        elif key == "a" or key == "Left":
            playerpoint[0] = playerpoint[0] - 20
            if ifcolide(list_obstacles,playerpoint[0],playerpoint[1]) == True:
                playerpoint[0] = playerpoint[0] + 10
                player.move(-10, 0)  # Move left
            else:
                playerpoint[0] = playerpoint[0] + 20
        elif key == "s" or key == "Down":
            playerpoint[1] = playerpoint[1] + 20
            if ifcolide(list_obstacles,playerpoint[0],playerpoint[1]) == True:
                playerpoint[1] = playerpoint[1] - 10
                player.move(0, 10)   # Move down
            else:
                playerpoint[1] = playerpoint[1] - 20
        elif key == "d" or key == "Right":
            playerpoint[0] = playerpoint[0] + 20
            if ifcolide(list_obstacles,playerpoint[0],playerpoint[1]) == True:
                playerpoint[0] = playerpoint[0] - 10
                player.move(10, 0)   # Move right
            else:
                playerpoint[0] = playerpoint[0] - 20
        elif key == "p":
            break  # Quit the program if '/' is pressed
        elif ifin(end_space,playerpoint[0],playerpoint[1]) == True:
            break # Quit true loop (the same thing as above)
        elif ifin(ouchiee1,playerpoint[0],playerpoint[1]) == True or ifin(ouchiee2,playerpoint[0],playerpoint[1]) == True or ifin(ouchiee3,playerpoint[0],playerpoint[1]) == True:
            yes = False
            break
        elif ifin(ybuttoncoord,playerpoint[0],playerpoint[1]) == True and yelbuttonpressed == False:
            ymidbutt.undraw()
            ymidbutt.setFill('white')
            ymidbutt.draw(win)
            yelbuttonpressed = True
            yeldoorexist = False
            ydoor.undraw()
            ydoormid.undraw()
            player.undraw()
            player.draw(win)
            list_obstacles.pop('ydoor')
        elif ifin(redbuttoncoord,playerpoint[0],playerpoint[1]) == True and redbuttonpressed == False:
            redbuttmid.undraw()
            redbuttmid.setFill('white')
            redbuttmid.draw(win)
            reddoor.undraw()
            reddoormid.undraw()
            redbuttonpressed = True
            reddoorexist = False
            player.undraw()
            player.draw(win)
            list_obstacles.pop('reddoor')
        
            
        
        

    if yes == False:
        win.close()
        maze4()
    else:
        win.close()
        
        
        
            
    win.close()
    
main()
