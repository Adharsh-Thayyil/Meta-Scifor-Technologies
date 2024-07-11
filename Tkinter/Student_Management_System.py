import tkinter as tk
from tkinter import messagebox


class Student:
  def __init__(self,name,roll_no,age):
    self.name = name
    self.roll_no = roll_no
    self.age = age


class StudentManagementSystem:
  def __init__(self):
    self.students = []

  def add_student(self,name,roll_no,age):
    self.students.append(Student(name,roll_no,age))
    print("Student added successfully!")
    messagebox.showinfo("Success","Student added successfully")

  def display_students(self):
    display_window = tk.Toplevel(root)
    display_window.title("Student Details")
    display_text = tk.Text(display_window)
    display_text.pack()
    for student in self.students:
      display_text.insert(tk.END,f"Name: {student.name}\nRoll No: {student.roll_no}\nAge: {student.age}\n\n")

  def search_student(self,roll_no):
    for student in self.students:
      if student.roll_no == roll_no:
        messagebox.showinfo("Student Details",f"Name: {student.name}\nRoll No: {student.roll_no}\nAge: {student.age}")
        return
    messagebox.showinfo("Error","Student not found")

  def delete_student(self,roll_no):
    for student in self.students:
      if student.roll_no == roll_no:
        self.students.remove(student)
        messagebox.showinfo("Success","Student deleted successfully")
        return
    messagebox.showinfo("Error","Student not found")

  def update_student(self,roll_no,name,age):
    for student in self.students:
      if student.roll_no == roll_no:
        student.name = name
        student.age = age
        messagebox.showinfo("Success","Student updated successfully")
        return
    messagebox.showinfo("Error","Student not found")

def add_student_clicked():
    name = name_entry.get()
    roll_no = roll_no_entry.get()
    age = age_entry.get()
    if name and roll_no and age:
      sms.add_student(name,roll_no,age)
      name_entry.delete(0,tk.END)
      roll_no_entry.delete(0,tk.END)
      age_entry.delete(0,tk.END)
    else:
      messagebox.showerror("Error","Please enter all the details")

def search_student_clicked():
    roll_no = search_roll_no_entry.get()
    if roll_no:
      sms.search_student(roll_no)
      search_roll_no_entry.delete(0,tk.END)
    else:
      messagebox.showerror("Error","Please enter the roll number")

def delete_student_clicked():
    roll_no = delete_roll_no_entry.get()
    if roll_no:
      sms.delete_student(roll_no)
      delete_roll_no_entry.delete(0,tk.END)
    else:
      messagebox.showerror("Error","Please enter the roll number")

def update_student_clicked():
    roll_no = update_roll_no_entry.get()
    name = update_name_entry.get()
    age = update_age_entry.get()
    if roll_no and name and age:
      sms.update_student(roll_no,name,age)
      update_roll_no_entry.delete(0,tk.END)
      update_name_entry.delete(0,tk.END)
      update_age_entry.delete(0,tk.END)
    else:
      messagebox.showerror("Error","Please enter all the details")

def exit_clicked():
    root.destroy()

sms = StudentManagementSystem()
root = tk.Tk()
root.title("Student Management System")

add_frame = tk.Frame(root)
add_frame.pack()
tk.Label(add_frame,text="Name:").pack(side=tk.LEFT)
name_entry = tk.Entry(add_frame)
name_entry.pack(side=tk.LEFT)
tk.Label(add_frame,text="Roll No:").pack(side=tk.LEFT)
roll_no_entry = tk.Entry(add_frame)
roll_no_entry.pack(side=tk.LEFT)
tk.Label(add_frame,text="Age:").pack(side=tk.LEFT)
age_entry = tk.Entry(add_frame)
age_entry.pack(side=tk.LEFT)

add_button = tk.Button(root,text="Add Student",command=add_student_clicked)
add_button.pack()

display_button = tk.Button(root,text="Display Students",command=sms.display_students)
display_button.pack()

search_frame = tk.Frame(root)
search_frame.pack()
tk.Label(search_frame,text="Enter the Roll No to Search:").pack(side=tk.LEFT)
search_roll_no_entry = tk.Entry(search_frame)
search_roll_no_entry.pack(side=tk.LEFT)

search_button = tk.Button(root,text="Search",command=search_student_clicked)
search_button.pack()

delete_frame = tk.Frame(root)
delete_frame.pack()
tk.Label(delete_frame,text="Enter the Roll No to Delete:").pack(side=tk.LEFT)
delete_roll_no_entry = tk.Entry(delete_frame)
delete_roll_no_entry.pack(side=tk.LEFT)

delete_button = tk.Button(root,text="Delete",command=delete_student_clicked)
delete_button.pack()

update_frame = tk.Frame(root)
update_frame.pack()
tk.Label(update_frame,text="Enter the Roll No to Update:").pack(side=tk.LEFT)
update_roll_no_entry = tk.Entry(update_frame)
update_roll_no_entry.pack(side=tk.LEFT)

tk.Label(update_frame,text="New Name:").pack(side=tk.LEFT)
update_name_entry = tk.Entry(update_frame)
update_name_entry.pack(side=tk.LEFT)

tk.Label(update_frame,text="New Age:").pack(side=tk.LEFT)
update_age_entry = tk.Entry(update_frame)
update_age_entry.pack(side=tk.LEFT)

update_button = tk.Button(root,text="Update",command=update_student_clicked)
update_button.pack()

exit_button = tk.Button(root,text="Exit",command=exit_clicked)
exit_button.pack()

root.mainloop()
