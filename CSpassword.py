#PASSWORD GENERATOR
import random
import string
characters_p=string.ascii_letters +string.digits
len=int(input("Enter the length of password required:"))
password= ''.join(random.choices(characters_p,k=len))
print("YOUR PASSWORD: ",password)


