import tkinter as tk
import main
import os
from tkinter import filedialog

downlist = []
filedir = ""
downpath = ""

window = tk.Tk()
window.title("Video Download")

sw = window.winfo_screenwidth()
#得到屏幕宽度
sh = window.winfo_screenheight()
#得到屏幕高度
ww = 600
wh = 600
#窗口宽高为100
x = (sw-ww) / 2
y = (sh-wh) / 2
window.geometry("%dx%d+%d+%d" % (ww, wh, x, y)) # 窗口居中布置,大小为ww wh

def open_folder():
    global filedir
    filedir = filedialog.askdirectory(title='Select a folder', initialdir=(os.getcwd()))
    filelist = main.get_filelist(filedir)
    filelist = sorted(filelist)
    for item in filelist:
        lb.insert('end', item)

def select_all():
    lb.select_set(0, tk.END)

def unselect_all():
    lb.select_clear(0, tk.END)

def select_storepath():
    global downpath
    downpath = filedialog.askdirectory(title="Select a folder", initialdir=(os.environ['HOME']+'/Downloads'))

def download_selected():
    downlist = []
    for i in range(lb.size()):
        if (lb.select_includes(i)):
            main.downloadFile(filedir +'/'+ lb.get(i), downpath)

def get_urllist():
    urllist = []
    for i in range(lb.size()):
        if (lb.select_includes(i)):
            urllist.extend(main.get_urllist(filedir + '/' + lb.get(i)))
    print(urllist)
    t.delete('0.0', tk.END)
    for i in urllist:
        print(i)
        t.insert(tk.END, i[0] + '\n\n')


menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open Folder', command=open_folder)

row = 1

b1 = tk.Button(window, text="Open Folder", command=open_folder)
b1.grid(row=row, column=0, sticky=tk.W)
row = row + 1

b2 = tk.Button(window, text="Select All", command=select_all)
b2.grid(row=0, column=1)


b2_ = tk.Button(window, text="Unselect All", command=unselect_all)
b2_.grid(row=0, column=2)


b3 = tk.Button(window, text="Download Selected", command=download_selected)
b3.grid(row=row, column=0, sticky=tk.W)
row = row + 1

b4 = tk.Button(window, text="Select Store Path", command=select_storepath)
b4.grid(row=row, column=0, sticky=tk.W)
row = row + 1

b5 = tk.Button(window, text="Get Urllist", command=get_urllist)
b5.grid(row=row, column=0, sticky=tk.W)
row = row + 1

lb = tk.Listbox(window, height=30, selectmode=tk.MULTIPLE)
lb.grid(row=1, column = 1, rowspan=4, columnspan=2)

t = tk.Text(window, height = 38, width=30, relief="solid")
t.grid(row=1, column=4, rowspan=4)
scroll = tk.Scrollbar()
scroll.grid(row=1,column=5, rowspan=4)
scroll.config(command=t.yview)
t.config(yscrollcommand=scroll.set)

window.grid_columnconfigure(3, minsize=10)
window.config(menu = menubar)

window.mainloop()