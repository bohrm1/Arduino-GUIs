from tkinter import *
import serial
import time

ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)  #initialzing comm port 
time.sleep(3) #halting program three second before continuing 

root = Tk()


def onClick():			#sending 'h' for HIGH over comm bus if onClick is pressed
	ser.write(b'h')
def offClick(): 
	ser.write(b'l')     #sending 'l' for LOW over comm bus if offClick is pressed 

onButton = Button(root, text = "LED On", padx=50, pady=50, command=onClick)    #on button
offButton = Button(root, text = "LED Off", padx=50, pady=50, command=offClick) #off button

onButton.pack()      #putting onButton onto screen
offButton.pack() 	 #putting ofButton onto screen. 

root.mainloop()			

