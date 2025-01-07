list1 = [1, 2, 3]

# add
def add_element(ls:list, idx:int, ele): 
    ls.insert(idx, ele)
    print(f"list after adding element:{ele} at index:{idx} => {ls}")

# append 
def append_element(ls: list, ele): 
    ls.append(ele)
    print(f"list after appending element:{ele} => {ls}")

# extend
def extend_list(ls1:list, ls2:list): 
    ls1.extend(ls2)
    print(f"list after extending: {ls1}")

# delete
def delete_element(ls:list, idx:int): 
    try: 
        del ls[idx]
        print(f"list after deleting: {ls}")
    except e: 
        print("index out of range")
        print(f"list is unchanged: {ls}")

add_element(list1, 0, -1) 
append_element(list1, 6) 
extend_list(list1, [8, 9, 10])
delete_element(list1, 0)
