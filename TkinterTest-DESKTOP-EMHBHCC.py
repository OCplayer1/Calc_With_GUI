#imports tkinter which is used to make GUI and it is named tk to be used
import tkinter as tk
import tkinter.font as font
import time
#this will create a new window
win = tk.Tk()
#this will add a title to the window
win.title("This is the new GUI")
#this sets it so that the GUI is not resizable 
win.resizable(False, False)
#this sets the exact size of the GUI
win.geometry("500x500")

TitleFont = font.Font(size=30)

def Add():
    add1 = Num1.get()
    add2 = Num2.get()

    result = int(add1) + int(add2)
    label = tk.Label(win, text= result)
    label['font'] = TitleFont
    label.place(relx = 0.41, rely = 0.3)
   

def Subtract():
    sub1 = Num1.get()
    sub2 = Num2.get()

    result = int(sub1) - int(sub2)
    label = tk.Label(win, text= result)
    label['font'] = TitleFont
    label.place(relx = 0.41, rely = 0.3)

def Multiply():
    Mult1 = Num1.get()
    Mult2 = Num2.get()

    result = int(Mult1) * int(Mult2)
    label = tk.Label(win, text= result)
    label['font'] = TitleFont
    label.place(relx = 0.41, rely = 0.3)

def Divide():
    Div1 = Num1.get()
    Div2 = Num2.get()

    result = int(Div1) / int(Div2)
    label = tk.Label(win, text= result)
    label['font'] = TitleFont
    label.place(relx = 0.41, rely = 0.3)



FirstLabel = tk.Label(win, text = "Please enter the first number")
SecondLabel = tk.Label(win, text = "Please enter the second number")

FirstLabel.place(relx = 0.175, rely = 0.6)
SecondLabel.place(relx = 0.525, rely = 0.6)

Num1 = tk.Entry(win)
Num2 = tk.Entry(win)

Num1.place(relx = 0.175, rely = 0.7)
Num2.place(relx = 0.525, rely = 0.7)




Title = tk.Label(win, text= "Calculator")
Title['font'] = TitleFont
Title.place(relx = 0.31 , rely = 0.01)

#this creates a button object called button1 with the set config that it is given
buttonAdd = tk.Button(win, text='Add', command = Add, width=20, height=1, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
#adding .pack() to the button will add it to the GUI
buttonAdd.place(relx = 0.15, rely = 0.8)


buttonSub = tk.Button(win, text='Subtract', command = Subtract, width=20, height=1, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
buttonSub.place(relx = 0.5, rely = 0.8)

buttonMult = tk.Button(win, text='Multiply', command = Multiply, width=20, height=1, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
buttonMult.place(relx = 0.15, rely = 0.9)

buttonDiv = tk.Button(win, text='Divide', command = Divide, width=20, height=1, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
buttonDiv.place(relx = 0.5, rely = 0.9)

#this will create the GUI itself it will alwasy need a mainloop
win.mainloop()