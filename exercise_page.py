import tkinter as tk
from tkinter import ttk
from insights_page import InsightsPage  # Import the InsightsPage class
from pushup_counter import PushupTracker
from bicep_curl_tracker import BicepCurlTracker 
from Squat import Squat
class ExercisePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Exercise Tracking")
        self.root.geometry("550x320")

        # Set the font and size for buttons
        button_font = ('Candara', 16)

        # Create a style and configure it
        style = ttk.Style()
        style.configure('TButton', font=button_font)

        title_label = ttk.Label(self.root, text="Choose Your Exercise", font=("Candara", 40, "bold"), padding=(0, 30))
        title_label.pack()

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=30)

        pushup_button = ttk.Button(button_frame, text="Pushup", command=self.pushup)
        pushup_button.grid(row=0, column=0, padx=10, pady=10)

        situp_button = ttk.Button(button_frame, text="Squat", command=self.SquatTracker)
        situp_button.grid(row=0, column=1, padx=10, pady=10)

        bicep_curl_button = ttk.Button(button_frame, text="Bicep Curl", command=self.BiCurlTracker)
        bicep_curl_button.grid(row=1, column=0, padx=10, pady=10)

        exit_button = ttk.Button(button_frame, text="Exit", command=lambda: self.exit_program())
        exit_button.grid(row=1, column=1, pady=10, padx=10)

    def pushup(self):
        self.root.destroy()
        pushup_window=tk.Tk()
        PushupTracker(pushup_window)
        pushup_window.mainloop()

    def BiCurlTracker(self):
        self.root.destroy()
        bicep_curl_window=tk.Tk()
        BicepCurlTracker(bicep_curl_window)
        bicep_curl_window.mainloop()

    def SquatTracker(self):
        self.root.destroy()
        squat_window=tk.Tk()
        Squat(squat_window)
        squat_window.mainloop()

    def show_insights(self, exercise_module_window):
        InsightsPage(exercise_module_window)

    def exit_program(self, window=None):
        if window:
            window.destroy()
        else:
            self.root.destroy()
    def situp(self):
        pass

