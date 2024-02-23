import tkinter as tk
import subprocess

# Define functions to run other scripts
def take_attendance():
    subprocess.run(["python", "main.py"])

def new_student():
    subprocess.run(["python", "new_student.py"])

# Define function to close the app
def close_app():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("ATTENDANCE SYSTEM")

# Set the initial size of the window to 720p
window.geometry("1280x720")

# Set the background color to blue
window.config(bg="blue")

# Create the frame with padding
frame = tk.Frame(window, bg="lightblue", padx=10, pady=10)
frame.pack(fill="both", expand=True)

# Create the "Take Attendance" button with larger text, padding, and green color
take_attendance_button = tk.Button(
    frame,
    text="Take Attendance",
    command=take_attendance,
    font=("Arial", 14),
    padx=15,
    pady=15,
    bg="green",
    fg="white",
)
take_attendance_button.pack(side="left")

# Create the "New Student" button with similar formatting
new_student_button = tk.Button(
    frame,
    text="New Student",
    command=new_student,
    font=("Arial", 14),
    padx=15,
    pady=15,
    bg="green",
    fg="white",
)
new_student_button.pack(side="right")

# Center the buttons within the frame
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Add spacing between buttons
take_attendance_button.pack(pady=10)
new_student_button.pack(pady=10)

# Bind escape key to close_app function
window.bind('<Escape>', close_app)

# Start the main loop
window.mainloop()