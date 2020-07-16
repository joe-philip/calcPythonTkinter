from tkinter import *


def createAndAllignNumButtons():
    button1 = Button(root, text="1", command=lambda: numClick(1), bg="#fff").grid(row=6, column=0)
    button2 = Button(root, text="2", command=lambda: numClick(2), bg="#fff").grid(row=6, column=1)
    button3 = Button(root, text="3", command=lambda: numClick(3), bg="#fff").grid(row=6, column=2)
    button4 = Button(root, text="4", command=lambda: numClick(4), bg="#fff").grid(row=5, column=0)
    button5 = Button(root, text="5", command=lambda: numClick(5), bg="#fff").grid(row=5, column=1)
    button6 = Button(root, text="6", command=lambda: numClick(6), bg="#fff").grid(row=5, column=2)
    button7 = Button(root, text="7", command=lambda: numClick(7), bg="#fff").grid(row=4, column=0)
    button8 = Button(root, text="8", command=lambda: numClick(8), bg="#fff").grid(row=4, column=1)
    button9 = Button(root, text="9", command=lambda: numClick(9), bg="#fff").grid(row=4, column=2)
    button0 = Button(root, text="0", command=lambda: numClick(0), bg="#fff").grid(row=7, column=1)
    # the value of the button clicked is passed onto a single function as argument


def createAndAllignOperatorButtons():
    buttonPlus = Button(root, text="+", command=lambda: operator(0), bg="#fff").grid(row=6, column=3)
    buttonMinus = Button(root, text="-", command=lambda: operator(1), bg="#fff").grid(row=5, column=3)
    buttonDivide = Button(root, text="/", command=lambda: operator(2), bg="#fff").grid(row=4, column=3)
    buttonMultiply = Button(root, text="x", command=lambda: operator(3), bg="#fff").grid(row=7, column=3)


def createAndAllignFunctionButtons():
    clearButton = Button(root, text="C", command=lambda: otherFunctions(1), bg="#fff").grid(row=7, column=0)
    equalsButton = Button(root, text="=", command=equals, bg="#fff").grid(row=7, column=2)


def numClick(n):
    if isOperatorClicked == 0:  # checks wether operators have been clicked
        if label['text'] == welcomeText:  # checks the text in label
            labelText.set(str(n))
        else:
            labelText.set(labelText.get() + str(n))
    else:
        if label['text'] == 0:
            labelText.set(str(n))
        else:
            labelText.set(labelText.get() + str(n))


def operator(op):
    if label['text'] == welcomeText:
        errormsg("Enter message first")
    else:
        global isOperatorClicked
        isOperatorClicked = 1
        global n1
        n1 = float(label['text'])
        labelText.set(0)
        global opt
        opt = op


def equals():
    if label['text'] == welcomeText:
        errormsg("Invalid Operation")
    else:
        isOperatorClicked = 0
        global n2
        n2 = float(label['text'])
        if (opt == 0):
            res = n1 + n2
        elif (opt == 1):
            res = n1 - n2
        elif (opt == 2):
            if n2 == 0:
                errormsg("Division by zero not possible")
        elif (opt == 3):
            res = n1 * n2
        if res % 1 == 0:
            labelText.set(str(int(res)))
        else:
            labelText.set(str(res))


def errormsg(message):
    error = Tk()
    errorLabel = Label(error, text=message)
    errorLabel.pack()
    error.mainloop()


def otherFunctions(choice):
    return


welcomeText = "Welcome to the calculator app"
appTitle = "Calculator"
isOperatorClicked = 0
root = Tk()
labelText = StringVar(root)
root.title(appTitle)
root.configure(bg="#fff")
label = Label(root, textvariable=labelText)
labelText.set(welcomeText)
label.grid(row=0, column=0, columnspan=4, rowspan=3)
createAndAllignNumButtons()
createAndAllignOperatorButtons()
createAndAllignFunctionButtons()
root.mainloop()
