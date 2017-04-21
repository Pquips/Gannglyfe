from Tkinter import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) 

GPIO.setwarnings(False) 

GPIO.setup(4,GPIO.OUT)

GPIO.setup(17,GPIO.OUT)

GPIO.setup(27,GPIO.OUT)

GPIO.setup(22,GPIO.OUT)

GPIO.setup(9,GPIO.OUT)

GPIO.setup(20,GPIO.OUT)


def keydownq(q):
    GPIO.output(20,GPIO.HIGH)
    
def keyupq(q):
    GPIO.output(20,GPIO.LOW)

def keydownw(w):
    GPIO.output(27,GPIO.HIGH)

def keyupw(w):
    GPIO.output(27,GPIO.LOW)

def keydowne(e):
    GPIO.output(9,GPIO.HIGH)    

def keyupe(e):
   GPIO.output(9,GPIO.LOW)

def keydowni(i):
    GPIO.output(4,GPIO.HIGH)

def keyupi(i):
   GPIO.output(4,GPIO.LOW)
       
def keydowno(o):
    GPIO.output(17,GPIO.HIGH)
    
def keyupo(o):
    GPIO.output(17,GPIO.LOW)

def keydownp(p):
    GPIO.output(22,GPIO.HIGH)
    
def keyupp(p):
    GPIO.output(22,GPIO.LOW)
   




root = Tk()
frame = Frame(root, width=100, height=100)
frame.bind("<KeyPress-q>", keydownq)
frame.bind("<KeyRelease-q>", keyupq)
frame.bind("<KeyPress-w>", keydownw)
frame.bind("<KeyRelease-w>", keyupw)
frame.bind("<KeyPress-e>", keydowne)
frame.bind("<KeyRelease-e>", keyupe)
frame.bind("<KeyPress-i>", keydowni)
frame.bind("<KeyRelease-i>", keyupi)
frame.bind("<KeyPress-o>", keydowno)
frame.bind("<KeyRelease-o>", keyupo)
frame.bind("<KeyPress-p>", keydownp)
frame.bind("<KeyRelease-p>", keyupp)



frame.pack()
frame.focus_set()
root.mainloop()


GPIO.cleanup()

os.system('xset r off')
