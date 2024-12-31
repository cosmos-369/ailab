# dictionary 
my_dict = {
    "name": "sanjay", 
    "age":20, 
    "city": "bellari", 
    "profession": "student"
}

# get by key
def get_by_key(mydict: dict, key):
    try:
        val = mydict[key]
        print(f"value for key {key} : {val}")
    except e: 
        print(f"key {key} not found in dictionary")

# get keys 
def get_keys(mydict: dict): 
    k = mydict.keys()
    print(f"keys of dictionary: {k}")

# get values 
def get_values(mydict: dict): 
    v = mydict.values() 
    print(f"values of dictionary: {v}")

# get items
def get_items(mydict:dict): 
    items = mydict.items() 
    print("keys and values present in dictionary") 
    for key, val in items: 
        print(f"{key} : {val}") 

# iterate 
def iterate_dict(mydict: dict): 
    print("traversing dictionary") 
    for key in mydict: 
        print(f"{key} : {mydict[key]}")

print("initiazied dict:", my_dict) 

get_by_key(my_dict, "name")
get_by_key(my_dict, "age")
get_by_key(my_dict, "city")

get_keys(my_dict)
get_values(my_dict) 
get_items(my_dict) 
iterate_dict(my_dict)