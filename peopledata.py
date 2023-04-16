from mimesis import Person
import os
import questions

def main_persondata():
    while True:
        person = Person()
        print(f"""
Случайно сгенерированная карточка:

Имя: {person.full_name()}
Возраст: {person.age()}
Пол: {person.gender()}
Рост: {person.height()}
Вес: {person.weight()}
Образование: {person.academic_degree()}
Группа крови: {person.blood_type()}
Язык: {person.language()}
Национальность: {person.nationality()}
Профессия: {person.occupation()}

Еще раз?
1 - да
любая другая кнопка - нет
""")
        c = input('Ввод: ')
        match c:
            case '1':
                pass
            case 'q':
                print(questions.persondata)
            case _ :
                break
        
def username():
    user = Person()
    while True:
        print(f"""Твой ник: {user.username()}

Еще раз?
1 - да 
любая другая кнопка - нет
""")
        c = input('Ввод: ')
        match c:
            case '1':
                pass
            case 'q':
                print(questions.username)
            case _ :
                break

        os.system('cls')

