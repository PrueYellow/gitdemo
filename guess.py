import random

number = []

#使用無窮迴圈   
while True:
 x = random.randint(1,49)
 if x not in number:     
    number.append(x)
 if len(number) == 6:
    print(sorted(number),end =" ")
    break
   


y = random.randint(1,49)
print(f"特別號: {y}")