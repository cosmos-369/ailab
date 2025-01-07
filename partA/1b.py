num = int(input("enter a number: ")) 
prime = True
for i in range(2, num // 2): 
    if num % i == 0: 
        prime = False 
        break 

if prime: 
    print(f"{num} is prime..!")
else:
    print(f"{num} is not prime..!")