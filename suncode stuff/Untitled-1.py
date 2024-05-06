from graphics import*
import random

def main():
    win = GraphWin("Landscape", 1200, 730)
    win.setBackground("lightskyblue") #sky

#sun
    sun = Circle(Point(1200, 0), 120) 
    sun.draw(win)
    sun.setFill("gold")
    sun.setOutline("gold")
    
#sun rays
    ray1 = Line(Point(1200,0), Point(1050, 150)) 
    ray1.draw(win)
    ray1.setOutline("gold")
    ray1.setWidth(15)
    ray2 = Line(Point(1200,0), Point(1185, 200))
    ray2.draw(win)
    ray2.setOutline("gold")
    ray2.setWidth(15)
    ray3 = Line(Point(1200,0), Point(1000, 15)) 
    ray3.draw(win)
    ray3. setOutline("gold")
    ray3.setWidth(15)

main()