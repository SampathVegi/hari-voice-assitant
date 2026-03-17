import tkinter as tk

root = tk.Tk()
root.title("Test GUI")
root.geometry("400x200")

label = tk.Label(root, text="GUI is working ✅", font=("Arial", 16))
label.pack(pady=50)

root.mainloop()
