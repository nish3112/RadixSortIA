from audioop import add
from cmath import e
from importlib.resources import path
from itertools import count
from logging import root
import os
from random import paretovariate
import re
from sqlite3 import paramstyle
import subprocess
from sys import stdin
from tkinter import *
from tkinter.ttk import Separator
from tokenize import String
from turtle import st
os.environ["JAVA_HOME"] = "C:/Users/tnish/java-1.8.0-openjdk-1.8.0.322-2.b06.dev.redhat.windows.x86_64/bin"
parent = Tk()  
parent.geometry("600x400")

save_path = 'C:/Users/tnish/OneDrive/Desktop/'
file_name = "test.txt"
file_name2 = "test1234.txt"
completeName = os.path.join(save_path, file_name)
completeName2 = os.path.join(save_path, file_name2)


num1 = Label(parent,text = "1.]").grid(row = 0, column = 0)  
e1 = Entry(parent)
e1.grid(row = 0, column = 1 )

num2 = Label(parent,text = "2.]").grid(row = 0, column = 4)  
e2 = Entry(parent)
e2.grid(row = 0, column = 5,padx=5,pady=5)

num3 = Label(parent,text = "3.]").grid(row = 0, column = 7)  
e3 = Entry(parent)
e3.grid(row = 0, column = 8)  



num4 = Label(parent,text = "4.]").grid(row = 1, column = 0)  
e4 = Entry(parent)
e4.grid(row = 1, column = 1) 

num5 = Label(parent,text = "5.]").grid(row = 1, column = 4)  
e5 = Entry(parent)
e5.grid(row = 1, column = 5)  


num6 = Label(parent,text = "6.]").grid(row = 1, column = 7)  
e6 = Entry(parent)
e6.grid(row = 1, column = 8) 




num7 = Label(parent,text = "7.]").grid(row = 2, column = 0)  
e7 = Entry(parent)
e7.grid(row = 2, column = 1)  

num8 = Label(parent,text = "8.]").grid(row = 2, column = 4)  
e8 = Entry(parent)
e8.grid(row = 2, column = 5)  

num9 = Label(parent,text = "9.]").grid(row = 2, column = 7)  
e9 = Entry(parent)
e9.grid(row = 2, column = 8)  



num10 = Label(parent,text = "10.]").grid(row = 3, column = 4)  
e10 = Entry(parent)
e10.grid(row = 3, column = 5)   
def openNewWindow():
    newWindow = Toplevel(parent)
    newWindow.title("Visualization")
    newWindow.geometry("600x400")
    file = open(completeName2,"r")
    Lines = file.readlines()
    
    count = 0
    list_steps = ["Original Array","Changes at position 1","Changes at position 10", "Changes at postion 100", "Changes at position 1000", "Changes at position 10000","Count at position 100000"]
    for line in Lines:
        # field = line.split(",") 
        field1 = "{}".format(line.strip())
        num_1 = Label(newWindow,text = field1)
        num_1.grid(row = count, column = 2, pady=20)
        num_2 = Label(newWindow,text = list_steps[count])
        num_2.grid(row = count, column = 1, pady=20)
        count +=1
        submit = Button(newWindow, text = "Next")
        submit.grid(row = 5, column = 5)  
        
    parent.mainloop()

# def exe_java():
#     os.system("start /B start cmd.exe @cmd /k javac RadixSort.java")
#     os.system("start /B start cmd.exe @cmd /k java RadixSort")
import os.path,subprocess
from subprocess import STDOUT,PIPE

def exe_file():
    command = "javac RadixSort.java"
    command2 = "java RadixSort"

    subprocess.call(command, shell=True)
    subprocess.call(command2, shell=True)

    
   
    
    
def savetofile():
    file = open(completeName, "w")
    file.write(str(e1.get()) + ",")
    file.write(str(e2.get()) + ",")
    file.write(str(e3.get()) + ",")
    file.write(str(e4.get()) + ",")
    file.write(str(e5.get()) + ",")
    file.write(str(e6.get()) + ",")
    file.write(str(e7.get()) + ",")
    file.write(str(e8.get()) + ",")
    file.write(str(e9.get()) + ",")
    file.write(str(e10.get()))
    file.close()
    global params
    params = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]
    
submit = Button(parent, text = "Update", command=savetofile and exe_file)
submit.grid(row = 5, column = 5)  

submit1 = Button(parent, text = "Start", command=openNewWindow)
submit1.grid(row = 7, column = 7)
parent.mainloop()  
    
