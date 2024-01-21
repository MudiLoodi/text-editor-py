from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

class HelloWorldApp:
    def __init__(self, root):
        self.root = root
        self.setup_tool_bar()
        self.setup_text_area()
        
    # TODO: Warn about unsaved changes.    
    def quit_app(self):
        root.destroy()
        
    def open_file(self):
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))
        filename = fd.askopenfilename(filetypes=filetypes)
        if (filename):
            with open(filename, "r") as file:
                file_content = file.read()
                self.text.insert(chars = file_content, index=END)
        
    def setup_tool_bar(self):
        tool_bar_container = Frame(self.root, background="red")
        tool_bar_container.pack(fill="both", expand=False)
        
        open_button = Button(tool_bar_container, text="Open", command=self.open_file)
        open_button.grid(row=0, column=0, padx=4, pady=4)
        
        save_button = Button(tool_bar_container, text="Save")
        save_button.grid(row=0, column=1, padx=4, pady=4)
        
        quit_button = Button(tool_bar_container, text="Quit", command=self.quit_app)
        quit_button.grid(row=0, column=2, padx=4, pady=4)
        


    def setup_text_area(self):
        text_area_container = Frame(self.root)
        # Expand and fill to the full width and height of parent window
        text_area_container.pack(fill="both", expand=True)
        
        self.text = Text(text_area_container, font="Helvetica 12")
        self.text.pack(pady=45, padx=45, fill="both", expand=True)
        

if __name__ == "__main__":
    root = Tk()
    app = HelloWorldApp(root)
    root.mainloop()
