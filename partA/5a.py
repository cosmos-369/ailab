# string count 
def string_count(s1:str, s2:str): 
    c = s1.count(s2)
    print(f"string `{s2}` is present {c} time in string `{s1}`")

s1 = "hello hello" 
s2 = "he" 
string_count(s1, s2)