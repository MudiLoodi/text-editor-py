import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

class DirectoryTreeView():
    def __init__(self, root):
        self.root = root
        tree = ttk.Treeview(self.root)
        tree.heading('#0', text='Departments', anchor=tk.W)
        tree.insert('', tk.END, text='Administration', iid=0, open=False)
        tree.insert('', tk.END, text='Logistics', iid=1, open=False)
        tree.insert('', tk.END, text='Sales', iid=2, open=False)
        tree.insert('', tk.END, text='Finance', iid=3, open=False)
        tree.insert('', tk.END, text='IT', iid=4, open=False)

        # adding children of first node
        tree.insert('', tk.END, text='John Doe', iid=5, open=False)
        tree.insert('', tk.END, text='Jane Doe', iid=6, open=False)
        tree.pack()