from tkinter import *
from tkinter import ttk

class HelloWorldApp:
    def __init__(self, root):
        self.root = root
        self.setup_tool_bar()
        self.setup_text_area()
        
    def setup_tool_bar(self):
        tool_bar_container = Frame(self.root, background="red")
        tool_bar_container.pack()
        open_button = Button(tool_bar_container, text="Open")
        open_button.grid()
        save_button = Button(tool_bar_container, text="Save")
        save_button.grid()

    def setup_text_area(self):
        text_area_container = Frame(self.root)
        # Expand and fill to the full width and height of parent window
        text_area_container.pack(fill="both", expand=True)
        
        text = Text(text_area_container, font="Helvetica 12")
        text.pack(pady=45, padx=45, fill="both", expand=True)
        

if __name__ == "__main__":
    root = Tk()
    app = HelloWorldApp(root)
    root.mainloop()
