import tkinter as tk



window = tk.Tk()
window.title("Video Download")

sw = window.winfo_screenwidth()
#得到屏幕宽度
sh = window.winfo_screenheight()
#得到屏幕高度
ww = 350
wh = 600
#窗口宽高为100
x = (sw-ww) / 2
y = (sh-wh) / 2
window.geometry("%dx%d+%d+%d" % (ww, wh, x, y)) # 窗口居中布置,大小为ww wh

l = tk.Label(window, text='', bg='yellow')
l.pack()

def do_job():
    pass

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=do_job)

window.config(menu = menubar)

window.mainloop()