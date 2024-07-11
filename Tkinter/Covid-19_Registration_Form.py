import tkinter as tk
from tkinter import messagebox

def covid_Reg_Form():
  name = entry_name.get()
  age = entry_age.get()
  gender = gender_var.get()
  address = entry_address.get("1.0", tk.END)
  email = entry_email.get()
  contact = entry_contact.get()
  country = entry_country.get()
  state = entry_state.get()
  symptoms = [symptom.get() for symptom in symptoms_vars]

  if not all([name, age, gender, address, email, contact, country, state, any(symptoms)]):
    messagebox.showerror(title="Error", message="Please fill in all the fields.")
  else:
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Address:", address)
    print("Email:", email)
    print("Contact No:", contact)
    print("Country:", country)
    print("State:", state)
    print("Symptoms:", symptoms)
    messagebox.showinfo(title="Registration Successful", message="Registration successful! Form Submitted Successfully.")

root = tk.Tk()
root.title("Covid Vaccine Registration Form")
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w")
tk.Label(root, text="Age:").grid(row=1, column=0, sticky="w")
tk.Label(root, text="Gender:").grid(row=2, column=0, sticky="w")
tk.Label(root, text="Address:").grid(row=3, column=0, sticky="w")
tk.Label(root, text="Email:").grid(row=4, column=0, sticky="w")
tk.Label(root, text="Contact No:").grid(row=5, column=0, sticky="w")
tk.Label(root, text="Country:").grid(row=6, column=0, sticky="w")
tk.Label(root, text="State:").grid(row=7, column=0, sticky="w")
tk.Label(root, text="Symptoms:").grid(row=8, column=0,sticky="w")

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)
gender_var = tk.StringVar()
gender_var.set("Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=1, sticky="e")
entry_address = tk.Text(root, height=5, width=30)
entry_address.grid(row=3, column=1)
entry_email = tk.Entry(root)
entry_email.grid(row=4, column=1)
entry_contact = tk.Entry(root)
entry_contact.grid(row=5, column=1)
entry_country = tk.Entry(root)
entry_country.grid(row=6, column=1)
entry_state = tk.Entry(root)
entry_state.grid(row=7, column=1)
symptoms_labels = ["cold","cough","fever","headache"]
symptoms_vars = [tk.BooleanVar() for i in symptoms_labels]
for i in range(len(symptoms_labels)):
  tk.Checkbutton(root, text=symptoms_labels[i], variable=symptoms_vars[i]).grid(row=8+i//2, column=1+i%2, sticky="w")

submit_button = tk.Button(root, text="Submit", command=covid_Reg_Form)
submit_button.grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()