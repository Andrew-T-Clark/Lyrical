#Import all those standard libraries
#__________________________
import math
import tkinter
#_____________________

#Define functions
#_______________________________
#Define function to get the input
def GetInput():
    Input = str(entry.get())
#__________________________________

#Create the window and elements
#______________________________________
#Set up application window
window = tkinter.Tk(screenName="Lyrical",  baseName=None,  className="Lyrical",  useTk=1)

#Set the size of the window
window.geometry('500x200') 

#Create imput for problem
typeherelabel = tkinter.Label(window, text="Type Problem Here")
entry = tkinter.Entry(window) 

#Create "solve" button
solvebutton = tkinter.Button(text="Solve",command=GetInput)

#Pack it up
typeherelabel.pack()
entry.pack()
solvebutton.pack()

#Create the main loop
window.mainloop()
#__________________________________
