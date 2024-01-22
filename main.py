from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox 

class TextEditApp:
    def __init__(self, root):
        self.root = root
        self.current_file = None
        self.file_name_StrVar = StringVar(value="Untitled")
        
        self.setup_tool_bar()
        self.setup_text_area()
        self.setup_file_info()
        
    # TODO: Warn about unsaved changes.    
    def quit_app(self):
        root.destroy()
    
    def ask_for_unsaved_changes(self):
        current_content = self.text.get(1.0, "end-1c")
        if (current_content):
            continue_ = messagebox.askokcancel("Unsaved changes", "You have made changes that are unsaved. Do you want to continue?") 
            # User want to continue action. Return True
            return continue_
        # No unsaved changes. Return True by default
        return True
        
    def open_file(self):
        if self.ask_for_unsaved_changes():
            filetypes = (('text files', '*.txt'), ('All files', '*.*'))
            filename = fd.askopenfilename(filetypes=filetypes)
            if (filename):
                with open(filename, "r") as file:
                    file_content = file.read()
                    self.text.insert(chars = file_content, index=END)
                file.close()
            self.file_name_StrVar.set(filename)
    
    def save_file(self):
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))
        if self.file_name_StrVar:
            file_path_to_save = fd.asksaveasfilename(confirmoverwrite=True, filetypes=filetypes, title="Save As")
            with open(file_path_to_save, "w") as file:
                new_file_content = self.text.get(1.0, "end-1c")
                file.write(new_file_content)
            file.close()
        
        
    def setup_tool_bar(self):
        tool_bar_container = Frame(self.root)
        tool_bar_container.pack(fill="both", expand=False)
        
        open_button = Button(tool_bar_container, text="Open", command=self.open_file)
        open_button.grid(row=0, column=0, padx=4, pady=4)
        
        save_button = Button(tool_bar_container, text="Save", command=self.save_file)
        save_button.grid(row=0, column=1, padx=4, pady=4)
        
        quit_button = Button(tool_bar_container, text="Quit", command=self.quit_app)
        quit_button.grid(row=0, column=2, padx=4, pady=4)

    def setup_text_area(self):
        self.text_area_container = Frame(self.root, bg="grey")
        # Expand and fill to the full width and height of parent window
        self.text_area_container.pack(fill="both", expand=True) 
        
        self.text = Text(self.text_area_container, font="Helvetica 12", border=2)
        self.text.pack(padx=45, pady=(10, 0), fill="both", expand=True)
        
    def setup_file_info(self):
        file_info_container = Frame(self.text_area_container, bg="green")
        file_info_container.pack(side=RIGHT, padx=(0, 45), pady=4)
        
        self.file_name_label = Label(file_info_container, textvariable=self.file_name_StrVar)
        self.file_name_label.pack()
        

if __name__ == "__main__":
    root = Tk()
    app = TextEditApp(root)
    root.mainloop()
