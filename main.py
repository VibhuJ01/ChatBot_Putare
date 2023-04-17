from tkinter import *
from Query_Analysis import Query

import pyttsx3
speech = pyttsx3.init()
speech.setProperty("rate", 150)


def analyse(output_screen,name_entry):
    output_screen.config(state=NORMAL)
    output = Query(name_entry.get())
    
    output_screen.insert(END, output +'\n\n')
    output_screen.config(state=DISABLED)
    
    speech.say(output)
    speech.runAndWait()
    
def clear(x):
    x.delete(0, END)

    
def main():
    # Setup Root
    root = Tk(className='AI - ChatBot')
    root.title("Brother")
    root.geometry("970x650")

    # Label and Entry Field
    Label(root, text="Query:").grid(row=0, column=0)
    name_entry = Entry(root, width=90)
    name_entry.grid(row=1, column=3)

    # Output Screen
    output_screen = Text(root, height=30, width=90)
    output_screen.grid(row=5, column=3)
    output_screen.config(state=DISABLED)

    # Buttons 
    Button(root,height=2, width=10, text="Compute", command=lambda: analyse(output_screen,name_entry)).grid(row=4, column=3)
    Button(root,height=2, width=10, text="Clear Input", command=lambda: clear(name_entry)).grid(row=4, column=2)
    Button(root,height=2, width=10, text="Clear Output", command=lambda: clear(output_screen)).grid(row=4, column=4)
    
    root.mainloop()

if(__name__ == '__main__'):
    main()
