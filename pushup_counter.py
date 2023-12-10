import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import cv2
from pose_detector import PoseDetector
from insights_page import InsightsPage

class PushupTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Pushup Tracking")
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
                elbow = self.detector.find_angle(frame, lm_list, 11, 13, 15, results, draw=False)
                shoulder = self.detector.find_angle(frame, lm_list, 13, 11, 23, results, draw=False)
                hip = self.detector.find_angle(frame, lm_list, 11, 23, 25, results, draw=False)

                per = int(np.interp(elbow, (90, 160), (0, 100)))
                bar = int(np.interp(elbow, (90, 160), (380, 50)))

                if elbow > 160 and shoulder > 40 and hip > 160:
                    self.form = 1

                if self.form == 1:
                    if per == 0:
                        if elbow <= 90 and hip > 160:
                            self.feedback = "Up"
                            if self.direction == 0:
                                self.count += 0.5
                                self.direction = 1
                        else:
                            self.feedback = "Fix Form"
                            self.error += 1

                    if per == 100:
                        if elbow > 160 and shoulder > 40 and hip > 160:
                            self.feedback = "Down"
                            if self.direction == 1:
                                self.count += 0.5
                                self.direction = 0
                        else:
                            self.feedback = "Fix Form"
                            self.error += 1

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
        data={"User":"Gourang","Exercise":"Pushup","Count":self.count,"Error":self.error}
        InsightsPage(insight_window,data)
        self.cap.release()
        insight_window.mainloop()

        

