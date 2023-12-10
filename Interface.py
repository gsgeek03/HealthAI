import tkinter as tk
import os
from tkinter import ttk, messagebox
from exercise_page import ExercisePage
from insights_page import InsightsPage
from food_page import FoodPage

class HealthAIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HealthAI")
        self.root.geometry("600x300")

        self.create_first_page()

    def create_first_page(self):
        self.destroy_widgets()

        # Title
        title_label = ttk.Label(self.root, text="HealthAI", font=("Candara", 40, "bold"), padding=(0, 30))
        title_label.pack()
        
        # Buttons side by side
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=30)

        # Style the buttons
        style = ttk.Style()
        style.configure('TButton', font=('Candara', 14), background='#4CAF50', fg='blue', borderwidth=0)
        style.map('TButton', background=[('active', '#45a999')])

        food_button = ttk.Button(button_frame, text="Food Recommendation", command=self.show_food_page, style='TButton')
        food_button.grid(row=0, column=0, padx=10)

        exercise_button = ttk.Button(button_frame, text="Exercise Tracking", command=self.show_exercise_page, style='TButton')
        exercise_button.grid(row=0, column=1, padx=10)

        # Exit Button
        exit_button = ttk.Button(self.root, text="Exit", command=lambda: self.exit_program(), style='TButton')
        exit_button.pack(pady=20)

    def show_food_page(self):
        self.root.destroy()
        os.system('python finalgui.py')

    def show_exercise_page(self):
        self.root.destroy()
        exercise_window = tk.Tk()
        ExercisePage(exercise_window)
        exercise_window.mainloop()

    def exit_program(self, window=None):
        confirmation = messagebox.askquestion("Exit", "Are you sure you want to exit?")
        if confirmation == 'yes':
            if window:
                window.destroy()
            else:
                self.root.destroy()

    def destroy_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthAIApp(root)
    root.mainloop()