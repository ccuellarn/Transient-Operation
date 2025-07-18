from tkinter import Tk, Label, Button
window = Tk()
window.geometry('400x300')
window.title('My first app')

label = Label(window,text='Planner For Astronomical Observations')
label.pack()

def message():
    print('Hello User')
button = Button(window,text='Say Hello',command=message)
button.config(fg='purple',bg='orange')
button.pack()

window.mainloop()
