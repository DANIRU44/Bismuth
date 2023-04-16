import os
import questions
import snake
import ygadaychislo

def main_games():
     while True:
        print("""
Выбери игру:
1 - змейка
2 - угадай число
""")

        game = input('Ввод: ')

        match game:
            case '1':
                os.system('cls')
                snake.menu_snake()
            case '2':
                os.system('cls')
                ygadaychislo.main_ygaday()
            case 'q':
                print(questions.games)
            case 'm' | 'M' | 'м' | 'М':
                break
            case _ :
                print("Не корректное значение ")