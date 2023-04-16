import skoroschet
import os
import questions
import sub_count

def main_dev():
    while True:
        print("""
Выбери, интересующий тренажёр:
1 - скоросчёт
2 - замена символов
""")
        match input('Ввод: '):
            case '1':
                os.system('cls')
                skoroschet.main_skoroschet()
            case '2':
                os.system('cls')
                sub_count.main_sub_count()
            case 'q':
                print(questions.development)
            case 'm' | 'M' | 'м' | 'М':
                break
            case _ :
                print("Не корректное значение ")


