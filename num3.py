import random
import string

def make_password_generator(length):
    def generator():
        char = string.ascii_letters + string.digits
        password = ''.join(random.choice(char) for i in range(length))
        return password
    return generator

gen = make_password_generator(8)
print(gen())
print(gen())
print(gen())