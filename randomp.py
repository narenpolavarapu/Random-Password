from random import choice
import string

def randompassword(l):
    characters = string.ascii_letters + string.digits
    password = ''.join(choice(characters) for i in range(l))
    return password
print("enter length of the password")
length = int(input(""))
password = randompassword(length)
print("Generating Random Password:", password)