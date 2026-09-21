import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

# 1. Create your other widgets first
button = tk.Button(root, text="I will be covered by the label", font=("Arial", 14))
button.pack(pady=50)

# 2. Create the floating label
label = tk.Label(root, text="I'm on top!", bg="yellow", relief="solid", bd=1)

# 3. Force it to the top layer
label.lift() 

# 4. Use your bulletproof follow function from before
def follow_mouse(event):
    window_x = event.x_root - root.winfo_rootx()
    window_y = event.y_root - root.winfo_rooty()
    label.place(x=window_x + 10, y=window_y + 15)

root.bind("<Motion>", follow_mouse)
root.mainloop()
