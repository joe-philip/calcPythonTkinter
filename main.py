from tkinter import *
from _tkinter import *


def windowPosition(name):  # positions window to the center of the screen
    name.update_idletasks()
    width = name.winfo_width()
    height = name.winfo_height()
    x = (name.winfo_screenwidth() // 2) - (width // 2)
    y = (name.winfo_screenheight() // 2) - (height // 2)
    name.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def createAndAllignNumButtons():
    button1 = Button(root, text="1", command=lambda: numClick(1), bg="#fff", border=0).grid(row=6, column=0)
    button2 = Button(root, text="2", command=lambda: numClick(2), bg="#fff", border=0).grid(row=6, column=1)
    button3 = Button(root, text="3", command=lambda: numClick(3), bg="#fff", border=0).grid(row=6, column=2)
    button4 = Button(root, text="4", command=lambda: numClick(4), bg="#fff", border=0).grid(row=5, column=0)
    button5 = Button(root, text="5", command=lambda: numClick(5), bg="#fff", border=0).grid(row=5, column=1)
    button6 = Button(root, text="6", command=lambda: numClick(6), bg="#fff", border=0).grid(row=5, column=2)
    button7 = Button(root, text="7", command=lambda: numClick(7), bg="#fff", border=0).grid(row=4, column=0)
    button8 = Button(root, text="8", command=lambda: numClick(8), bg="#fff", border=0).grid(row=4, column=1)
    button9 = Button(root, text="9", command=lambda: numClick(9), bg="#fff", border=0).grid(row=4, column=2)
    button0 = Button(root, text="0", command=lambda: numClick(0), bg="#fff", border=0).grid(row=7, column=1)
    # the value of the button clicked is passed onto a single function as argument


def createAndAllignOperatorButtons():
    buttonPlus = Button(root, text="+", command=lambda: operator(0), bg="#fff", border=0).grid(row=6, column=3)
    buttonMinus = Button(root, text="-", command=lambda: operator(1), bg="#fff", border=0).grid(row=5, column=3)
    buttonDivide = Button(root, text="/", command=lambda: operator(2), bg="#fff", border=0).grid(row=4, column=3)
    buttonMultiply = Button(root, text="x", command=lambda: operator(3), bg="#fff", border=0).grid(row=7, column=3)


def createAndAllignFunctionButtons():
    clearButton = Button(root, text="C", command=lambda: otherFunctions(1), bg="#fff", border=0).grid(row=8, column=0)
    equalsButton = Button(root, text="=", command=equals, bg="#fff", border=0).grid(row=7, column=2)
    clearAllButton = Button(root, text="Clear All", command=lambda: otherFunctions(2), bg="#fff", border=0).grid(row=8,
                                                                                                                 column=1)
    dotButton = Button(root, text=".", command=lambda: otherFunctions(3), bg="#fff", border=0).grid(row=7, column=0)


def numClick(n):
    if isOperatorClicked == 0:  # checks wether operators have been clicked
        if label['text'] == welcomeText or label['text'] == "0":  # checks the text in label
            labelText.set(str(n))
        else:
            labelText.set(labelText.get() + str(n))
    else:
        if labelText.get() == "0":
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
        if opt == 0:
            res = n1 + n2
        elif opt == 1:
            res = n1 - n2
        elif opt == 2:
            if n2 == 0:
                errormsg("Division by zero not possible")
            else:
                res = n1 / n2
        elif opt == 3:
            res = n1 * n2
        if res % 1 == 0:
            labelText.set(str(int(res)))
        else:
            labelText.set(str(res))


def errormsg(message):
    def exit():
        error.destroy()

    error = Tk()
    error.title("Error")
    error.configure(bg="#fff")
    windowPosition(error)
    errorLabel = Label(error, text=message, bg="#fff")
    errorLabel.pack()
    okButton = Button(error, text="OK", command=exit, bg="#007aff", fg="#fff", border=0)
    okButton.pack()
    error.mainloop()


def otherFunctions(choice):
    if choice == 1:  # delete button
        if len(labelText.get()) > 0:
            labelText.set(labelText.get()[:-1])
        else:
            errormsg("Nothing to delete")
    elif choice == 2:
        n1 = n2 = 0
        labelText.set(welcomeText)
        res = 0
        opt = 0
    elif choice==3:
        if labelText.get()==welcomeText or labelText.get()=="0":
            labelText.set("0.")
        else:
            labelText.set((labelText.get())+".")

    return


welcomeText = "Welcome to the calculator app"
appTitle = "Calculator"
isOperatorClicked = 0
root = Tk()
root.geometry("300x300")
windowPosition(root)
labelText = StringVar(root)
root.title(appTitle)
root.configure(bg="#fff")
label = Label(root, textvariable=labelText, bg="#fff", font=('Helvetica', 14))
label.configure(anchor=W)
labelText.set(welcomeText)
label.grid(row=0, column=0, columnspan=4, rowspan=3)
createAndAllignNumButtons()
createAndAllignOperatorButtons()
createAndAllignFunctionButtons()
root.mainloop()
