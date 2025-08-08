#step 1: create an empty dictionary
my_list = []

#step 2: Append elements to the dictionary
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#step 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)

#step 4: extend the list with another list
my_list.extend([50, 60, 70])

#step 5: remove the last element
my_list.pop()

#step 6: sort the list in ascending order
my_list.sort()

#step 7: find and print the index of element 30
index_30 = my_list.index(30)
print("final list:", my_list)
print("index of 30:", index_30)
