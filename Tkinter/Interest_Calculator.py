import tkinter as tk
from tkinter import messagebox

def calculate_interest():
  if interest_type.get() == 0:
    messagebox.showerror("Error", "Please select an interest type.")
    return
  principal = principal_scale.get()
  rate = rate_scale.get()/100
  time = time_scale.get()
  
  if interest_type.get() == 1:
    interest = principal * rate * time
  else:
    interest = principal * (1 + rate) ** time - principal

  interest_scale.set(interest)

root = tk.Tk()
root.title("Interest Calculator")

principal_label = tk.Label(root, text="Principal(Amount):")
principal_label.pack()
principal_scale = tk.Scale(root, from_=1000, to=100000, orient="horizontal", length=200)
principal_scale.pack()

rate_label = tk.Label(root, text="Rate(%):")
rate_label.pack()
rate_scale = tk.Scale(root, from_=1, to=20, orient="horizontal")
rate_scale.pack()

time_label = tk.Label(root, text="Time(Years):")
time_label.pack()
time_scale = tk.Scale(root, from_=1, to=10, orient="horizontal")
time_scale.pack()

interest_type = tk.IntVar()
simple_interest_radio = tk.Radiobutton(root, text="Simple Interest", variable=interest_type, value=1)
simple_interest_radio.pack()

compound_interest_radio = tk.Radiobutton(root, text="Compound Interest", variable=interest_type, value=2)
compound_interest_radio.pack()

calculate_button = tk.Button(root, text="Calculate", bg = "green", command=calculate_interest)
calculate_button.pack()

interest_label = tk.Label(root, text="Interest:")
interest_label.pack()
interest_scale = tk.Scale(root, from_=0, to=100000, orient="horizontal", length=200)
interest_scale.pack()

root.mainloop()