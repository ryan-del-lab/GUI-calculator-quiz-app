import tkinter as tk

def click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


root = tk.Tk()
root.title("COS102 Calculator")
root.geometry("350x500")
root.configure(bg="black")

# Display screen
entry = tk.Entry(
    root,
    font=("Arial", 24),
    bg="black",
    fg="white",
    justify="right",
    bd=8,
    insertbackground="white"
)

entry.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=20,
    sticky="nsew"
)

buttons = [

    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)

]

for (text,row,col) in buttons:

    if text == 'C':
        button = tk.Button(
            root,
            text=text,
            font=("Arial",16,"bold"),
            bg="darkorange",
            fg="white",
            width=5,
            height=2,
            command=clear
        )

    elif text == '=':
        button = tk.Button(
            root,
            text=text,
            font=("Arial",16,"bold"),
            bg="orange",
            fg="white",
            width=5,
            height=2,
            command=calculate
        )

    elif text in ['+','-','*','/']:
        button = tk.Button(
            root,
            text=text,
            font=("Arial",16,"bold"),
            bg="#FF6A00",
            fg="white",
            width=5,
            height=2,
            command=lambda t=text: click(t)
        )

    else:
        button = tk.Button(
            root,
            text=text,
            font=("Arial",16),
            bg="#2E2E2E",
            fg="white",
            width=5,
            height=2,
            command=lambda t=text: click(t)
        )

    button.grid(
        row=row,
        column=col,
        padx=5,
        pady=5
    )

for i in range(5):
    root.grid_rowconfigure(i, weight=1)

for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()