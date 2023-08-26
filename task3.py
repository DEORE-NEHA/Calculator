import random, string
from tkinter import *
import pyperclip
 
root =Tk()
root.geometry("400x400") 
 
root.title(" Password Generator")
 
 
output_pass = StringVar()
 
all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]  #list of all possible characters
 
def randPassGen():
    password = "" # to store password
    for y in range(pass_len.get()):
        char_type = random.choice(all_combi)   #to randomize the occurance of alphabet, digit or symbol
        password = password + random.choice(char_type)
     
    output_pass.set(password)
 
 
def copyPass():
    pyperclip.copy(output_pass.get())
 
 
pass_head = Label(root, text = 'Password Length', font = 'times 12 bold').pack(pady=10) 
 
pass_len = IntVar() 
length = Spinbox(root, from_ = 4, to_ = 32 , textvariable = pass_len , width = 24, font='times 16').pack()
 

 
Button(root, command = randPassGen, text = "Generate Password", font="times 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
pass_label = Label(root, text = 'Random Generated Password', font = 'times 12 bold').pack(pady="30 10")
Entry(root , textvariable = output_pass, width = 24, font='times 16').pack()
 

 
Button(root, text = 'Copy to Clipboard', command = copyPass, font="times 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
root.mainloop()  