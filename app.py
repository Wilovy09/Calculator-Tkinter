#import parser
from tkinter import *

root=Tk()
root.title("Calculator")

display=Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

i=0
def get_number(n):
    global i
    display.insert(i,n)
    i+=1

def get_operation(operator):
    global i
    operator_length=len(operator)
    display.insert(i, operator)
    i+=operator_length

def clear_display():
    display.delete(0, END)

def undo():
    display_state=display.get()
    if len(display_state):
        display_new_state=display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, 'ERROR')
"""
def calculate():
    display_state=display.get()
    try:
        math_expression=parser.expr(display_state).compile()
        result=eval(math_expression)
        clear_display
        display.insert(0, result)
    except expression as identifier:
        clear_display()
        display.insert(0, 'ERROR')
"""
#? Numeric buttons
Button(root,text="1", command=lambda:get_number(1)).grid(row=2,column=0, sticky=W+E)
Button(root,text="2", command=lambda:get_number(2)).grid(row=2,column=1, sticky=W+E)
Button(root,text="3", command=lambda:get_number(3)).grid(row=2,column=2, sticky=W+E)

Button(root,text="4", command=lambda:get_number(4)).grid(row=3,column=0, sticky=W+E)
Button(root,text="5", command=lambda:get_number(5)).grid(row=3,column=1, sticky=W+E)
Button(root,text="6", command=lambda:get_number(6)).grid(row=3,column=2, sticky=W+E)

Button(root,text="7", command=lambda:get_number(7)).grid(row=4,column=0, sticky=W+E)
Button(root,text="8", command=lambda:get_number(8)).grid(row=4,column=1, sticky=W+E)
Button(root,text="9", command=lambda:get_number(9)).grid(row=4,column=2, sticky=W+E)

Button(root,text="0", command=lambda:get_number(0)).grid(row=5,column=0, sticky=W+E)

#? Operations Buttons
Button(root,text="AC",command=lambda:clear_display()).grid(    row=5,column=1, sticky=W+E)

Button(root,text="%", command=lambda:get_operation("%")).grid(     row=5,column=2, sticky=W+E)
Button(root,text="+", command=lambda:get_operation("+")).grid(     row=2,column=3, sticky=W+E)
Button(root,text="-", command=lambda:get_operation("-")).grid(     row=3,column=3, sticky=W+E)
Button(root,text="*", command=lambda:get_operation("*")).grid(     row=4,column=3, sticky=W+E)
Button(root,text="/", command=lambda:get_operation("/")).grid(     row=5,column=3, sticky=W+E)

Button(root,text="←",   command=lambda:undo()).grid(     row=2,column=4, sticky=W+E, columnspan=2)
Button(root,text="exp", command=lambda:get_operation("**")).grid(      row=3,column=4, sticky=W+E)
Button(root,text="^2",  command=lambda:get_operation("**2")).grid(     row=3,column=5, sticky=W+E)
Button(root,text="(",   command=lambda:get_operation("(")).grid(       row=4,column=4, sticky=W+E)
Button(root,text=")",   command=lambda:get_operation(")")).grid(       row=4,column=5, sticky=W+E)

# Button(root,text="=", command=lambda:calculate()).grid(     row=5,column=4, sticky=W+E, columnspan=2)
Button(root,text="=").grid(     row=5,column=4, sticky=W+E, columnspan=2)


root.mainloop()