from tkinter import *


def createAndAllignNumButtons():
    button1 = Button(root, text="1", command=one, bg="#fff").grid(row=6, column=0)
    button2 = Button(root, text="2", command=two, bg="#fff").grid(row=6, column=1)
    button3 = Button(root, text="3", command=three, bg="#fff").grid(row=6, column=2)
    button4 = Button(root, text="4", command=four, bg="#fff").grid(row=5, column=0)
    button5 = Button(root, text="5", command=five, bg="#fff").grid(row=5, column=1)
    button6 = Button(root, text="6", command=six, bg="#fff").grid(row=5, column=2)
    button7 = Button(root, text="7", command=seven, bg="#fff").grid(row=4, column=0)
    button8 = Button(root, text="8", command=eight, bg="#fff").grid(row=4, column=1)
    button9 = Button(root, text="9", command=nine, bg="#fff").grid(row=4, column=2)
    button0 = Button(root, text="0", command=zero, bg="#fff").grid(row=7, column=1)


def createAndAllignOperatorButtons():
    buttonPlus = Button(root, text="+", command=plus, bg="#fff").grid(row=6, column=3)
    buttonMinus = Button(root, text="-", command=minus, bg="#fff").grid(row=5, column=3)
    buttonDivide = Button(root, text="/", command=divide, bg="#fff").grid(row=4, column=3)
    buttonMultiply = Button(root, text="x", command=multiply, bg="#fff").grid(row=7, column=3)


def createAndAllignFunctionButtons():
    clearButton = Button(root, text="C", command=clear, bg="#fff").grid(row=7, column=0)
    dotButton = Button(root, text=".", command=dot, bg="#fff").grid(row=7, column=2)


def one():
    return


def two():
    return


def three():
    return


def four():
    return


def five():
    return


def six():
    return


def seven():
    return


def eight():
    return


def nine():
    return


def zero():
    return


def plus():
    return


def minus():
    return


def multiply():
    return


def divide():
    return


def clear():
    return


def dot():
    return


welcomeText = "Welcome to the calculator app"
root = Tk()
root.configure(bg="#fff")
label = Label(root, text=welcomeText)
label.grid(row=0, column=0, columnspan=4, rowspan=3)
createAndAllignNumButtons()
createAndAllignOperatorButtons()
createAndAllignFunctionButtons()
root.mainloop()
