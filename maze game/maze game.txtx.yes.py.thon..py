import random

from graphics import *

win = GraphWin('Maze', 500, 500) # size of game window
win.setBackground('white')
playerx = 50
playery = 450
def blkrect(x1,y1,x2,y2):
    rect = Rectangle(Point(x1,y1), Point(x2,y2))
    rect.setFill('black')
    rect.draw(win)

def main():
    

# IDE: Integrated Development Environment - In our case this is IDLE.
# Note the indentation. In python this is VERY important.



    maze1()
    while True:
        movement()


def maze1():
    # green box to indicate the start
    
    # Text to indicate the end
    end = Text(Point(450,15),'End')
    end.draw(win)

    # First vertical line. Note, you can call the variables anything you want - except reserved words.
    vert1 = Rectangle(Point(0,0), Point(25,450))
    vert1.setFill('black')
    vert1.draw(win)

    # horizontal line
    horizon1 = Rectangle(Point(75,500), Point(500, 450))
    horizon1.setFill('black')
    horizon1.draw(win)

    #vertical 2 yay    bottomleft     topright
    vert2 = Rectangle(Point(75,500), Point(100,75))
    vert2.setFill('black')
    vert2.draw(win)

    #horizontal but roof
    roof = Rectangle(Point(0, 0), Point(425, 25))
    roof.setFill('black')
    roof.draw(win)

    #horizontal gap vert2
    joinvert2 = Rectangle(Point(150,75), Point(300,100))
    joinvert2.setFill('black')
    joinvert2.draw(win)

    #vert corner part
    cornervert = Rectangle(Point(300,100), Point(325,0))
    cornervert.setFill('black')
    cornervert.draw(win)

    #little hori
    horiguy = Rectangle(Point(100,150), Point(200,175))
    horiguy.setFill('black')
    horiguy.draw(win)

    #continue lil hori
    horiguy2 = Rectangle(Point(250, 150), Point(375, 175))
    horiguy2.setFill('black')
    horiguy2.draw(win)

    #vert finish deadend
    deadvert = Rectangle(Point(375, 175), Point(425, 0))
    deadvert.setFill('black')
    deadvert.draw(win)

    #button
    deadex = Rectangle(Point(325, 50), Point(375, 0))
    deadex.setFill('red')
    deadex.draw(win)
    
    #hori for fork
    blkrect(150,225,325,250)
    #split deadend down vert
    blkrect(375,175,425,400)
    #vert down middle to deadend2
    blkrect(300,225,325,400)
    #horiz for end of deadend
    blkrect(150,375,400,400)
    #hori pathway S
    blkrect(100,300,250,325)
    #reddoor
    deadex = Rectangle(Point(350, 450), Point(375, 400))
    deadex.setFill('red')
    deadex.draw(win)
    blkrect(360,410,365,440)
    blkrect(475,0,500,500)

    player = Circle(Point(playerx,playery), 20)
    player.setFill("blue")
    player.draw(win)
    
def ifdrawplayerx(num):
    if Point((playerx + num),y).getObject().config["fill"] != "#000000":
            playerx = playerx + num
            player.undraw(win)
            player = Circle(Point(playerx,playery), 20)
            player.setFill("blue")
            player.draw(win)
def ifdrawplayery(num):
    if Point((playery + num),y).getObject().config["fill"] != "#000000":
            playery = playery + num
            player.undraw(win)
            player = Circle(Point(playerx,playery), 20)
            player.setFill("blue")
            player.draw(win)
#def movement():
   # if keyboard.is_pressed("left"):
     #   ifdrawplayerx(25)
            
            
  #  if keyboard.is_pressed("right"):

   # elif keyboard.is_pressed("up"):
     #   ifdrawplayery(-25)

  #  if keyboard.is_pressed("down"):




    


main()
