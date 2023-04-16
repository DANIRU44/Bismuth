import os
import questions
import passwords
import peopledata

def main_gen():
    while True:
        print("""
Выбери, интересующий генератор:
1 - пароли
2 - ники
3 - данные людей
""")

        tren = input('Ввод: ')

        match tren:
            case '1':
                os.system('cls')
                passwords.main_passwords()
            case '2':
                os.system('cls')
                peopledata.username()
            case '3':
                os.system('cls')
                peopledata.main_persondata()
            case 'q':
                print(questions.generators)
            case 'm' | 'M' | 'м' | 'М':
                break
            case _ :
                print("Не корректное значение ")