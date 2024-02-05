import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import os

# Function to play frames from a folder
def play_frames(frame_folder, frame_rate):
    frame_files = sorted([f for f in os.listdir(frame_folder) if f.endswith(".png")])
    if not frame_files:
        return
    
    for frame_file in frame_files:
        frame_path = os.path.join(frame_folder, frame_file)
        frame = cv2.imread(frame_path)
        
        cv2.imshow("Frame Viewer", frame)
        if cv2.waitKey(int(1000 / frame_rate)) & 0xFF == 27:
            break
    
    cv2.destroyAllWindows()
    ask_to_exit()

# Function to handle the "Browse" button
def browse_frame_folder():
    folder_path = filedialog.askdirectory()
    frame_folder_entry.delete(0, tk.END)
    frame_folder_entry.insert(0, folder_path)

# Function to handle the "Play" button
def play_frames_button():
    frame_folder = frame_folder_entry.get()
    frame_rate = frame_rate_var.get()

    play_frames(frame_folder, frame_rate)

# Function to ask the user to press a key to exit
def ask_to_exit():
    root.unbind('<Key>')
    root.bind('<Key>', lambda event: root.destroy())
    messagebox.showinfo("Playback Complete", "Press any key to exit playback.")

# Create the main window
root = tk.Tk()
root.title("Frame Player")

# Set a dark mode theme for the GUI
root.tk_setPalette(background='#000000', foreground='#FFFFFF')

# Create and pack widgets
frame_folder_label = tk.Label(root, text="Select Frame Folder:")
frame_folder_label.pack()

frame_folder_entry = tk.Entry(root, width=50)
frame_folder_entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_frame_folder)
browse_button.pack()

frame_rate_label = tk.Label(root, text="Frame Rate (fps):")
frame_rate_label.pack()

frame_rate_var = tk.DoubleVar()
frame_rate_var.set(30.0)  # Default frame rate

frame_rate_entry = tk.Entry(root, textvariable=frame_rate_var)
frame_rate_entry.pack()

play_button = tk.Button(root, text="Play Frames", command=play_frames_button)
play_button.pack()

# Start the GUI main loop
root.mainloop()
