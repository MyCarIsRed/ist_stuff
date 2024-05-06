import random

from graphics import *

def main():
    

# IDE: Integrated Development Environment - In our case this is IDLE.
# Note the indentation. In python this is VERY important.
    
    title()
    movement()
    maze1()
    congrats1()
    button()
    maze2()
    maze3()
    
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
    
def movement():
    win = GraphWin('Instructions', 500, 500)
    win.setBackground('white')
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
    start = Rectangle(Point(0,500), Point(50, 450))
    start.setFill("Light Green")
    start.draw(win)
    # Text to indicate the end
    end = Rectangle(Point(450,50), Point(500, 0))
    end.setFill("Red")
    end.draw(win)
    # First vertical line. Note, you can call the variables anything you want - except reserved words.
    vert1 = Rectangle(Point(0,0), Point(25,450))
    vert1.setFill('black')
    vert1.draw(win)
    
    w = Rectangle(Point(0,0), Point(450, 25))
    w.setFill('black')
    w.draw(win)
    
    vert = Rectangle(Point(25,450), Point(350, 400))
    vert.setFill('black')
    vert.draw(win)
    
    ww = Rectangle(Point(150,150), Point(500, 250))
    ww.setFill('black')
    ww.draw(win)
    
    wwa = Rectangle(Point(0,20), Point(450, 100))
    wwa.setFill('black')
    wwa.draw(win)
    # Player model
    pelayer = Circle(Point(475, 50), 5)
    pelayer.setFill("navy")
    pelayer.draw(win)
    player = Circle(Point(25, 475), 15)
    playercoordx = 25
    playercoordy = 475
    player.setFill("navy")
    player.draw(win)
    # Movement functions
    yes = getPixel(0,0)
    print(yes)
    while True:
        key = win.checkKey()

        if key == "w" or key == "Up":
            player.move(0, -10)  # Move up
        elif key == "a" or key == "Left":
            player.move(-10, 0)  # Move left
        elif key == "s" or key == "Down":
            player.move(0, 10)   # Move down
        elif key == "d" or key == "Right":
            player.move(10, 0)   # Move right
        elif key == "p":
            break  # Quit the program if '/' is pressed
    win.close()

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

def button():
    win = GraphWin('Instruction', 500, 500)
    tital = Text(Point(250, 100), "Instructions")
    tital.setSize(30)
    tital.draw(win)
    h = Text(Point(250,250),'In this level you will encounter buttons')
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


    
main()
