import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import cv2
from pose_detector import PoseDetector
from insights_page import InsightsPage

class Squat:
    def __init__(self, root):
        self.root = root
        self.root.title("Squat")
        self.root.geometry("800x600")

        self.detector = PoseDetector()
        self.cap = cv2.VideoCapture(0)
        self.count = 0
        self.error = 0
        self.direction = 0
        self.form = 0
        self.feedback = ""

        # Camera Frame
        self.camera_frame = ttk.Frame(self.root)
        self.camera_frame.pack(expand=True, fill="both")

        # Count Label
        self.count_label = ttk.Label(self.root, text="Count: 0", font=("Arial", 18))
        self.count_label.pack(pady=10)

        # Status Label
        self.status_label = ttk.Label(self.root, text="Status: Fix Form", font=("Arial", 18))
        self.status_label.pack(pady=10)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)

        exit_button = ttk.Button(button_frame, text="Exit", command=self.exit_program)
        exit_button.pack(side="left", padx=10)

        insights_button = ttk.Button(button_frame, text="Insights", command=self.show_insights)
        insights_button.pack(side="left", padx=10)

        self.create_widgets()

    def create_widgets(self):
        self.display_camera_feed()

    def display_camera_feed(self):
        _, frame = self.cap.read()

        if frame is not None:
            frame, results = self.detector.find_pose(frame)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            photo = ImageTk.PhotoImage(image=Image.fromarray(frame_rgb))
            camera_label = ttk.Label(self.camera_frame, image=photo)
            camera_label.photo = photo
            camera_label.grid(row=0, column=0)

            if results.pose_landmarks:
                lm_list = self.detector.find_position(frame, [], results)
                right_leg = self.detector.find_angle(frame, lm_list, 24, 26, 28, results, draw=False)
                left_leg = self.detector.find_angle(frame, lm_list, 23, 25, 27, results, draw=False)

                if right_leg >= 150 and left_leg >= 150:
                    self.form = 1

                if self.form == 1:
                        if right_leg >= 160 and left_leg >= 160:
                            self.feedback = "You are Standing. Do Squat"
                        elif right_leg < 80 and left_leg < 80:
                            self.feedback = "Incorrect form. Try to maintain 90 degree while squatting. Stand up and do again"
                            self.error += 1
                            self.form = 0
                        elif right_leg >= 80 and right_leg<=100 and left_leg >= 80 and left_leg<=100:
                            self.feedback = "Correct Form. Keep Going"
                            self.count += 1
                            self.form = 0
                else:
                    self.feedback = "Stand Straight to start doing Squat"
                    self.form = 0
                # Update labels
                self.count_label.config(text=f"Count: {int(self.count)}")
                self.status_label.config(text=f"Status: {self.feedback}")

        self.root.after(10, self.display_camera_feed)

    def exit_program(self):
        self.cap.release()
        self.root.destroy()

    def stop_camera_feed(self):
        if self.cap.isOpened():
            self.cap.release()


    def show_insights(self):
        self.stop_camera_feed()
        self.root.destroy()
        insight_window = tk.Tk() 
        data={"User":"Gourang","Exercise":"Squat","Count":self.count,"Error":self.error}
        InsightsPage(insight_window,data)
        self.cap.release()
        insight_window.mainloop()
        

