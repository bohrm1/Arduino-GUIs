from tkinter import *
import serial
import time

root = Tk()
ser = serial.Serial('COM3', baudrate=9600, timeout=1)    #initializing serial comms
time.sleep(3)			

#clicking the button while cause the string inside of the entry box to be 
#written to the serial port.

def buttonClick():    			
	angle = angleEntry.get()     #getting string inside entry box 
	ser.write(angle.encode())    #writing this angle to serial port 

#creating box where you type angle for servo 
angleEntry = Entry(root, width = 50, bg = "pink")
angleEntry.grid(row=0, column=1)

#creating label for angle 
servoLabel = Label(root, text = "Angle:")
servoLabel.grid(row=0, column=0)

#creating button that calls buttonClick function when pressed. 
setAngle = Button(root, text = "Set Servo Angle", padx=20, pady=10, command=buttonClick)
setAngle.grid(row=1, column=1)


root.mainloop()

