import tkinter as tk
import iavl
import random

class Viewer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.tree = iavl.Tree()
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.text = tk.Text(self)
        self.text.pack()
        self.create_button = tk.Button(self)
        self.create_button["text"] = "New Tree"
        self.create_button["command"] = self.create_tree
        self.create_button.pack(side=tk.LEFT)

        self.display_button = tk.Button(self)
        self.display_button["text"] = "Display Tree"
        self.display_button["command"] = self.print_tree
        self.display_button.pack(side=tk.LEFT)

        self.insert_button = tk.Button(self)
        self.insert_button["text"] = "Insert Node"
        self.insert_button["command"] = self.insert_node
        self.insert_button.pack(side=tk.LEFT)

    def create_tree(self):
        self.tree = iavl.Tree()

    def print_tree(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, str(self.tree.display()))

    def insert_node(self):
        for i in range(10):
            key = random.randint(0, 100)
            self.tree.insert(key, str(key))

if __name__ == '__main__':
    root = tk.Tk()
    app = Viewer(master=root)
    app.mainloop()