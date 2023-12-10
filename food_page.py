import tkinter as tk
from tkinter import ttk

class FoodPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Coming Soon")
        self.root.geometry("400x200")

        label_frame = ttk.Frame(self.root)
        label_frame.pack(expand=True, fill="both")

        label = ttk.Label(label_frame, text="Feature available soon", font=("Arial", 20))
        label.pack(pady=50)
        # Exit Button
        exit_button = ttk.Button(self.root, text="Exit", command=lambda: self.exit_program(self.root))
        exit_button.pack(pady=20)

    def exit_program(self, window=None):
        if window:
            window.destroy()
        else:
            self.root.destroy()
