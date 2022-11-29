
import tkinter as tk
import tkinter.messagebox as tkm
import math

def button_click(event):

    btn = event.widget
    num = btn["text"]
    if num[0]==0:
        entry.delete(0,tk.END)


    if num == "=":

        siki = entry.get() 
        
        #siki.split('sqrt')
        #siki.replace('sqrt',',')
        res = eval(siki) 
        entry.delete(0, tk.END) 
        entry.insert(tk.END, res) 
    
    elif num == "CE":
        entry.delete(0,tk.END)
        res=0

    #elif num == "x²":
        #entry.delete(0,tk.END)
        #entry.insert(tk.END,res)
        #entry.insert(tk.END,"**")

    elif num == "sqrt":
        res = eval(siki)
        entry.delete(0, tk.END) 
        entry.insert(tk.END, res) 

    elif num == "mod":
        siki=entry.get()
        f=1

    
        

    else: 
        entry.insert(tk.END, num)


root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row=0, column=0, columnspan=3)


r, c = 1, 0
for num in range(9, -1, -1):
    button = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

a,b=4,1
sonotas=["CE","**","%"]
for sonota in sonotas:
    button = tk.Button(root, text=f"{sonota}", width=4, height=2, font=("", 30))
    button.grid(row=b, column=a)
    button.bind("<1>", button_click)
    b+=1

operators = ["+", "=", "-", ".", "/", "×"]
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

root.mainloop()
