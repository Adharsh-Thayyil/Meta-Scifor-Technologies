class MyList:
    def __init__(self, data):
      self.data = data

    def append(self, item):
      self.data.append(item)

    def insert(self, index, item):
      self.data.insert(index, item)

    def remove(self, item):
      self.data.remove(item)

    def pop(self, index):
      return self.data.pop(index)

    def clear(self):
      self.data.clear()

    def reverse(self):
      self.data.reverse()

    def sort(self, key = None, reverse = False ):
      self.data.sort(key = key, reverse = reverse)

    def __repr__(self):
      return repr(self.data)

my_list = MyList([1, 2, 3, 4, 5])
print(my_list)

my_list.append(6)
print(my_list)

my_list.insert(2, 7)
print(my_list)

my_list.remove(3)
print(my_list)

item = my_list.pop(1)
print(item)
print(my_list)

my_list.reverse()
print(my_list)