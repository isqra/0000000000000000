import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
list_buttons =  []

bottom_frame=tk.Frame(root, height=50, width=50, bg="white", padx=10, pady=10)

for i in range(10):
    b = (tk.Button(bottom_frame))
    b.pack(side="left")
    b.config(text=str(i))


root.mainloop()