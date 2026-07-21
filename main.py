from password_generator import generate_password
from utils import get_password_length,get_password_count

def main():
    print('-'*40)
    print('     Password Generator')
    print('-'*40)

    length=get_password_length()
    count=get_password_count()
    print('\nGenerated Password(s):')
    for i in range(count):
        print(f'{i+1}. {generate_password(length)}')

if __name__ == "__main__":
    main()

