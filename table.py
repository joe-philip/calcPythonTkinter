from tkinter import *

def createAndDisplayTable(n, lnumber, hnumber):
    def destruct(event):
        disp.destroy()
    disp = Tk()
    disp.title("Table")
    disp.configure(bg="#fff")
    disp.resizable(False,False)
    lab = []  # created a list of unknown size
    a = 0
    for i in range(lnumber, hnumber):
        temp = Label(disp, text=str(n) + "x" + str(i) + "=" + str(n * i), bg="#fff",width=25)  # creates a temporary label of unknown size
        lab.append(temp)  # adds the label to the list
        lab[a].pack()  # packs the label
        a += 1
    disp.bind("<KeyPress>",destruct)
    disp.mainloop()


def tableWindow():
    global n
    global lnumber
    global hnumber
    n = int(numText.get())
    lnumber = int(lNumText.get())
    hnumber = int(hNumText.get())
    window.destroy()
    createAndDisplayTable(n, lnumber, hnumber)


def listener(event):
    if event.char == '\x1b':
        window.destroy()
    elif event.char == '\r':
        tableWindow()


def create():
    global window
    window = Tk()
    window.configure(bg="#fff", width="280", height="130", padx=5)
    window.resizable(False,False)
    window.title("Multiplication Table")
    windowPosition(window)
    global numText, lNumText, hNumText
    numText = StringVar(window)
    lNumText = StringVar(window)
    hNumText = StringVar(window)
    num = Entry(window, text=numText, border=0, width=3).grid(row=0, column=1, pady=5, sticky=E)
    numLabel = Label(window, text="Enter the number \t", bg="#fff").grid(row=0, column=0, sticky=W)
    lowerLabel = Label(window, text="Enter the starting Number\t", bg="#fff").grid(row=1, column=0, sticky=W)
    lower = Entry(window, text=lNumText, border=0, width=3).grid(pady=2, row=1, column=1, sticky=E)
    higherLabel = Label(window, text="Enter Max limit\t", border=0, bg="#fff").grid(row=2, column=0, sticky=W)
    higher = Entry(window, text=hNumText, border=0, width=3).grid(row=2, column=1, sticky=E)
    okButton = Button(window, text="OK", border=0, bg="#007aff", fg="#fff", command= tableWindow).grid(row=3, column=0, sticky=SE)
    cancelButton = Button(window, text="Cancel", border=0, bg="#007aff", fg="#fff", command=window.destroy).grid(row=3, column=1, sticky=SW)
    window.bind("<KeyPress>", listener)
    window.mainloop()


def windowPosition(name):  # positions window to the center of the screen
    name.update_idletasks()
    width = name.winfo_width()
    height = name.winfo_height()
    x = (name.winfo_screenwidth() // 2) - (width // 2)
    y = (name.winfo_screenheight() // 2) - (height // 2)
    name.geometry('{}x{}+{}+{}'.format(width, height, x, y))
