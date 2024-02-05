import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import os

# Function to convert a video to ASCII frames
def convert_to_ascii(video_file, output_folder, mode):
    if not output_folder:
        messagebox.showerror("Error", "Please enter a folder name.")
        return
    
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    
    cap = cv2.VideoCapture(video_file)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if mode == "PNG":
            frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
            cv2.imwrite(frame_filename, gray_frame)
        elif mode == "TXT":
            ascii_frame = ""
            for row in gray_frame:
                for pixel_value in row:
                    ascii_frame += "@MNHX80WM#*+=-:. "[pixel_value // 25]
                ascii_frame += "\n"

            with open(os.path.join(output_folder, f"frame_{frame_count:04d}.txt"), "w") as txt_file:
                txt_file.write(ascii_frame)

        frame_count += 1

    cap.release()
    messagebox.showinfo("Conversion Complete", "Video to ASCII conversion completed.")

# Function to handle the "Browse" button
def browse_video_file():
    file_path = filedialog.askopenfilename()
    video_file_entry.delete(0, tk.END)
    video_file_entry.insert(0, file_path)

# Function to handle the "Convert" button
def convert_video():
    video_file = video_file_entry.get()
    output_folder = output_folder_entry.get()
    mode = mode_var.get()

    convert_to_ascii(video_file, os.path.join(os.path.expanduser('~'), 'Desktop', output_folder), mode)

# Create the main window
root = tk.Tk()
root.title("Video to ASCII Converter")

# Set a dark mode theme for the GUI
root.tk_setPalette(background='#000000', foreground='#FFFFFF')

# Create and pack widgets
video_file_label = tk.Label(root, text="Select Video File:")
video_file_label.pack()

video_file_entry = tk.Entry(root, width=50)
video_file_entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_video_file)
browse_button.pack()

output_folder_label = tk.Label(root, text="Enter Output Folder Name:")
output_folder_label.pack()

output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.pack()

mode_label = tk.Label(root, text="Select ASCII Mode:")
mode_label.pack()

mode_var = tk.StringVar()
mode_var.set("PNG")
mode_png_radio = tk.Radiobutton(root, text="PNG", variable=mode_var, value="PNG")
mode_txt_radio = tk.Radiobutton(root, text="TXT", variable=mode_var, value="TXT")
mode_png_radio.pack()
mode_txt_radio.pack()

convert_button = tk.Button(root, text="Convert", command=convert_video)
convert_button.pack()

# Start the GUI main loop
root.mainloop()
