import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

PLUGIN_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_PYTHON = os.path.join(PLUGIN_DIR, "venv", "Scripts", "python.exe")  # macOS/Linux: "venv/bin/python"
MASK_SCRIPT = os.path.join(PLUGIN_DIR, "magic_mask.py")

def run_magic_mask():
    video_path = filedialog.askopenfilename(
        title="Select Video Clip to Mask",
        filetypes=[("Video Files", "*.mp4 *.mov *.mkv *.avi")]
    )
    if not video_path:
        return

    status_label.config(text="Select subject in popup window, then press SPACE...")
    root.update()

    try:
        subprocess.run([VENV_PYTHON, MASK_SCRIPT, video_path], check=True)
        matte_path = video_path.rsplit(".", 1)[0] + "_matte.mp4"
        status_label.config(text=f"Done! Saved: {os.path.basename(matte_path)}")
        messagebox.showinfo("Magic Mask Complete", f"Matte generated:\n{matte_path}\n\nDrag this file into your Media Pool.")
    except Exception as e:
        status_label.config(text="Error generating mask.")
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Magic Mask Free (SAM 2)")
root.geometry("360x160")
root.attributes("-topmost", True)

tk.Label(root, text="AI Magic Mask for DaVinci Resolve Free", font=("Arial", 11, "bold")).pack(pady=10)
tk.Button(root, text="Select Clip & Create Mask", command=run_magic_mask, height=2, width=25).pack(pady=5)
status_label = tk.Label(root, text="Ready", fg="gray")
status_label.pack(pady=10)

root.mainloop()
