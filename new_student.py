import cv2
import os
import tkinter as tk
from tkinter import messagebox

class WebcamApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Webcam App")

        # Define folder path to save the captured image
        self.folder_path = "captured_images"

        # Create the folder if it doesn't exist
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

        # Initialize the webcam
        self.cap = cv2.VideoCapture(0)

        # Check if webcam is opened successfully
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Error opening webcam!")
            self.root.destroy()
            return

        # Create GUI components
        self.label = tk.Label(root, text="Enter your name:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.capture_button = tk.Button(root, text="Capture Image", command=self.capture_image)
        self.capture_button.pack(pady=20)

    def capture_image(self):
        # Capture the frame
        ret, frame = self.cap.read()

        # Check if frame is captured successfully
        if not ret:
            messagebox.showerror("Error", "Error capturing frame!")
            return

        # Get user name from entry
        user_name = self.entry.get()

        # Generate unique filename with user name
        filename = f"{self.folder_path}/{str(user_name)}.jpg"

        # Save the captured image
        cv2.imwrite(filename, frame)

        # Release the webcam
        self.cap.release()

        # Display success message
        messagebox.showinfo("Success", f"Image captured successfully and saved as {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WebcamApp(root)
    root.mainloop()
