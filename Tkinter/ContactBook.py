import tkinter as tk

def get_selected_contact():
  selected_contact = contact_listbox.curselection()
  if selected_contact:
    details_label.config(text=f"Selected Contact:{contact_listbox.get(selected_contact[0])}")
  else:
    details_label.config(text="No contact selected.")

def add_contact():
  name = name_entry.get()
  number = number_entry.get()
  if name and number:
    contact = f"{name} : {number}"
    index = 0
    while index < contact_listbox.size() and contact_listbox.get(index) < contact:
      index += 1
    contact_listbox.insert(index, contact)
    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)
    details_label.config(text="Conctact added successfully.")
  else:
    details_label.config(text="Please enter a name and number.")

def edit_contact():
  selected_contact = contact_listbox.curselection()
  if selected_contact:
    name = name_entry.get()
    number = number_entry.get()
    if name and number:
      contact_listbox.delete(selected_contact)
      contact_listbox.insert(selected_contact[0], f"{name}:{number}")
      name_entry.delete(0, tk.END)
      number_entry.delete(0, tk.END)
      details_label.config(text="Contact edited successfully.")
    else:
      details_label.config(text="Please enter a name and number.")
  else:
    details_label.config(text="No contact selected.")

def view_contact():
  contacts = "\n".join(contact_listbox.get(0, tk.END))
  details_label.config(text=f"Contacts:\n{contacts}")

def reset_contact():
  name_entry.delete(0, tk.END)
  number_entry.delete(0, tk.END)
  details_label.config(text="Contaact details reset successfully.")

def exit_app():
  root.destroy()

root = tk.Tk()
root.title("Contact Book")

get_btn = tk.Button(root, text="Get Selected Contact", command=get_selected_contact)
get_btn.pack()

add_btn = tk.Button(root, text="Add Contact", command=add_contact)
add_btn.pack()

edit_btn = tk.Button(root, text="Edit Contact", command=edit_contact)
edit_btn.pack()

view_btn = tk.Button(root, text="View Contacts", command=view_contact)
view_btn.pack()

reset_btn = tk.Button(root, text="Reset Field", command=reset_contact)
reset_btn.pack()

exit_btn = tk.Button(root, text="Exit", command=exit_app)
exit_btn.pack()

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

number_label = tk.Label(root, text="Number:")
number_label.pack()
number_entry = tk.Entry(root)
number_entry.pack()

contact_listbox = tk.Listbox(root)
contact_listbox.pack()

details_label = tk.Label(root, text="")
details_label.pack()

root.mainloop()
