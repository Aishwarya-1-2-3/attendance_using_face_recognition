# import turtle

# a=int(input("Enter the side "))
# col=input("Enter the color ")
# tut=turtle.Turtle()
# tut.speed(10)
# tut.fillcolor(col)
# tut.begin_fill()
# for _ in range(4):
#     tut.forward(a)
#     tut.right(90)
# tut.end_fill()
# turtle.done()/
# import pdb 
# def add_mem(a,b):
#     return a+b
# def add_mem(a,b):
#     pdb.set_trace()
#     return a+b
# add_mem(4,5)
from tkinter import *;
expression=""
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)
def equal():
    global expression
    total=str(eval(expression))
    equation.set(total)
    expression=" "
def clear():
    global expression
    expression=" "
    equation.set(" ")
if __name__=="__main__":
    gui=Tk()
    equation=StringVar()
    gui.title("Calculator")
    gui.geometry("270x150")
    gui.configure(background="light green")
gui.mainloop()

