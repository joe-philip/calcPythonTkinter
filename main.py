from tkinter import *
import table as tables
<<<<<<< HEAD
=======

>>>>>>> 626e853fcf8e724cd2dba7f7c9d3df16976db6f7

def listener(event):
    if "0123456789".find(event.char) != -1:
        numClick(int(event.char))
    elif event.char == ".":
        otherFunctions(3)
    elif "+-/*".find(event.char) != -1:
        operator(int("+-/*".find(event.char)))
    elif event.char == '\r':
        equals()
    elif event.char == '\x08':
        otherFunctions(1)
    elif event.char == '\x7f':
        otherFunctions(2)
    elif event.char == '\x1b':
        root.destroy()
    elif event.char == 'm':
        otherFunctions(4)


def defineRoot():
    root.geometry("400x430")
    root.configure(padx=25, pady=25)
    root.resizable(False, False)  # disables resizing of window
    root.configure(bg="#fff")
    root.title(appTitle)
    root.bind("<KeyPress>", listener)  # listens to keypress
    photo = PhotoImage(file="Icons/1.png")  # Defining Icon picture
    root.iconphoto(False, photo)  # adding Icon
    windowPosition(root)


def createAndDefineLabels():
    # <<<===Number Label===>>>
    global labelText
    global numberLabel
    labelText = StringVar(root)
    numberLabel = Label(root, textvariable=labelText, bg="#fff", font=('Helvetica', 14))
    numberLabel.configure(anchor=W, pady=25)
    labelText.set(welcomeText)
    numberLabel.grid(row=0, column=0, columnspan=3, rowspan=3, sticky=W)
    # the sticky attribute sets the text to the left side of label
    # <<<===Operator===>>>
    global operatorDisplay
    operatorDisplay = StringVar(root)
    operatorLabel = Label(root, textvariable=operatorDisplay, bg="#fff", font=('Helvetica', 14))
    operatorLabel.configure(anchor=E)
    operatorLabel.grid(row=0, column=4, rowspan=3, sticky=E)
    # <<<===Menu===>>>
    clearLabel = Label(root, text="Clear -->", bg="#fff")
    clearLabel.grid(row=9, column=0, padx=2, pady=2, sticky=E)
    backspace = Label(root, text="Backspace", bg="#fff")
    backspace.grid(row=9, column=1, padx=2, pady=2, sticky=W)
    deleteAllLabel = Label(root, text="Delete All -->", bg="#fff")
    deleteAllLabel.grid(row=10, column=0, padx=2, pady=2, sticky=E)
    deleteLabel = Label(root, text="Delete", bg="#fff")
    deleteLabel.grid(row=10, column=1, padx=2, pady=2, sticky=W)
    equalsLabel = Label(root, text="Equals-->", bg="#fff")
    equalsLabel.grid(row=11, column=0, padx=2, pady=2, sticky=E)
    enterLabel = Label(root, text="Enter", bg="#fff")
    enterLabel.grid(row=11, column=1, padx=2, pady=2, sticky=W)


def windowPosition(name):  # positions window to the center of the screen
    name.update_idletasks()
    width = name.winfo_width()
    height = name.winfo_height()
    x = (name.winfo_screenwidth() // 2) - (width // 2)
    y = (name.winfo_screenheight() // 2) - (height // 2)
    name.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def createAndAllignButtons():
    # <<<===Num Buttons===>>>
    button1 = Button(root, text="1", command=lambda: numClick(1), bg="#fff", border=0, width=3, height=2)
    button1.grid(row=6, column=0, padx=25)
    button2 = Button(root, text="2", command=lambda: numClick(2), bg="#fff", border=0, width=3, height=2)
    button2.grid(row=6, column=1, padx=25)
    button3 = Button(root, text="3", command=lambda: numClick(3), bg="#fff", border=0, width=3, height=2)
    button3.grid(row=6, column=2, padx=25)
    button4 = Button(root, text="4", command=lambda: numClick(4), bg="#fff", border=0, width=3, height=2)
    button4.grid(row=5, column=0, padx=25)
    button5 = Button(root, text="5", command=lambda: numClick(5), bg="#fff", border=0, width=3, height=2)
    button5.grid(row=5, column=1, padx=25)
    button6 = Button(root, text="6", command=lambda: numClick(6), bg="#fff", border=0, width=3, height=2)
    button6.grid(row=5, column=2, padx=25)
    button7 = Button(root, text="7", command=lambda: numClick(7), bg="#fff", border=0, width=3, height=2)
    button7.grid(row=4, column=0, padx=25)
    button8 = Button(root, text="8", command=lambda: numClick(8), bg="#fff", border=0, width=3, height=2)
    button8.grid(row=4, column=1, padx=25)
    button9 = Button(root, text="9", command=lambda: numClick(9), bg="#fff", border=0, width=3, height=2)
    button9.grid(row=4, column=2, padx=25)
    button0 = Button(root, text="0", command=lambda: numClick(0), bg="#fff", border=0, width=3, height=2)
    button0.grid(row=7, column=1, padx=25)
    # the value of the button clicked is passed onto a single function as argument
    # <<<===Operators===>>>
    buttonPlus = Button(root, text="+", command=lambda: operator(0), bg="#fff", border=0, width=3, height=2)
    buttonPlus.grid(row=6, column=3, pady=2)
    buttonMinus = Button(root, text="-", command=lambda: operator(1), bg="#fff", border=0, width=3, height=2)
    buttonMinus.grid(row=5, column=3, pady=2)
    buttonDivide = Button(root, text=chr(247), command=lambda: operator(2), bg="#fff", border=0, width=3, height=2)
    buttonDivide.grid(row=4, column=3, pady=2)
    buttonMultiply = Button(root, text="x", command=lambda: operator(3), bg="#fff", border=0, width=3, height=2)
    buttonMultiply.grid(row=7, column=3, pady=2)
    # <<<===Other Functions===>>>
    clearButton = Button(root, text="C", command=lambda: otherFunctions(1), bg="#fff", border=0, width=3, height=2)
    clearButton.grid(row=8, column=0)
    equalsButton = Button(root, text="=", command=equals, bg="#fff", border=0, width=3, height=2)
    equalsButton.grid(row=7, column=2)
<<<<<<< HEAD
    clearAllButton = Button(root, text="Clear\nAll", command=lambda: otherFunctions(2), bg="#fff", border=0, width=5,
=======
    clearAllButton = Button(root, text="Clear\nAll", command=lambda: otherFunctions(2), bg="#fff", border=0, width=3,
>>>>>>> 626e853fcf8e724cd2dba7f7c9d3df16976db6f7
                            height=2)
    clearAllButton.grid(row=8, column=1, pady=2)
    dotButton = Button(root, text=".", command=lambda: otherFunctions(3), bg="#fff", border=0, width=3, height=2)
    dotButton.grid(row=7, column=0, pady=2)
<<<<<<< HEAD
    tablesButton = Button(root, text="Tables", command=lambda: otherFunctions(4), bg="#fff", border=0, width=3,height=2)
=======
    tablesButton = Button(root, text="Tables", command=lambda: otherFunctions(4), bg="#fff", border=0, width=3,
                          height=2)
>>>>>>> 626e853fcf8e724cd2dba7f7c9d3df16976db6f7
    tablesButton.grid(row=8, column=2, pady=2)


def numClick(n):
    if len(str(numberLabel['text'])) < 11 or numberLabel['text'] == welcomeText:  # checks for overflow
        if isOperatorClicked == 0:  # checks wether operators have been clicked
            if numberLabel['text'] == welcomeText or numberLabel['text'] == "0":  # checks the text in label
                labelText.set(str(n))
            else:
                labelText.set(labelText.get() + str(n))
        else:
            if labelText.get() == "0":
                labelText.set(str(n))
            else:
                labelText.set(labelText.get() + str(n))
    else:
        errormsg("Enter less than 10 numbers")


def operator(op):
    if numberLabel['text'] == welcomeText or labelText.get() == '':
        errormsg("Enter number first")
    else:
        global isOperatorClicked
        isOperatorClicked = 1
        global n1
        n1 = float(numberLabel['text'])
        labelText.set(0)
        global opt
        opt = op
        if op == 0:
            operatorDisplay.set("+")
        elif op == 1:
            operatorDisplay.set("-")
        elif op == 2:
            operatorDisplay.set(chr(247))
        elif op == 3:
            operatorDisplay.set("x")


def equals():
    if numberLabel['text'] == welcomeText:
        errormsg("Invalid Operation")
    else:
        isOperatorClicked = 0
        global n2
        n2 = float(numberLabel['text'])
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
    def close(event):
        error.destroy()

    error = Tk()
    error.bind("<KeyPress>", close)
    error.geometry("200x80")
    error.title("Error")
    error.configure(bg="#fff")
    error.resizable(False, False)
    windowPosition(error)
    errorLabel = Label(error, text=message, bg="#fff")
    errorLabel.pack(pady=10)
    okButton = Button(error, text="OK", command=lambda: error.destroy(), bg="#007aff", fg="#fff", border=0)
    # the destroy() is a built in function it exits the window
    okButton.pack()
    error.mainloop()


def otherFunctions(choice):
    if choice == 1:  # delete button
        if len(labelText.get()) > 1 and labelText.get() != welcomeText:
            labelText.set(labelText.get()[:-1])
        elif len(labelText.get()) == 1:
            labelText.set("0")
        else:
            errormsg("Nothing to delete")
    elif choice == 2:  # clear all
        n1 = n2 = 0
        labelText.set(welcomeText)
        res = 0
        opt = 0
        global isOperatorClicked
        isOperatorClicked = 0
        operatorDisplay.set("")
    elif choice == 3:  # dot button
        if labelText.get().find('.') == -1:  # checks wether dot is already present in the number
            if labelText.get() == welcomeText or labelText.get() == "0" or labelText.get() == "0.":
                labelText.set("0.")
            else:
                labelText.set((labelText.get()) + ".")
        else:
            errormsg("Invalid choice")
    elif choice == 4:  # Multiplication Table
        tables.create()


# <<<===Initializations===>>>
welcomeText = "Welcome to the calculator app"
appTitle = "Calculator"
isOperatorClicked = 0
# <<<===Main===>>>
root = Tk()
defineRoot()
createAndDefineLabels()
createAndAllignButtons()
root.mainloop()
