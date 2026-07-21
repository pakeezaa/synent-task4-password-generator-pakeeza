import random
import string

def generate_password(length=12):
    if length<4:
        raise ValueError('Password should be of atleast lenght 4')
    
    uppercase=string.ascii_uppercase
    lowercase=string.ascii_lowercase
    digits=string.digits
    special="!@#$%^&*()-_+=[]{};:,.<>?/"

    password_chars= [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]
    all_chars=uppercase+lowercase+digits+special
    password_chars+=[random.choice(all_chars) for _ in range(length-4)]

    random.shuffle(password_chars)
    return "".join(password_chars)