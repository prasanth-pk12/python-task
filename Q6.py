
list_a= ['car' ,'tree','place','under','grass','price']

remove_items_containing_a_or_A = lambda str :  list_a.remove(str)

for el in list_a:
  if 'a' in el.lower():
     remove_items_containing_a_or_A(el)

print(list_a) 
