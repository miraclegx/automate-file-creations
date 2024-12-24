# tryin to automate making a love game functions
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def save_to():
	file_path = tk.filedialog.asksaveasfilename(defaultextension='.lua')
	if file_path:
		with open(file_path,'w') as file:
			file.write('''function love.load()\nend\nfunction love.update(dt)\nend\nfunction love.draw()\nend''')
	pop_up  = messagebox.showinfo('very boring guy','file created')

root = tk.Tk()
root.geometry('200x100')
root.title('Make love file')

label = tk.Label(root,text='Enter A Name For The File').grid(row = 1,column = 0,padx = 20)

# enrty box for the fil_ename
'''f_name = tk.Entry(root,width = 5)
f_name.grid(column = 5,row = 1,padx = 10)'''

#buton to selct save directory
save_btn = tk.Button(root,text = 'clic me',command = save_to)
save_btn.grid(column = 0,row = 2,pady = 0)

root.mainloop()