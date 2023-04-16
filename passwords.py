import os
import questions
import string
import random

сhars = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation

def main_passwords():
    os.system('cls')
    while True:
        
        length = input('Длина пароля: ')
        if length.isdigit():
            length = int(length)
        elif  length == 'q':
            print(questions.passwords)
        elif length in ['m','M','м','М']:
            break
        else:
            print('Не корректное значение')
            continue
            
 
        password = ''
        for _ in range(length):
            password += random.choice(сhars)
            
        print(f'\n{password}\n')
        print("""Еще раз?
1 - да 
2 - нет""")

        match input('Ввод: '):
            case '1':
                main_passwords()
            case _ :
                break


