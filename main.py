from tkinter import *
from tkinter import ttk

class HelloWorldApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        text = Text(self.root)
        # Expand and fill to the full width and height of parent window
        text.pack(pady=45, padx=45, fill="both", expand=True)


if __name__ == "__main__":
    root = Tk()
    app = HelloWorldApp(root)
    root.mainloop()
