t_1=(1,4,9,16,25,36)
print("t_1:",t_1)

t_modified = tuple((i**2 for i in t_1 ))
print("t_modified:",t_modified)

print("Element at index position 4 of t-modified:",t_modified[4])

print("t_sliced:",t_modified[slice(1,4)])
