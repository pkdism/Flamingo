from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
root = Tk("Text Editor")

scrollbar = Scrollbar(root)
scrollbar.pack(side = "right", fill = "y")
text = Text(root, font = "Consolas", bg = "#000055", fg = "#FFFFFF", insertbackground = "white", yscrollcommand = scrollbar.set);
text.pack(side="left", fill="both", expand=True)
scrollbar.config(command = text.yview)


def saveas(event):
	global filename
	t = text.get("1.0","end-1c")
	savelocation = filedialog.asksaveasfilename(defaultextension = '.txt', filetypes = (('Text Files','*.txt'), ('Python files', '*.py'), ('All files', '*.*')))
	file = open(savelocation, "w")
	file.write(t)
	file.close()

def open_(event):
	global filename
	openfile = filedialog.askopenfilename(filetypes = (('Text Files','*.txt'), ('Python files', '*.py'), ('All files', '*.*')))
	#if(openfile!=None):
	with open(openfile, "r") as f:
		contents = f.read()
		text.insert('1.0',contents)
		f.close()

def exit_command(event):
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def saveas_util():
	global filename
	t = text.get("1.0","end-1c")
	savelocation = filedialog.asksaveasfilename(defaultextension = '.txt', filetypes = (('Text Files','*.txt'), ('Python files', '*.py'), ('All files', '*.*')))
	file = open(savelocation, "w")
	file.write(t)
	file.close()

def open_util():
	global filename
	openfile = filedialog.askopenfilename(filetypes = (('Text Files','*.txt'), ('Python files', '*.py'), ('All files', '*.*')))
	#if(openfile!=None):
	with open(openfile, "r") as f:
		contents = f.read()
		text.insert('1.0',contents)
		f.close()

def exit_command_util():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()


def about():
	label = messagebox.showinfo("Flamingo", "Copyright © 2016-2016 \nPawan Dwivedi\nIndian Institute of Technology Dhanbad")

root.bind("<Control-s>", saveas)
root.bind("<Control-o>", open_)
root.bind("<Escape>", exit_command)
root.bind("<Control-w>", exit_command)

menu = Menu(root)
root.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Open       ctrl+o", command = open_util)
filemenu.add_command(label = "Save As   ctrl+s", command = saveas_util)
filemenu.add_command(label = "Exit          esc", command = exit_command_util)
helpmenu = Menu(menu)
menu.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "About", command = about)

root.mainloop()