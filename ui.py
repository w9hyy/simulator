import Tkinter as tk
window = tk.Tk()


label=tk.Label(text='privet', fg='green', bg='yellow', width=20, height=20)
label.pack()

button=tk.Button(text='hi', fg='red', bg='blue', width=10, height=5)
button.pack()

entry=tk.Entry()
entry.pack()

def handler_button():
    print(entry.get())

button['command']=handler_button







window.mainloop()

