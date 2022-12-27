
ch=int(input("Enter your choice (number only) :"))

# function to print inverting pyramid
def starPyramid(n):
  for i in range(n):
    print(' '*(i) + '* '*(n-i))

if ch==1:
  n=5 #no.of rows
  starPyramid(n)  
  for i in range(1,n):
    print(' '*(n-i-1) + '- '*(i+1))
elif ch==2:
  starPyramid(5)
else:
  print("Invalid Input")

   

