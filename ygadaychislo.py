import os
import questions
import random
import time

def main_ygaday():
    while True:
        answer = random.randint(1,10)
        print('''
Выбери уровень сложности
1 - 7 попыток
2 - 5 попыток
3 - 3 попытки
4 - 1 попытка
''')

        f = input('Ввод: ')

        match f:
            case '1':
                attempts = 7
            case '2':
                attempts = 5
            case '3':
                attempts = 3
            case '4':
                attempts = 1
            case '1748395':
                joke()
            case 'q':
                print(questions.ygaday)
            case 'm' | 'M' | 'м' | 'М':
                break
            case _ :
                print("ошибка")
                continue

        for i in range(attempts):
            print(f'Введите число от одного до десяти, у вас {attempts-i} попыток\n')
            try:
                choice = int(input('Ввод: '))
                if choice == answer:
                    print(f'Поздравляем, вы угадали число {answer}\n')
                    break
                else:
                    print('Вы не угадали число\n')
            except:
                print('число пиши\n')


def joke():
    text = [".......................", "зря ты это сделал", "не хочешь играть по правилам...ну ладно", 
            "я тоже кое-что могу", "я удалю все данные с этого копьютера", '5', '4', '3', '2', '1', 
            "хотя знаешь ты можешь отиграться", "чтобы ты понял, что всё серьёзно, компьютер уже заражён и выйдя из программы",
            "ты автоматически запустишь вирус", "но если сможешь отыграться то я просто самоуничтожусь",
            f'начнём {os.environ["USERNAME"]}', "угадайте случайно заданное число от 1 до 10, у вас 1 попытка ",
            "введите число: ", "поздравляем вы угадали число!", "мы ещё встретимся...\n"]
    
    for i in text:
        if i == "введите число: ":
            input('введи число: ')
            continue
        print(i)
        time.sleep(random.randint(1,2))

