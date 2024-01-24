import tkinter as tk
from tkinter import ttk
from tkinter import *
import os

class DirectoryTreeView(ttk.Treeview):
    def __init__(self, root):
        super().__init__(root)
        current_folder = os.path.basename(os.getcwd())
        self.heading('#0', text=f"{current_folder}", anchor=tk.W)

        files = [f for f in os.listdir() if os.path.isfile(f)]
        for i in range(0, len(files)):
            self.insert("", END, text=f"{files[i]}", iid=i, open=False)