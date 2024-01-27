import tkinter as tk
from tkinter import ttk
import os

class DirectoryTreeView(ttk.Treeview):
    def __init__(self, root):
        super().__init__(root)
        # current_folder = os.path.basename(os.getcwd())

        # self.populate_tree(os.getcwd())
        
    def update_dir(self, dir):
        # Delete the current tree
        self.delete(*self.get_children())
        # Update the heading
        self.heading('#0', text=f"{dir}", anchor=tk.W)
        self.populate_tree(dir)

    def populate_tree(self, path, parent=''):
        for item in os.listdir(path):
            # Ignore hidden files
            if not item.startswith(".") and not item.startswith("_"):
                item_path = os.path.join(path, item)

                if os.path.isdir(item_path):
                    # If it's a directory, add it as a parent node
                    node_id = self.insert(parent, tk.END, text=item, open=False)
                    self.populate_tree(item_path, parent=node_id)
                else:
                    # If it's a file, add it as a child node
                    self.insert(parent, tk.END, text=item, open=False)
