# set operatiosn 

seta = {1, 2, 3, 4}
setb = {4, 5, 6, 7} 

# union
def union_sets(a:set, b:set): 
    c = a.union(b) 
    print(f"union of sets: {c}")

# intersection 
def intersection_sets(a:set, b:set): 
    c = a.intersection(b) 
    print(f"intersection of sets: {c}") 

# difference
def difference_sets(a:set, b:set): 
    c = a.difference(b) 
    print(f"setA - setB = {c}")

# symmetric difference 
def symmetric_diff_sets(a:set, b:set): 
    c = a.symmetric_difference(b) 
    print(f"symmetric difference of sets: {c}")

# subset
def subset_sets(a:set, b:set): 
    c = a.issubset(b) 
    print(f"is A subset of B: {c}")

# superset
def superset_sets(a:set, b:set): 
    c = a.issuperset(b) 
    print(f"is A superset of B: {c}") 

# disjoint
def disjoint_sets(a:set, b:set): 
    c = a.isdisjoint(b) 
    print(f"is set A and set B disjoint sets: {c}")

print("set A:", seta)
print("set B:", setb) 

union_sets(seta, setb) 
intersection_sets(seta, setb) 
difference_sets(seta, setb) 
symmetric_diff_sets(seta, setb) 
subset_sets(seta, setb) 
superset_sets(seta, setb) 
disjoint_sets(seta, setb) 