import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title('calcultor')
root.geometry('320x320')
root.config(bg='white')
entry=tk.Entry(root,font=('Arial',20),borderwidth=4,relief='ridge',justify='right')
entry.grid(row=0,column=0,columnspan=3,padx=10,pady=10,ipady=10)
def click (symvol):
    x=entry.get()
    entry.delete(0,tk.END)
    entry.insert(tk.END,x+symvol)
def clear():
    entry.delete(0,tk.END)
def calculate():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(result))
    except Exception:
        messagebox.showerror('error')
def kay_click(event):
    key=event.char
    if key in "1234567890*/+-.":
        click(key)
    elif key=="\r":
        calculate()
    elif key=="\x08":
        entry.delete(len(entry.get())-1,tk.END)
buttons=[
    ('7', 1, 0),('8', 1, 1),('9', 1, 2),('+', 1, 3),
    ('4', 2, 0),('5',2, 1),('6', 2, 2),('-', 2, 3),
    ('1', 3, 0),('2', 3, 1),('3', 3, 2),('*', 3,3),
    ('0', 4, 1),('=', 4, 2),('/', 4, 3),(' ', 4, 0)
]
for (text, row,col) in buttons:
    if text=='=':
        btn=tk.Button(root,text=text,width=6,height=3,font=('Arial',20),bg='black',fg='white',activebackground='gray',command=calculate)
    else:
        btn=tk.Button(root,text=text,width=6,height=3,font=('Arial',20),bg='black',fg='white',activebackground='gray',command=lambda t=text: click(t))
    btn.grid(row=row,column=col,padx=8,pady=8)
clearbutton=tk.Button(root,text='c', width=6,height=3, font=('Arial',20),bg='black',fg='white',activebackground='gray', command=clear)
clearbutton.grid(row=4,column=0,pady=8)
root.bind("<Key>",kay_click)
root.mainloop()

        
                     


