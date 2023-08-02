import random
import string
numbers = string.digits
special_chars=string.punctuation
lower=string.ascii_lowercase
upper=string.ascii_uppercase
chars=[numbers, special_chars, lower, upper]
all_chars=numbers+special_chars+lower+upper
password_length= int(input("Enter the password length:"))
while password_length< 4:
    print("Password must contain at least 4 characters as it must contain at least 1 character from each category")
    password_length=int(input("Enter the password length:"))
password = ""
for j in range(4):
    for i in range(1):
        password+=chars[j][random.randint(0, len(chars[j])-1)]
for i in range(1, password_length-3):
    if len(password)<password_length:
        password+=(random.choice(all_chars))
print(password)
