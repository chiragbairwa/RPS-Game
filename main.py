from tkinter import *
from random import *
root = Tk()
root.geometry('266x230')
root.title("Rock Paper Scissor")

words = ["Rock" , "Paper" , "Scissor"]

def click( _num ):    
    if _num == 1:
        contain = words[ randint(0,2) ]
        lbl1 = Label(root, text="Your choice: Rock")
        lbl2 = Label(root, text="PC choice  :" + contain)
        lbl1.grid(row = 4)
        lbl2.grid(row = 5)

        if contain == "Rock":
            result = Label(root, text="*Its A DRAW*")
            result.grid(row = 6,column = 1)

        if contain == "Paper":
            result = Label(root, text="*You WON*")
            result.grid(row = 6,column = 1)
            
        if contain == "Scissor":
            result = Label(root, text="*You LOSE*")
            result.grid(row = 6,column = 1)

    if _num == 2:
        contain = words[ randint(0,2) ]
        lbl1 = Label(root, text="Your choice: Paper")
        lbl2 = Label(root, text="PC  choice :" + contain)
        lbl1.grid(row = 4)
        lbl2.grid(row = 5)

        if contain == "Rock":
            result = Label(root, text="*You WON*")
            result.grid(row = 6,column = 1)

        if contain == "Paper":
            result = Label(root, text="*Its A DRAW*")
            result.grid(row = 6,column = 1)
            
        if contain == "Scissor":
            result = Label(root, text="*You LOSE*")
            result.grid(row = 6,column = 1)
            
    if _num == 3:
        contain = words[ randint(0,2) ]
        lbl1 = Label(root, text="Your choice: Scissor")
        lbl2 = Label(root, text="PC  choice :" + contain)
        lbl1.grid(row = 4)
        lbl2.grid(row = 5)

        if contain == "Rock":
            result = Label(root, text="*You LOSE*")
            result.grid(row = 6,column = 1)

        if contain == "Paper":
            result = Label(root, text="*You WON*")
            result.grid(row = 6,column = 1)
            
        if contain == "Scissor":
            result = Label(root, text="*Its A DRAW*")
            result.grid(row = 6,column = 1)

#BUTTONS
bt1 = Button(root, text= "  Rock ", padx=30.5, pady=10, bg="red",   command=lambda:click(1) )
bt2 = Button(root, text= " Paper ", padx=30, pady=10, bg="green", command=lambda:click(2) )
bt3 = Button(root, text= "Scissor", padx=30, pady=10, bg="blue",  command=lambda:click(3) )

bt1.grid(row = 0)
bt2.grid(row = 1)
bt3.grid(row = 2)

root.mainloop()
