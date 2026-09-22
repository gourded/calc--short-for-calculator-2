import tkinter as tk
import math
import numpy as np


sqrt=False
scientificCalc=False
firstTimeScientficCalc=False

#this class holds all the numbers and operators in order to calculate multiple operations strung together
class Calculation:
    def __init__(self):
        self.nums = []
        self.opps = []
    def get_nums(self):
        return self.nums
    def get_opps(self):
        return self.opps
    def add_num(self, num):
        self.nums.append(num)
    def add_opp(self, opp):
        self.opps.append(opp)
    def calculate(self):
        global sqrt
        global scientificCalc
        global firstTimeScientficCalc
        nums = self.nums
        opps = self.opps
        if not nums:
            return 0 
        
        i = 0
        while i < len(opps):
            if opps[i] == '^':
                if "." in str(nums[i+1]):
                    sqrt=True
                if nums[i+1]>=0:

                    nums[i]=nums[i]**(nums[i+1])
                    opps.pop(i)
                    nums.pop(i+1)
                else: 
                    if((1/nums[i])%2==0):
                        nums=[]
                        opps=[]
                    
                        if scientificCalc==False:
                            scientificCalc=True
                            firstTimeScientficCalc=True
                        return  
                    else:
                        nums[i]= -(abs(nums[i+1])**(1/nums[i]))
                        opps.pop(i)
                        nums.pop(i+1)  
            elif opps[i] == '√':
                if nums[i+1]>=0:

                    nums[i]=nums[i+1]**(1/nums[i])
                    opps.pop(i)
                    nums.pop(i+1)
                else: 
                    if(nums[i]%2==0):
                        nums=[]
                        opps=[]
                    
                        if scientificCalc==False:
                            scientificCalc=True
                            firstTimeScientficCalc=True
                        return  
                    else:
                        nums[i]= -(abs(nums[i+1])**(1/nums[i]))
                        opps.pop(i)
                        nums.pop(i+1)  
            else:
                i += 1
        i=0
        while i < len(opps):
            if opps[i] == '*':
               nums[i] *= nums[i + 1]
               nums.pop(i + 1)
               opps.pop(i)
            elif opps[i] == '/':
                nums[i] /= nums[i + 1]
                nums.pop(i + 1)
                opps.pop(i)
            else:
                i += 1
        result = nums[0]
        for j in range(len(opps)):
            if opps[j] == '+':
                result += nums[j + 1]
            elif opps[j] == '-':
                result -= nums[j + 1]
        if result%1==0:
            result=int(result)
        return result
        
    def clear(self):
        self.nums = []
        self.opps = []

#a few global variables
x=0
output=0
operation = Calculation()
canUnlockMult=False
hasDecimal=False
newEquation=True
squared=0
squaring=False

#operation methods
def addition():
    global operation
    global x
    global hasDecimal
    operation.add_opp("+")
    operation.add_num(x)
    x=0
    addToLabel("+")
    hasDecimal=False

def subtraction():
    global operation
    global x
    global hasDecimal
    operation.add_opp("-")
    operation.add_num(x)
    x=0
    addToLabel("-")
    hasDecimal=False


def multiplication():
    global operation
    global x
    global hasDecimal
    operation.add_opp("*")
    operation.add_num(x)
    x=0
    addToLabel("*")
    hasDecimal=False

def division():
    global operation
    global x
    global hasDecimal
    operation.add_opp("/")
    operation.add_num(x)
    x=0
    addToLabel("/")
    hasDecimal=False

def exponent():
    global operation
    global x
    global hasDecimal
    global squaring
    operation.add_opp("^")
    operation.add_num(x)
    x=0
    addToLabel("^")
    hasDecimal=False
    squaring=True

def squareRoot():
    global operation
    global x
    global hasDecimal
    operation.add_opp("√")
    operation.add_num(x)
    x=0
    addToLabel("√")
    hasDecimal=False

def decimal():
    global x
    global hasDecimal
    if hasDecimal==False:
        x2=str(x)
        x2=x2+"."
        x=x2
        addToLabel(".")
        hasDecimal=True

def negative():
    global x
    length = len(str(x))
    x=x*-1

    
    tempText=label.cget("text")
    tempText=tempText[:-length]
    label.config(text=tempText+str(x))


# this one is the equals button
def doIt():
    global x
    global output
    global operation
    global canUnlockMult
    global hasDecimal
    global newEquation
    global firstTimeScientficCalc
    newEquation=True

    multChecker()
    squareChecker()
    operation.add_num(x)
    output=operation.calculate()
    if sqrt==True:
        buttonRoot.config(text="√",command=lambda: squareRoot())
    if firstTimeScientficCalc:
        setLabelText("i")
        output=0
        firstTimeScientficCalc=False
    elif output==None:
        setLabelText("Error")
        output=0
    else:
        setLabelText(str(output))

    x=0
    operation.clear()
    addButton()
    fractionChecker()
    negativeChecker()
    if "." in str(output):
        hasDecimal=True
    else:
        hasDecimal=False

def clear():
    global x
    global output
    global operation
    global hasDecimal
    global newEquation
    hasDecimal=False
    newEquation=True
    x=0
    setLabelText("0")
    operation.clear()

def setNum(num):
    global x
    global newEquation
    if hasDecimal==True:
        x=str(x)
        x=x+str(num)
        x=float(x)
    else:
        x=x*10+num
    if newEquation==True:
        setLabelText(str(num))
        newEquation=False
    elif label.cget("text")=="0":
        setLabelText(str(num))
    else:
        addToLabel(str(num))

#these ones change the label
def setLabelText(text):
    label.config(text=text)
def addToLabel(text):
    label.config(text=label.cget("text")+text)

#these allow buttons to be added and be accesable to the player
def addButton():
    global output
    if output==2:
        button2.config(text="2",command=lambda: setNum(2))
    elif output==3:
        button3.config(text="3",command=lambda: setNum(3))
    elif output==4:
        button4.config(text="4",command=lambda: setNum(4))
    elif output==5:
        button5.config(text="5",command=lambda: setNum(5))
    elif output==6:
        button6.config(text="6",command=lambda: setNum(6))
    elif output==7:
        button7.config(text="7",command=lambda: setNum(7))
    elif output==8:
        button8.config(text="8",command=lambda: setNum(8))
    elif output==9:
        button9.config(text="9",command=lambda: setNum(9))


def multChecker():
    global canUnlockMult
    checkMult=""
    tempOp=operation.get_nums()
    for i in range(len(tempOp)):
        checkMult=f"{tempOp[i]}+{tempOp[i]}+{tempOp[i]}"
        if checkMult in label.cget("text"):
            canUnlockMult=True
    if canUnlockMult==True:
            buttonMultiply.config(text="*",command=lambda: multiplication())
            buttonDivide.config(text="/",command=lambda: division())

def fractionChecker():
    if "." in str(output):
        buttonDecimal.config(text=".",command=lambda: decimal())

def squareChecker():
    global squared
    checkSquare=""
    tempOp=operation.get_nums()
    checkSquare=f"{tempOp[0]}*{tempOp[0]}"
    if checkSquare == label.cget("text"):
        squared+=1
    if squared==5:
        buttonExponent.config(text="x^n",command=lambda: exponent())

def negativeChecker():
    if "-" in str(output):
        buttonNegative.config(text="M-/+", command= lambda: negative())



#this creates the window
root = tk.Tk()
root.title("Calculator")
root.geometry("500x500")

root.rowconfigure(0,weight=0)
root.columnconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.columnconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.columnconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
root.columnconfigure(3,weight=1)
root.rowconfigure(4,weight=1)
root.rowconfigure(5,weight=1)
root.rowconfigure(6,weight=1)

l1=tk.Label(root,text="                    ",height=0)
l2=tk.Label(root,text="                    ",height=0)
l3=tk.Label(root,text="                    ",height=0)
l4=tk.Label(root,text="                    ",height=0)





#the output
label = tk.Label(root, text="",font=("Arial", 24), anchor="w")

# all the number buttons
button1 = tk.Button(root, text="1",command=lambda: setNum(1), font=("Arial", 24))
button2 = tk.Button(root, text="",font=("Arial", 24))
button3 = tk.Button(root, text="", font=("Arial", 24))
button4 = tk.Button(root, text="", font=("Arial", 24))
button5 = tk.Button(root, text="", font=("Arial", 24))
button6 = tk.Button(root, text="", font=("Arial", 24))
button7 = tk.Button(root, text="", font=("Arial", 24))
button8 = tk.Button(root, text="", font=("Arial", 24))
button9 = tk.Button(root, text="", font=("Arial", 24))
button0 = tk.Button(root, text="", font=("Arial", 24))

#all the operator buttons
buttonPlus = tk.Button(root, text="+",command=lambda: addition(), font=("Arial", 24))
buttonMinus = tk.Button(root, text="-",command=lambda: subtraction(), font=("Arial", 24))
buttonMultiply = tk.Button(root, font=("Arial", 24))
buttonDivide = tk.Button(root ,font=("Arial", 24))
buttonEqual = tk.Button(root, text="=",command=lambda: doIt(), font=("Arial", 24))
buttonClear = tk.Button(root, text="C",command=lambda: clear(), font=("Arial", 24))
buttonDecimal = tk.Button(root ,font=("Arial", 24))
#buttonAnswer = tk.Button(root, text="Ans",command=lambda: setNum(output), font=("Arial", 24))
buttonExponent = tk.Button(root, text="" ,font=("Arial", 24))
buttonRoot = tk.Button(root, text="" ,font=("Arial", 24))
buttonNegative=tk.Button(root, text="" ,font=("Arial",24))

#allaigns everything to a grid
l1.grid(row=0,column=0,sticky="nsew")
l2.grid(row=0,column=1,sticky="nsew")
l3.grid(row=0,column=2,sticky="nsew")
l4.grid(row=0,column=3,sticky="nsew")

label.grid(row=1, column=0,columnspan=4,sticky="nsew")

button1.grid(row=3, column=0,sticky="nsew")
button2.grid(row=3, column=1,sticky="nsew")
button3.grid(row=3, column=2,sticky="nsew")
button4.grid(row=4, column=0,sticky="nsew")
button5.grid(row=4, column=1,sticky="nsew")
button6.grid(row=4, column=2,sticky="nsew")
button7.grid(row=5, column=0,sticky="nsew")
button8.grid(row=5, column=1,sticky="nsew")
button9.grid(row=5, column=2,sticky="nsew")
button0.grid(row=6, column=1,sticky="nsew")
buttonPlus.grid(row=3, column=3,sticky="nsew")
buttonMinus.grid(row=4, column=3,sticky="nsew")
buttonMultiply.grid(row=5, column=3,sticky="nsew")
buttonDivide.grid(row=6, column=3,sticky="nsew")
buttonEqual.grid(row=6, column=2,sticky="nsew")
buttonClear.grid(row=2, column=3,sticky="nsew")
buttonDecimal.grid(row=6, column=0,sticky="nsew")
buttonExponent.grid(row=2, column=0,sticky="nsew")
buttonRoot.grid(row=2, column=1,sticky="nsew")
buttonNegative.grid(row=2,column=2,sticky="nsew")




root.mainloop()

