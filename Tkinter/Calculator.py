import tkinter as tk
import math

def button_click(symbol):
  current = entry.get()
  entry.delete(0, tk.END)
  entry.insert(0, current + symbol)

def clear():
  entry.delete(0, tk.END)

def calculate():
  expression = entry.get()
  if expression:
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

def square_root():
  value = float(entry.get())
  entry.delete(0, tk.END)
  entry.insert(0, math.sqrt(value))

def square():
  value = float(entry.get())
  entry.delete(0, tk.END)
  entry.insert(0, str(value ** 2))

def sin():
  value = float(entry.get())
  entry.delete(0, tk.END)
  entry.insert(0, str(math.sin(math.radians(value))))

def cos():
  value = float(entry.get())
  entry.delete(0, tk.END)
  entry.insert(0, str(math.cos(math.radians(value))))

def tan():
  value = float(entry.get())
  entry.delete(0, tk.END)
  entry.insert(0, str(math.tan(math.radians(value))))

root = tk.Tk()
root.title("Advanced Calculator")

entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('√', 5, 1), ('x²', 5, 2), ('sin', 5, 3),
    ('cos', 6, 0), ('tan', 6, 1), ('(', 6, 2), (')', 6, 3)
]

for (symbol,row,col) in buttons:
  button = tk.Button(root, text=symbol, padx=20, pady=10, command=lambda s=symbol: button_click(s))
  button.grid(row=row, column=col, padx=5, pady=5)
  if symbol == '=':
    button.config(command=calculate)
  elif symbol == 'C':
    button.config(command=clear)
  elif symbol == '√':
    button.config(command=square_root)
  elif symbol == 'x²':
    button.config(command=square)
  elif symbol == 'sin':
    button.config(command=sin)
  elif symbol == 'cos':
    button.config(command=cos)
  elif symbol == 'tan':
    button.config(command=tan)

root.mainloop()