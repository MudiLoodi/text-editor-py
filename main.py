from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox 
import os
import treeview

class TextEditApp:
    def __init__(self, root):
        self.root = root
        self.file_name_StrVar = StringVar(value="Untitled")
        self.file_status_StrVar = StringVar(value="")
        self.current_file_content = ""
        self.file_path_to_save = ""

        # Allows root to expand
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.geometry("850x600")
        self.root.title("Text Edit")
        
        self.setup_tool_bar()
        self.setup_file_info()
        self.setup_panned_window()
        
    # TODO: Warn about unsaved changes.    
    def quit_app(self):
        self.root.destroy()
        
    def detect_changes(self, event):
        self.file_status_StrVar.set("⬤")
    
    def listen_for_hotkeys(self, event):
        # X11 key mask for Control (4) and Mod1 (8) keys. 4+8=12
        if (event.state == 12):
            match event.keysym:
                case "s":
                    self.save_file(None)
                case "r":
                    # TODO: Redo
                    print("pressed r")
                case "u":
                    # TODO: Undo
                    print("pressed u")
    
    def ask_for_unsaved_changes(self):
        current_content_in_editor = self.text.get(1.0, "end-1c")
        if (self.current_file_content != current_content_in_editor):
            continue_ = messagebox.askokcancel("Unsaved changes", "You have made changes that are unsaved. Do you want to continue?") 
            # User want to continue action. Return True
            return continue_
        # No unsaved changes. Return True by default
        return True
        
    def open_file(self):
        if self.ask_for_unsaved_changes():
            filetypes = (('text files', '*.txt'), ('All files', '*.*'))
            self.file_path_to_save = fd.askopenfilename(filetypes=filetypes)
            if self.file_path_to_save:
                with open(self.file_path_to_save, "r") as file:
                    file_content = file.read()
                    self.text.delete(index1=1.0, index2=END)
                    self.text.insert(chars = file_content, index=END)
                    self.current_file_content = file_content
                file.close()
                file_name = os.path.basename(self.file_path_to_save)
                self.file_name_StrVar.set(file_name)
    
    def save_file(self, mode):
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))
        # if mode is save as or the current file is 'Untitled'
        if mode == "saveAS" or self.file_name_StrVar.get() == "Untitled":
            self.file_path_to_save = fd.asksaveasfilename(confirmoverwrite=True, filetypes=filetypes, title="Save As")
        if self.file_path_to_save:
            with open(self.file_path_to_save, "w") as file:
                new_file_content = self.text.get(1.0, "end-1c")
                self.current_file_content = new_file_content
                file.write(new_file_content)
            self.file_status_StrVar.set("")
            file.close()
    
    # Sets up the tool bar at the top.
    def setup_tool_bar(self):
        self.tool_bar_container = Frame(self.root)
        self.tool_bar_container.grid(column=0, row=0, sticky=W)
        
        file_menu_button= Menubutton ( self.tool_bar_container, text="File", relief=RAISED )
        file_menu_button.menu = Menu (file_menu_button, tearoff = 0)
        file_menu_button["menu"] = file_menu_button.menu
        file_menu_button.grid(column=0, row=0)
        
        file_menu_button.menu.add_command (label="Open", command=self.open_file)
        file_menu_button.menu.add_command (label="Save", command=lambda: self.save_file("save"))
        file_menu_button.menu.add_command (label="Save As", command=lambda: self.save_file("saveAS"))
        
        quit_button = Button(self.tool_bar_container, text="Quit", command=self.quit_app)
        quit_button.grid(column=1, row=0, padx=4, pady=4)

    # Sets up the paned window that holds the directory view and text sections.
    def setup_panned_window(self):
        pw = ttk.PanedWindow(orient=HORIZONTAL, width=1900)

        # Left 
        pw.add(self.directory_treeview_section())

        # Right 
        pw.add(self.text_section())

        pw.grid(column=0, row=1, sticky=NSEW)
        
        
    # Sets up the text section. Returns a Frame after setting up its layout
    def text_section(self):
        self.text_area_container = Frame(self.root)
        self.text_area_container.grid(column=0, row=0, sticky=NSEW, padx=10, pady=10)
        
        # Configure column and row weights for the text area container
        self.text_area_container.columnconfigure(0, weight=1)
        self.text_area_container.rowconfigure(0, weight=1)
        
        self.text = scrolledtext.ScrolledText(self.text_area_container, font="Helvetica 12", border=2)
        self.text.grid(sticky=NSEW, rowspan=4)
        
        # Detect changes in text
        self.text.bind("<Key>", self.detect_changes)
        # Listen for hotkeys
        self.text.bind("<Control-s>", self.listen_for_hotkeys)
        
        return self.text_area_container
        
    # Sets up the directory view section. Retruns Frame after setting it up.
    def directory_treeview_section(self):
        self.tree_container = Frame(self.root)
        self.tree_container.grid(column=1, row=1)
        
        # Overwrite default ttk style for later 
        # style = ttk.Style(self.root)
        # style.configure("Treeview", background=("gray"))
        self.tree = treeview.DirectoryTreeView(self.tree_container)
        self.tree.pack(fill="both", expand=True)

        self.tree.bind("<ButtonRelease-1>", self.open_selected_file)
        return self.tree_container

        
    def setup_file_info(self):
        self.file_name_label = Label(self.tool_bar_container, textvariable=self.file_name_StrVar)
        self.file_name_label.grid(column=10, row=0)
        
        self.file_status_label = Label(self.tool_bar_container, textvariable=self.file_status_StrVar)
        self.file_status_label.grid(column=11, row=0)
    
    def find_file_path(self, filename):
        for root, dirs, files in os.walk(os.getcwd()):
            if filename in files:
                return os.path.join(root, filename)

        return None  # File not found

    # Opens the selected file from the directory view
    def open_selected_file(self, event):
        tree_content = self.tree.focus()
        current_item = self.tree.item(tree_content)
        absolute_path = self.find_file_path(current_item["text"])
        # TODO: Check if the current item is a dir, if so ignore.
        if absolute_path == None:
            return
        elif not os.path.isdir(absolute_path):
            with open(absolute_path, "r") as file:
                file_content = file.read()
                self.text.delete(index1=1.0, index2=END)
                self.text.insert(chars = file_content, index=END)
                self.current_file_content = file_content
                self.file_name_StrVar.set(current_item["text"])
                self.file_path_to_save = absolute_path
            file.close()
        

if __name__ == "__main__":
    root = Tk()
    app = TextEditApp(root)
    root.mainloop()
