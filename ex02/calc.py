import tkinter as tk
import tkinter.messagebox as tkm

def button_clik(event):
    btn=event.widget
    txt=btn[
    ]
    tkm.showinfo(txt,f"{}ボタンが押されました")


root = tk.Tk()
root.title("おためしか")
root.geometry("500x200")

button=tk.Button(root,text=0,font=30)
button=tk.Button(root,text=1,font=30)
button=tk.Button(root,text=2,font=30)
button=tk.Button(root,text=3,font=30)
button=tk.Button(root,text=4,font=30,width=,height)

button.bind("<1>",button_clik)
button.pack()


root.mainloop()