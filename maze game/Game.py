import random 
from graphics import *


def main():
    

# IDE: Integrated Development Environment - In our case this is IDLE.
# Note the indentation. In python this is VERY important.

    begin()

def game():
    movement()
    maze1()
    begin()

def afterkidnap():
    kidnap()
    maze1()
def ifskip():
    win = GraphWin('You Won', 1000, 1000)

    line(500,200,30,"Congradulation",win)
    line(500,400,20,"you completed maze but at the cost",win)
    line(500,500,20,"of knowing you couldnt beat the maze,",win)
    line(500,600,20,"knowing you dont have the skill to do it",win)
    line(500,800,10,"Click to continue",win)

    win.getMouse() # pause for click in window 
    win.close()
def begin():
    win = GraphWin("LAB ESCAPE", 1000, 700)

    tImage = Image(Point(500,500), "New_Back.png")
    tImage.draw(win)
    # Title Screen
    title = Text(Point(500, 200), "LAB ESCAPE")
    title.setTextColor("yellow")
    title.setSize(36)
    title.draw(win)

    # Create three buttons on the title screen
    begin_button = create_button(win, Point(500, 400), 200, 50, "Begin")  # This button will start something
    level_button = create_button(win, Point(500, 500), 200, 50, "View Levels")  # This button will show the level view
    close_button = create_button(win, Point(500, 600), 200, 50, "Close")  # This button will close the game

    # Wait for a mouse click
    while True:
        click_point = win.getMouse()
        if begin_button.getP1().getX() <= click_point.getX() <= begin_button.getP2().getX() and begin_button.getP1().getY() <= click_point.getY() <= begin_button.getP2().getY():
            win.close()
            game()
            break
        elif level_button.getP1().getX() <= click_point.getX() <= level_button.getP2().getX() and level_button.getP1().getY() <= click_point.getY() <= level_button.getP2().getY():
            win.close()
            levels()
            break
        elif close_button.getP1().getX() <= click_point.getX() <= close_button.getP2().getX() and close_button.getP1().getY() <= click_point.getY() <= close_button.getP2().getY():
            win.close()
            break

def levels():
    win = GraphWin("Level Selector", 1000, 700)

    tImage = Image(Point(500,500), "New_Back.png")
    tImage.draw(win)
    # Title Screen
    title = Text(Point(500, 150), "Level Selector")
    title.setTextColor("yellow")
    title.setSize(36)
    title.draw(win)
    
    lv1 = create_button(win, Point(500, 300), 200, 50, "Level 1")  
    lv2 = create_button(win, Point(500, 400), 200, 50, "Level 2")  
    lv3 = create_button(win, Point(500, 500), 200, 50, "Level 3")  
    lv4 = create_button(win, Point(500, 600), 200, 50, "Level 4")
    blkrect(420,595,580,605,win)

    # Wait for a mouse click
    while True:
        click_point = win.getMouse()
        if lv1.getP1().getX() <= click_point.getX() <= lv1.getP2().getX() and lv1.getP1().getY() <= click_point.getY() <= lv1.getP2().getY():
            win.close()
            maze1()
            congrats1() 
            begin()
        elif lv2.getP1().getX() <= click_point.getX() <= lv2.getP2().getX() and lv2.getP1().getY() <= click_point.getY() <= lv2.getP2().getY():
            win.close()
            maze2()
            congrats2() 
            begin()
        elif lv3.getP1().getX() <= click_point.getX() <= lv3.getP2().getX() and lv3.getP1().getY() <= click_point.getY() <= lv3.getP2().getY():
            win.close()
            maze3()
            congrats3() 
            begin()
        elif lv4.getP1().getX() <= click_point.getX() <= lv4.getP2().getX() and lv4.getP1().getY() <= click_point.getY() <= lv4.getP2().getY():
            win.close()
            break

def movement():
    win = GraphWin('Instruction', 1000, 1000)
    line(500,200,35,"Instructions",win)
    line(500,500,25,"To move use the w a s d keys to control the character",win)
    line(500,600,25,"you can also use arrow keys",win)
    line(500,700,25,'if you get too annoyed you can press "p" to skip the level',win)
    line(500,950,15,"Click to continue",win)
    win.getMouse() 
    win.close()
def kidnap():
    win = GraphWin('Kidnapped', 1000, 1000)
    line(500,200,35,"Kidnapped",win)
    line(500,500,25,"you woke up after being knocked out",win)
    line(500,600,25,"by a mystirious force",win)
    win.getMouse() 
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
            player.undraw()
            player = Image(Point(playerpoint[0],playerpoint[1]), "BlockUp.png")
            player.draw(win)
            playerpoint[1] = playerpoint[1] - 20
            if ifcolide(list_obstacles,playerpoint[0],playerpoint[1]) == True:
                playerpoint[1] = playerpoint[1] + 10
                player.move(0, -10)  # Move up
            else:
                playerpoint[1] = playerpoint[1] + 20

        elif key == "a" or key == "Left":
            player.undraw()
            player = Image(Point(playerpoint[0],playerpoint[1]), "BlockLeft.png")
            player.draw(win)
            playerpoint[0] = playerpoint[0] - 20
            if ifcolide(list_obstacles,playerpoint[0],playerpoint[1]) == True:
                playerpoint[0] = playerpoint[0] + 10
                player.move(-10, 0)  # Move left
            else:
                playerpoint[0] = playerpoint[0] + 20

        elif key == "s" or key == "Down":
            player.undraw()
            player = Image(Point(playerpoint[0],playerpoint[1]), "BlockDown.png")
            player.draw(win)
            playerpoint[1] = playerpoint[1] + 20
            if ifcolide(list_obstacles,playerpoint[0],playerpoint[1]) == True:
                playerpoint[1] = playerpoint[1] - 10
                player.move(0, 10)   # Move down
            else:
                playerpoint[1] = playerpoint[1] - 20

        elif key == "d" or key == "Right":
            player.undraw()
            player = Image(Point(playerpoint[0],playerpoint[1]), "BlockRight.png")
            player.draw(win)
            playerpoint[0] = playerpoint[0] + 20
            if ifcolide(list_obstacles,playerpoint[0],playerpoint[1]) == True:
                playerpoint[0] = playerpoint[0] - 10
                player.move(10, 0)   # Move right
            else:
                playerpoint[0] = playerpoint[0] - 20

        elif key == "p":
            # Quit the program if '/' is pressed
            win.close()
            ifskip()
            buttoninstructions()
            maze2()
            break
        if ifin(end_space,playerpoint[0],playerpoint[1]) == True:
            win.close()
            congrats1()
            buttoninstructions()
            maze2()
            break # Quit true loop (the same thing as above)

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
    win = GraphWin('You Won', 1000, 1000)
    line(500,800,20,"Click to continue",win)
    line(500,200,35,"Congradulation",win)
    line(500,400,25,"you completed maze 1",win)
    win.getMouse() # pause for click in window
    win.close()

def buttoninstructions():
    win = GraphWin('Instruction', 1000, 1000)
    line(500,200,30,"Instructions",win)
    line(500,500,25,"In this next level you will encounter buttons",win)
    line(500,600,25,"buttons are colour coded and concected to doors",win)
    line(500,700,25,"stand on a button to deactivate or activate it.",win)
    line(500,900,20,"Click to continue",win)
    win.getMouse() # pause for click in window
    win.close()

def maze2():
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
            player.undraw()
            player = Image(Point(playerpoint[0],playerpoint[1]), "BlockUp.png")
            player.draw(win)
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
            player.undraw()
            player = Image(Point(playerpoint[0],playerpoint[1]), "BlockLeft.png")
            player.draw(win)
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
            player.undraw()
            player = Image(Point(playerpoint[0],playerpoint[1]), "BlockDown.png")
            player.draw(win)
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
            player.undraw()
            player = Image(Point(playerpoint[0],playerpoint[1]), "BlockRight.png")
            player.draw(win)
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
            win.close()
            ifskip()
            fake_end()
            maze3()
            break  # Quit the program if '/' is pressed
        elif ifin(end_space,playerpoint[0],playerpoint[1]) == True:
            win.close()
            congrats2()
            fake_end()
            maze3()
            break # Quit true loop (the same thing as above)
            
        elif buttonpressed == False:
            if ifin(button,playerpoint[0],playerpoint[1]):
                middlebutton.undraw()
                middlebutton.setFill('Light Green')
                middlebutton.draw(win)
                doorr.undraw()
                doorbit.undraw()
                doorexist = False
                buttonpressed = True

def doorcolide(door,x,y):
    if x >= door[0] and x <= door[2] and y >= door[1] and y <= door[3]:
        return False
    else:
        return True



def congrats2():
    win = GraphWin('You Won', 1000, 1000)
    line(500,800,20,"Click to continue",win)
    line(500,200,35,"Congradulation",win)
    line(500,400,25,"you completed maze 2",win)
    win.getMouse() # pause for click in window
    win.close()

def fake_end():
    win = GraphWin('Instruction', 1000, 1000)
    line(500,100,35,"Instructions",win)
    line(500,300,25,"In the next level you will encounter fake doors",win)
    line(500,400,25,"they have a difference in colour",win)
    line(500,500,25,"hope you remember what the real one looked like",win)
    line(500,600,25,"If you do enter the wrong exit you will be kidnapped",win)
    line(500,700,25,"and taken back to the start(in game)",win)
    line(500,800,25,"Good Luck",win)
    line(500,900,20,'Click to continue',win)

    win.getMouse() # pause for click in window
    win.close()

def maze3():
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
            player.undraw()
            player = Image(Point(playerpoint[0],playerpoint[1]), "BlockUp.png")
            player.draw(win)
            playerpoint[1] = playerpoint[1] - 20
            if ifcolide(listobby,playerpoint[0],playerpoint[1]) == True:
                playerpoint[1] = playerpoint[1] + 10
                player.move(0, -10)  # Move up
            else:
                playerpoint[1] = playerpoint[1] + 20
        elif key == "a" or key == "Left":
            player.undraw()
            player = Image(Point(playerpoint[0],playerpoint[1]), "BlockLeft.png")
            player.draw(win)
            playerpoint[0] = playerpoint[0] - 20
            if ifcolide(listobby,playerpoint[0],playerpoint[1]) == True:
                playerpoint[0] = playerpoint[0] + 10
                player.move(-10, 0)  # Move left
            else:
                playerpoint[0] = playerpoint[0] + 20
        elif key == "s" or key == "Down":
            player.undraw()
            player = Image(Point(playerpoint[0],playerpoint[1]), "BlockDown.png")
            player.draw(win)
            playerpoint[1] = playerpoint[1] + 20
            if ifcolide(listobby,playerpoint[0],playerpoint[1]) == True:
                playerpoint[1] = playerpoint[1] - 10
                player.move(0, 10)   # Move down
            else:
                playerpoint[1] = playerpoint[1] - 20
        elif key == "d" or key == "Right":
            player.undraw()
            player = Image(Point(playerpoint[0],playerpoint[1]), "BlockRight.png")
            player.draw(win)
            playerpoint[0] = playerpoint[0] + 20
            if ifcolide(listobby,playerpoint[0],playerpoint[1]) == True:
                playerpoint[0] = playerpoint[0] - 10
                player.move(10, 0)   # Move right
            else:
                playerpoint[0] = playerpoint[0] - 20
        elif key == "p":
            win.close()
            ifskip()
            won()
            break  # Quit the program if '/' is pressed
        elif ifin(end_space,playerpoint[0],playerpoint[1]) == True:
            congrats3()
            won()
            break # Quit true loop (the same thing as above)
        elif ifin(fake_end,playerpoint[0],playerpoint[1]) == True:

            hm = False
            break
    if hm == True:      
        win.close()
    else:
        win.close()
        afterkidnap()

def congrats3():

    win = GraphWin('You Won', 1000, 1000)
    line(500,200,30,"Congradulation",win)
    line(500,400,20,"you completed maze 3",win)
    line(500,800,10,"Click to continue",win)

    win.getMouse() # pause for click in window 
    win.close()

def won():
    win = GraphWin('You Won', 1000, 1000)
    line(500,200,30,"Conggradroolashun. \n Maze 4 coming up in the next patch :) :(",win)
    line(500,400,20,"To be continured...",win)

    win.getMouse() # pause for click in window 
    win.close()
def blkrect(x1,y1,x2,y2,win):
    rect = Rectangle(Point(x1,y1), Point(x2,y2))
    rect.setFill('black')
    rect.draw(win)
def line(x,y,large,leter,win):
    line = Text(Point(x,y),leter)
    line.setSize(large)
    line.draw(win)

def create_button(win, center, width, height, label):
    x, y = center.getX(), center.getY()
    button = Rectangle(Point(x - width/2, y - height/2), Point(x + width/2, y + height/2))
    button.setFill('lightblue')
    button.draw(win)
    text = Text(center, label)
    text.setSize(20)
    text.draw(win)
    return button

main()
