try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry("320x240-8-200")
mainWindow['padx'] = 8
mainWindow.update()
mainWindow.minsize(mainWindow.winfo_width(), mainWindow.winfo_height())

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nw', columnspan=4)


# cButton = tkinter.Button(mainWindow, text="C")
# cButton.grid(row=1, column=0, sticky='new')
# ceButton = tkinter.Button(mainWindow, text="CE")
# ceButton.grid(row=1, column=1, sticky='new')
calcList = ["C", "CE", "", "", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "0", "=", "=", "/"]
# sevenButton = tkinter.Button(mainWindow, text="7")
# sevenButton.grid(row=2, column=0, sticky='new')
# eightButton = tkinter.Button(mainWindow, text="8")
# eightButton.grid(row=2, column=1, sticky='new')
# nineButton = tkinter.Button(mainWindow, text="9")
# nineButton.grid(row=2, column=2, sticky='new')
# addButton = tkinter.Button(mainWindow, text="+")
# addButton.grid(row=2, column=3, sticky='new')


a = 0
for i in range(1, 6):
    for j in range(0, 4):
        if calcList[a] == "":
            a += 1
            j += 1
            continue
        elif calcList[a] == "=" and calcList[a+1] == "=":
            tkinter.Button(mainWindow, text=calcList[a]).grid(row=i, column=j, sticky='new', columnspan=2)
            a += 1
            j += 1
        elif calcList[a] == "=" and calcList[a+1] != "=":
            a += 1
            j += 1
            continue
        else:
            tkinter.Button(mainWindow, text=calcList[a]).grid(row=i, column=j, sticky='new')
            a += 1
            j += 1
    i += 1


mainWindow.mainloop()
