import tkinter as tk
from tkinter import messagebox

def student_form():
  name = name_entry.get()
  age = age_entry.get()
  address = address_entry.get()
  gender = gender_var.get()
  email = email_entry.get()
  
  print("Name:", name)
  print("Age:", age) 
  print("Address:", address)
  print("Gender:", gender)
  print("Email:", email)

  if name and age and gender and address and email:
    messagebox.showinfo("Success", "Student registered successfully!")
    
  else:
    messagebox.showerror("Error", "Please fill in all fields.")
  

root = tk.Tk()
root.title("Student Registration Form")

name_frame = tk.Frame(root)
name_frame.pack(padx=10, pady=5)
name_label = tk.Label(name_frame, text="Name:")
name_label.place(x=100, y=10)
name_label.pack(side="left")
name_entry = tk.Entry(name_frame)
name_entry.pack(side="right")

age_frame = tk.Frame(root)
age_frame.pack(padx=10, pady=5)
age_label = tk.Label(age_frame, text="Age:")
age_label.pack(side="left")
age_entry = tk.Entry(age_frame)
age_entry.pack(side="right")

address_frame = tk.Frame(root)
address_frame.pack(padx=10, pady=5)
address_label = tk.Label(address_frame, text="Address:")
address_label.pack(side="left")
address_entry = tk.Entry(address_frame)
address_entry.pack(side="right")

gender_frame = tk.Frame(root)
gender_frame.pack(padx=10, pady=5)
gender_label = tk.Label(gender_frame, text="Gender:")
gender_label.pack(side="left")
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male")
male_radio.pack(side="left")
female_radio = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female")
female_radio.pack(side="left")
others_radio = tk.Radiobutton(gender_frame, text="Others", variable=gender_var, value="Others")
others_radio.pack(side="left")

email_frame = tk.Frame(root)
email_frame.pack(padx=10, pady=5)
email_label = tk.Label(email_frame, text="Email:")
email_label.pack(side="left")
email_entry = tk.Entry(email_frame)
email_entry.pack(side="right")


submit_button = tk.Button(root, text="Submit", command=student_form, bg="green")
submit_button.pack(padx=10, pady=10)

root.mainloop()