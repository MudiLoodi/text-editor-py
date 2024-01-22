from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox 
import os

class TextEditApp:
    def __init__(self, root):
        self.root = root
        self.file_name_StrVar = StringVar(value="Untitled")
        self.file_status_StrVar = StringVar(value="")
        self.current_file_content = ""
        self.file_path_to_save = ""
        
        self.setup_tool_bar()
        self.setup_text_area()
        self.setup_file_info()
        
    # TODO: Warn about unsaved changes.    
    def quit_app(self):
        root.destroy()
        
    def detect_changes(self, event):
        self.file_status_StrVar.set("⬤")
    
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
        if mode == "saveAS" or not self.file_name_StrVar:
            self.file_path_to_save = fd.asksaveasfilename(confirmoverwrite=True, filetypes=filetypes, title="Save As")
        if self.file_path_to_save:
            with open(self.file_path_to_save, "w") as file:
                new_file_content = self.text.get(1.0, "end-1c")
                self.current_file_content = new_file_content
                file.write(new_file_content)
            self.file_status_StrVar.set("")
            file.close()
    
    def setup_tool_bar(self):
        tool_bar_container = Frame(self.root)
        tool_bar_container.pack(fill="both", expand=False)
        
        open_button = Button(tool_bar_container, text="Open", command=self.open_file)
        open_button.grid(row=0, column=0, padx=4, pady=4)
        
        save_as_button = Button(tool_bar_container, text="Save as", command=lambda: self.save_file("saveAS"))
        save_as_button.grid(row=0, column=1, padx=4, pady=4)
        
        save_button = Button(tool_bar_container, text="Save", command=lambda: self.save_file("save"))
        save_button.grid(row=0, column=2, padx=4, pady=4)
        
        quit_button = Button(tool_bar_container, text="Quit", command=self.quit_app)
        quit_button.grid(row=0, column=3, padx=4, pady=4)

    def setup_text_area(self):
        self.text_area_container = Frame(self.root, bg="grey")
        # Expand and fill to the full width and height of parent window
        self.text_area_container.pack(fill="both", expand=True) 
        
        self.text = Text(self.text_area_container, font="Helvetica 12", border=2)
        self.text.pack(padx=45, pady=(10, 0), fill="both", expand=True)
        
        # Detect changes in text
        self.text.bind("<Key>", self.detect_changes)
        
    def setup_file_info(self):
        file_info_container = Frame(self.text_area_container)
        file_info_container.pack(side=RIGHT, padx=(0, 45), pady=4)
        
        self.file_name_label = Label(file_info_container, textvariable=self.file_name_StrVar)
        self.file_name_label.grid(column=0, row=0)
        
        self.file_status_label = Label(file_info_container, textvariable=self.file_status_StrVar)
        self.file_status_label.grid(column=1, row=0)
        

if __name__ == "__main__":
    root = Tk()
    app = TextEditApp(root)
    root.mainloop()
