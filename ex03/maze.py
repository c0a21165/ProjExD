import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global cx, cy, mx, my
    global tori,count,atai
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    if maze_lst[mx][my] == 1:
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1
    cx, cy = mx*100+50, my*100+50

    #if atai==0:
    #    for i in maze_lst:
     #       if maze_lst[mx][my]==0:
      #          mx2, my2 =i,i
            



    
    #gx, gy = mx2*100, my2*100
    canvas.coords("kokaton", cx, cy)
    canvas.coords("goal",150,150)
    count=my+mx
    if count ==5:
        henka()
    
    root.after(100, main_proc)

def henka():
    tkm.showwarning("こうかとん","ダッシュ")


def henka2():
    global tori
    tori = tk.PhotoImage(file="fig/0.png")

def henka3():
    tkm.showwarning("こうかとん","つかれた")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15, 9)
    # print(maze_lst)
    mm.show_maze(canvas, maze_lst)
    mx, my= 1, 1
    cx, cy = mx*100+50, my*100+50

    count=0
    atai=0

    tori = tk.PhotoImage(file="fig/8.png")
    canvas.create_image(cx, cy, image=tori, tag="kokaton")
    goal = tk.PhotoImage(file="fig/0.png")
    canvas.create_image(cx,cy, image=goal, tag="goal")
    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()