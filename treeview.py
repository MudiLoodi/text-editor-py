import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo


class DirectoryTreeView(ttk.Treeview):
    def __init__(self, root):
        super().__init__(root)
        self.heading('#0', text='Departments', anchor=tk.W)
        self.insert('', tk.END, text='Administration', iid=0, open=False)
        self.insert('', tk.END, text='Logistics', iid=1, open=False)
        self.insert('', tk.END, text='Sales', iid=2, open=False)
        self.insert('', tk.END, text='Finance', iid=3, open=False)
        self.insert('', tk.END, text='IT', iid=4, open=False)

        # Adding children of the first node
        self.insert('', tk.END, text='John Doe', iid=5, open=False)
        self.insert('', tk.END, text='Jane Doe', iid=6, open=False)
    