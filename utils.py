def get_password_length():
    while True:

        length_input=input(
        "Enter password length (minimum 4,default 12):"
    ).strip()
        if length_input=="":
            return 12
        if length_input.isdigit():
            length=int(length_input)
        if length>=4:
            return length
        
        print('please enter a valid number ( 4 or greater)\n')

def get_password_count():
    count_input=input(
        'how many password you want to generate ? (default 1)\n'
    ).strip()
    if count_input.isdigit() and int(count_input) >0:
        return int(count_input)
    return 1
