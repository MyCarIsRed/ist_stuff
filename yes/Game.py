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
    win = GraphWin("LAB ESCAPE", 1000, 1000)

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
    win = GraphWin("Level Selector", 1000, 1000)

    tImage = Image(Point(500,500), "New_Back.png")
    tImage.draw(win)
    # Title Screen
    title = Text(Point(500, 200), "Level Selector")
    title.setTextColor("yellow")
    title.setSize(36)
    title.draw(win)
    
    lv1 = create_button(win, Point(500, 400), 200, 50, "Level 1")  
    lv2 = create_button(win, Point(500, 500), 200, 50, "Level 2")  
    lv3 = create_button(win, Point(500, 600), 200, 50, "Level 3")  
    lv4 = create_button(win, Point(500, 700), 200, 50, "Level 4")  

    # Wait for a mouse click
    while True:
        click_point = win.getMouse()
        if lv1.getP1().getX() <= click_point.getX() <= lv1.getP2().getX() and lv1.getP1().getY() <= click_point.getY() <= lv1.getP2().getY():
            win.close()
            maze1()
        elif lv2.getP1().getX() <= click_point.getX() <= lv2.getP2().getX() and lv2.getP1().getY() <= click_point.getY() <= lv2.getP2().getY():
            win.close()
            maze2()
        elif lv3.getP1().getX() <= click_point.getX() <= lv3.getP2().getX() and lv3.getP1().getY() <= click_point.getY() <= lv3.getP2().getY():
            win.close()
            maze3()
        elif lv4.getP1().getX() <= click_point.getX() <= lv4.getP2().getX() and lv4.getP1().getY() <= click_point.getY() <= lv4.getP2().getY():
            win.close()
            maze4()

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
    win = GraphWin('Maze 1', 1000, 1000)
    start = Rectangle(Point(15,985), Point(65, 935))
    start.setFill("Light Green")
    start.draw(win)
    # Text to indicate the end
    end = Rectangle(Point(985,15), Point(935, 65))
    end.setFill("Red")
    end.draw(win)
    # function that draws black lines
    blkrect(0,0,15,1000,win)
    blkrect(0,0,1000,15,win)
    blkrect(0,1000,1000,985,win)
    blkrect(1000,0,985,1000,win)
    blkrect(300,0,315,800,win)
    blkrect(600,200,615,1000,win)
    blkrect(850,0,865,600,win)

    # Player model
    player = Image(Point(40,960), "BlockUp.png")
    player.draw(win)
    
    # Movement functions
    list_obstacles = {'vert1':[0,0,15,1000],'vert2':[0,0,1000,15],'vert3':[0,985,1000,1000],'vert4':[985,0,1000,1000],'vert5':[300,0,315,800],'vert6':[600,200,615,1000],'vert7':[850,0,865,600]}
    end_space = [935,15,985,65]
    playerpoint = [40, 960]
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
    win = GraphWin(('Maze 2'),1000,1000)#window
    #start
    start = Rectangle(Point(15,985), Point(65, 935))
    start.setFill("Light Green")
    start.draw(win)
    #end
    end = Rectangle(Point(985,15), Point(935, 65))
    end.setFill("Red")
    end.draw(win)

    # First vertical line. Note, you can call the variables anything you want - except reserved words.
    blkrect(0,0,15,1000,win)#1
    blkrect(0,985,1000,1000,win)#2
    blkrect(985,0,1000,1000,win)#3
    blkrect(0,0,1000,15,win)#4
    blkrect(920,0,935,900,win)#5
    blkrect(65,60,80,1000,win)#6
    blkrect(80,60,850,75,win)#7
    blkrect(80,400,500,415,win)#8
    blkrect(920,400,550,415,win)#9
    blkrect(485,125,500,415,win)#10
    blkrect(300,125,485,140,win)#11
    blkrect(70,125,250,140,win)#12
    blkrect(235,140,250,350,win)# 13
    blkrect(300,140,315,350,win)# 14
    blkrect(300,350,400,365,win)# 15
    blkrect(385,200,400,365,win)# 16
    blkrect(130,885,920,900,win)# 17
    blkrect(70,800,870,815,win)# 18
    blkrect(130,500,145,815,win)# 19
    blkrect(130,485,250,500,win)# 20
    blkrect(250,485,265,700,win)# 21
    blkrect(320,485,930,500,win)# 22
    blkrect(320,485,335,700,win)# 23
    blkrect(320,685,850,700,win)# 24
    blkrect(835,550,850,700,win)# 25
    blkrect(550,550,835,565,win)# 26


    #_______button_____
    buttoncolour = Rectangle(Point(80, 140), Point(130, 190))
    buttoncolour.setFill('red')
    buttoncolour.draw(win)
    middlebutton = Circle(Point(105,165),(12))
    middlebutton.setFill('black')
    middlebutton.draw(win)

    #__door___
    doorr = Rectangle(Point(920, 900), Point(935, 985))
    doorr.setFill('red')
    doorr.draw(win)
    #_________
    doorbit = Rectangle(Point(925,910), Point(930,975))#|door bit
    doorbit.setFill('black')
    doorbit.draw(win)
    
    player = Image(Point(40,965), "BlockRight.png")
    player.draw(win)

    playerpoint = [40,965]
    listobby = {'1':[0,0,15,1000],'2':[0,985,1000,1000],'3':[985,0,1000,1000],'4':[0,0,1000,15],'5':[920,0,935,900],'6':[65,60,80,1000],'7':[80,60,850,75],'8':[80,400,500,415],'9':[920,400,550,415],'10':[485,125,500,415],'11':[300,125,485,140],
                '12':[70,125,250,140],'13':[235,140,250,350],'14':[300,140,315,350],'15':[300,350,400,365],'16':[385,200,400,365],'17':[130,885,920,900],'18':[70,800,870,815],'19':[130,500,145,815],'20':[130,485,250,500],'21':[250,485,265,700],
                '22':[320,485,930,500],'23':[320,485,335,700],'24':[320,685,850,700],'25':[835,550,850,700],'26':[550,550,835,565]}
    button = [80,140,130,190]
    door = [920,900,935,985]
    end_space = [935,15,985,65]
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
            maze3()
            break  # Quit the program if '/' is pressed
        elif ifin(end_space,playerpoint[0],playerpoint[1]) == True:
            win.close()
            congrats2()
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

    player = Image(Point(35,475), "BlockDown.png")
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
            maze4()
            break  # Quit the program if '/' is pressed
        elif ifin(end_space,playerpoint[0],playerpoint[1]) == True:
            win.close()
            congrats3()
            fake_end()
            maze4()
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

def congrats3():
    win = GraphWin('You Won', 1000, 1000)
    line(500,800,20,"Click to continue",win)
    line(500,200,35,"Congradulation",win)
    line(500,400,25,"you completed maze 3",win)
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

def maze4():
    win = GraphWin('Maze 4', 1000, 1000)

    start = Rectangle(Point(20,1000), Point(120, 900))
    start.setFill("Light Green")
    start.draw(win)
    blkrect(0,0,1000,20,win)# 1
    blkrect(120,980,1000,1000,win)# 2
    blkrect(0,0,20,1000,win)# 3
    blkrect(980,0,1000,1000,win)# 4
    blkrect(120,1000,140,120,win)# 5
    blkrect(140,120,880,140,win)# 6
    blkrect(880,140,860,880,win)# 7
    blkrect(860,880,240,860,win)# 8
    blkrect(240,860,260,240,win)# 9
    blkrect(260,240,760,260,win)# 10
    blkrect(760,260,740,760,win)# 11
    blkrect(740,760,360,740,win)# 12
    blkrect(480,480,740,520,win)# 13
    fake_end = Rectangle(Point(640, 520), Point(740, 620))
    fake_end.setFill("maroon")
    fake_end.draw(win)

    end = Rectangle(Point(640, 380), Point(740, 480))
    end.setFill("red")
    end.draw(win)

    player = Image(Point(70,950), "BlockUp.png")
    player.draw(win)

    listobby = {'1':[0,0,1000,20],'2':[120,980,1000,1000],'3':[0,0,20,1000],'4':[980,0,1000,1000],
                '5':[120,120,140,1000],'6':[140,120,880,140],'7':[860,140,880,880],'8':[240,860,860,880],'9':[240,240,260,860],
                '10':[260,240,760,260],'11':[740,260,760,760],'12':[360,740,740,760],
                '13':[480,480,740,520]}
    end_space = [640,380,740,480]
    fake_end = [640,520,740,620]
    playerpoint = [70,950]
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
            win.close()
            congrats4()
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

def congrats4():

    win = GraphWin('You Won', 1000, 1000)
    line(500,200,30,"Congradulation",win)
    line(500,400,20,"you completed maze 4",win)
    line(500,800,10,"Click to continue",win)

    win.getMouse() # pause for click in window 
    win.close()

def won():
    win = GraphWin('You Won', 1000, 1000)
    line(500,200,30,"Congradulation",win)
    line(500,400,20,"You have beaten the game,",win)

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