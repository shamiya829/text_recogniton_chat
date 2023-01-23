import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
root.configure(bg = "white")

display = tk.Text(root, state = "disabled", yscrollcommand = tk.Scrollbar(root).set, height=200)
display.pack(expand = True, fill = tk.BOTH)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

textbox = tk.Text(root, yscrollcommand = scrollbar.set, height=100)
textbox.insert(tk.INSERT, "Type your message here...")
textbox.place(relx=0.4, rely=0.90, anchor=tk.S, width=400, height=100)

button = tk.Button(root, text = "Send", bg = "blue", command = lambda: print("Your message was sent!"))
button.configure(bg = "black")
button.place(relx=0.85, rely=0.90, anchor=tk.S, width=100, height=50)


root.mainloop()
