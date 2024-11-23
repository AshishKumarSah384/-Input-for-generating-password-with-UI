import tkinter as tk

def open_popup():
    popup = tk.Toplevel(root)  # Create a new window
    popup.title("Popup Window")
    popup.geometry("200x100")
    tk.Label(popup, text="This is a popup!", font=("Arial", 12)).pack(pady=10)
    tk.Button(popup, text="Close", command=popup.destroy).pack(pady=5)

root = tk.Tk()
root.title("Main Window")
root.geometry("300x200")

tk.Button(root, text="Open Popup", command=open_popup).pack(pady=20)

root.mainloop()
