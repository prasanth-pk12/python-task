
# Custom Exception by inheriting Exception class
class IndexError(Exception):
   def __init__(self,msg):
      self.msg=msg
   def __str__(self):
      return self.msg

# Given list
list_a = [1,2,3,4,5]

try:
  # raising ValueError exception when non-int input
  try:
    index = int(input("Enter the index : "))
  except ValueError as err:
    raise ValueError("Use an Integer value as the input.")
  
  # raising IndexError exception when index out of bounds 
  if index >= len(list_a):
    raise IndexError(f"The index {index} is incorrect and index should lie between -5 and 4. ")
    print(list_a[index])

# catch and print exception
except (IndexError,ValueError) as err:
  print(err)

