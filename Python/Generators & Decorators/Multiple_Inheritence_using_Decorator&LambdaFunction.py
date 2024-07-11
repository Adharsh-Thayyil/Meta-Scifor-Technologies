def multiple_inheritance(*base_classes):
  return lambda cls: type(cls.__name__, base_classes, {})

class ClassA:
  def method_a(self):
      print("Method A from ClassA")

class ClassB:
  def method_b(self):
      print("Method B from ClassB")

class ClassC:
  def method_c(self):
      print("Method C from ClassC")

@multiple_inheritance(ClassA, ClassB, ClassC)
class CombinedClass:
  pass

obj = CombinedClass()
obj.method_a()  
obj.method_b()  
obj.method_c() 