# Apples In Dessert Provide Sweet Rich Layers 
# Never Let Clever Monkeys Invent Innovative Solutions

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'c']

# nested list 
print("nested list:")
list3 = [list1, list2]
print(list3) 

# length
print("list lengths:")
print(f"list1: {len(list1)}")
print(f"list2: {len(list2)}")

# concatenation 
print("list concatination:")
print(f"list1+list2={list1+list2}")

# membership 
print("membership:") 
print(f"1 in list1:{1 in list1}")
print(f"1 in list2:{1 in list2}")

# iteration 
print("iteration:") 
print("iterating list1:")
for i in list1:
    print(i) 

# indexing
print("indexing:") 
print(f"list1[4]: {list1[4]}")
print(f"list2[2]: {list2[2]}")

# slicting 
print("slicing:") 
print(f"index 1 to 4 of list1:{list1[1:4]}")

# append 
print("appending:") 
list1.append(6)
print(f"list1 after appending 5: {list1}")

# insert 
print("inserting:")
list2.insert(2, 'z')
print(f"list2 after inserting z at index 2: {list2}")

# deleted 
print("deleting:") 
list1.remove(3)
print(f"list1 after removing 3: {list1}")

# pop 
print("pop:") 
ele = list2.pop() 
print(f"poping element from list:{ele}")
print(f"list2: {list2}")

# sort 
print("sorting: ") 
list2.sort() 
print(f"list2 after sorting: {list2}")

# reverse 
print("reversing: ")
list2.reverse()
print(f"list2 after reversing: {list2}")

# list comprehenstion 
x = [i**2 for i in list1] 
print(f"x:{x}")