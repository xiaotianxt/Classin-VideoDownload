import tkinter as tk
import main
import os, sys, time
from tkinter import filedialog


downlist = []
filedir = ""
downpath = ""

windowMain = tk.Tk()
windowMain.title("Video Download")

sw = windowMain.winfo_screenwidth()
#得到屏幕宽度
sh = windowMain.winfo_screenheight()
#得到屏幕高度
ww = 700
wh = 600
#窗口宽高为100
x = (sw-ww) / 2
y = (sh-wh) / 2
windowMain.geometry("%dx%d+%d+%d" % (ww, wh, x, y)) # 窗口居中布置,大小为ww wh

def open_folder():
    global filedir
    filedir = filedialog.askdirectory(title='Select a folder', initialdir=(os.path.dirname(sys.argv[0])))
    filelist = main.get_filelist(filedir)
    filelist.sort()
    listboxFilelist.delete(0, tk.END)
    listboxDatelist.delete(0, tk.END)
    for item in filelist:
        listboxFilelist.insert('end', item[1])
        listboxDatelist.insert('end', item[0])
    
    listbox_click()

def select_all():
    listboxFilelist.select_set(0, tk.END)
    listbox_click()
    

def unselect_all():
    listboxFilelist.select_clear(0, tk.END)
    listbox_click()

def select_storepath():
    global downpath
    downpath = filedialog.askdirectory(title="Select a folder", initialdir=(os.environ['HOME']+'/Downloads'))

def download_selected():
    downlist = []
    for i in range(listboxFilelist.size()):
        if (listboxFilelist.select_includes(i)):
            main.downloadFile(filedir +'/'+ listboxFilelist.get(i), downpath)

def listbox_click(*event):
    urllist = get_urllist()
    textResult.delete('0.0', tk.END)
    textResult.insert(tk.END, "Video Numbers: " + "%02d" % len(urllist))
    

def get_urllist():
    urllist = []
    for i in range(listboxFilelist.size()):
        if (listboxFilelist.select_includes(i)):
            if(listboxFilelist.get(i)[0]=='.'):
                continue
            urllist.extend(main.get_urllist(filedir + '/' + listboxFilelist.get(i)))
    print(urllist)
    textUrllist.delete('0.0', tk.END)
    for i in urllist:
        textUrllist.insert(tk.END, i[0] + '\n\n')
    textResult.delete('0.0', tk.END)
    textResult.insert(tk.END, "Video Numbers: " + "%02d" % len(urllist))
    return urllist

def copy_all():
    data = textUrllist.get('0.0', tk.END)
    os.system("echo '%s' | pbcopy" % data)


menubarMenubar = tk.Menu(windowMain)
filemenu = tk.Menu(menubarMenubar, tearoff=0)
menubarMenubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open Folder', command=open_folder)

row = 1

buttonOpenFolder = tk.Button(windowMain, text="Open Folder", command=open_folder, width=20)
buttonOpenFolder.grid(row=row, column=1, sticky=tk.W)
row = row + 1

buttonSelectAll = tk.Button(windowMain, text="Select All", command=select_all, width=20)
buttonSelectAll.grid(row=row - 1, column=4)

buttonUnselectAll = tk.Button(windowMain, text="Unselect All", command=unselect_all, width=20)
buttonUnselectAll.grid(row=row, column=4)

buttonCopyToClipboard = tk.Button(windowMain, text="Copy to Clipboard", command=copy_all, width=20)
buttonCopyToClipboard.grid(row=row + 1, column=4)

buttonDownloadSelected = tk.Button(windowMain, text="Download Selected", command=download_selected, width=20)
buttonDownloadSelected.grid(row=row, column=1, sticky=tk.W)
row = row + 1

buttonSelectStorePath = tk.Button(windowMain, text="Select Store Path", command=select_storepath, width=20)
buttonSelectStorePath.grid(row=row, column=1, sticky=tk.W)
row = row + 1

buttonGetUrllist = tk.Button(windowMain, text="Get Urllist", command=get_urllist, width=20)
buttonGetUrllist.grid(row=row, column=1, sticky=tk.W)
row = row + 1



listboxFilelist = tk.Listbox(windowMain, height=20, width=15, selectmode=tk.MULTIPLE, font=("TkTextFont", 15))
listboxFilelist.grid(row=row, column = 2)
listboxFilelist.bind('<<ListboxSelect>>', listbox_click)
row = row + 1

listboxDatelist = tk.Listbox(windowMain, height=20, width=20, font=("TkTextFont", 15))
listboxDatelist.grid(row = row - 1, column=1)
row = row + 1

textUrllist = tk.Text(windowMain, height = 20, width=30, relief="solid", font=("TkTextFont", 15))
textUrllist.grid(row=row - 2, column=4)
scrollUrllist = tk.Scrollbar()
scrollUrllist.grid(row=row - 2,column=5, sticky=tk.E + tk.W)
scrollUrllist.config(command=textUrllist.yview)
textUrllist.config(yscrollcommand=scrollUrllist.set)

textResult = tk.Text(windowMain, height = 1, width = 30, relief="solid")
textResult.grid(row=row - 3, column=4)
textResult.insert(tk.END, "Video Numbers: ")

windowMain.grid_columnconfigure(2, minsize=10)
windowMain.grid_columnconfigure(0, minsize=30)

for i in range(row - 2):
    windowMain.grid_rowconfigure(i, minsize=30)

windowMain.config(menu = menubarMenubar)

windowMain.mainloop()