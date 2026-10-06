import tkinter as tk

score = 0
num1 = 0
num2 = 0

def summ():
    result = num1 + num2
    print(f"Ответ:{result}")

def diff():
    result = num1 - num2
    print(f"<UNK>:{result}")

def division():
    result = num1 / num2
    print(f"<UNK>:{result}")

def multiplication():
    result = num1 * num2
    print(f"<UNK>:{result}")

def exponentiation():
    result = num1 ** num2
    print(f"<UNK>:{result}")

def start():
    global score
    score += 1
    label.config(text=str(score))
    print("Hello")

root = tk.Tk()

root.geometry("500x500")

header = tk.Frame(root, bg="black", height=100, width=200)
header.pack(side="top", fill="x")

main = tk.Frame(root, bg="light blue", height=300, width=300)
main.pack(side='bottom', fill='x')

footer = tk.Frame(root, bg="black", height=100, width=200)
footer.pack(side="bottom", fill="x")

button_start = tk.Button(main, text="start", command=start)
button_start.pack()

button_summ = tk.Button(main, text="sum", command=summ)
button_summ.pack()

button_division = tk.Button(main, text="division", command=division)
button_division.pack()

button_multiply = tk.Button(main, text="multiplication", command=multiplication)
button_multiply.pack()

button_exponentiation = tk.Button(main, text="exponentiation", command=exponentiation)
button_exponentiation.pack()

button_diff = tk.Button(main, text="diff", command=diff)
button_diff.pack()

label = tk.Label(root, text="Hello World")
label.pack()

root.mainloop()
