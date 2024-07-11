class Student:
  def __init__(self,name,roll_no,grade,is_on_probation):
    self.name = name
    self.roll_no = roll_no
    self.grade = grade
    self.is_on_probation = is_on_probation

  def display_student(self):
    print(f"Name:{self.name} Roll.No:{self.roll_no} Grade:{self.grade} Probation:{'Yes' if self.is_on_probation else 'No'}")

def display_names(students):
  for student in students:
    print(student.name)


student1 = Student("Adharsh","1","A",True)
student2 = Student("Abhay","2","B",False)
students = [student1,student2]
display_names(students)