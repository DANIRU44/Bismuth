import time
import random
import os
import questions
# import matplotlib as mpl
import matplotlib.pyplot as plt

choice = ''
result = 0
average_value = 0

def main_skoroschet():
    global choice
    while True:
        print("""
Какой режим?
1 - стандартный (50)
2 - произвольный
3 - посмотреть результаты
""")
        choice = input('Ввод: ')

        match choice:
            case '1' | '2':
                start()
            case '3':
                read_results() 
            case 'q':
                print(questions.skoroschet)
            case 'm' | 'M' | 'м' | 'М':
                break
        

def start():
    global result
    global average_value
    if choice == '2':
        r = int((input("Cколько попыток? ")))
    else : 
        r = 50

    print(f'''
Сейчас будут последовательно выводиться {r} математических примеров типа 1 + 5 - 3.
Твоя задача решить пример в голове и просто нажать enter чтобы показать следующий
''')
    pl=["+", "-"]
    print("Нажми на enter чтобы начать")
    input()
    start = time.time()
    for i in range(r):
        os.system('cls')
        print(random.randint(1,9), random.choice(pl), random.randint(1,9), random.choice(pl), random.randint(1,9))
        input()
    end = time.time()

    result = round(end - start, 1)
    average_value = round(result/r, 2)

    if choice == '1':
        print(f"Потрачено вренени: {round(end - start, 1)} секунды")
    else:
        print(f'В среднем на один пример: {round(result/r, 2)}')
    save_result()


def save_result():
    print("""
Сохранить результат?

1 - да
2 - нет
3 - открыть графики
""")
    match input('Ввод: '):
        case '1':
            global choice
            global result
            global average_value

            if choice == '1':
                with open('default_skor.txt','a') as f:
                    f.write(f'{result}\n')
            else:
                with open('average_skor.txt','a') as f:
                    f.write(f'{average_value}\n')

        case '2':
            pass
        case '3':
            read_results()
        case 'q':
            print(questions.skor_save)
        case _ :
            print('Не корректное значение')
            save_result()
            
def read_results():
    graf_one = []
    graf_two = []

    with open('default_skor.txt', 'r') as file:
        for line in file.readlines():
            graf_one.append(line)
        graf_one = [float(i.rstrip()) for i in graf_one]


    with open('average_skor.txt', 'r') as file:
        for line in file.readlines():
            graf_two.append(line)
        graf_two = [float(i.rstrip()) for i in graf_two]

    fig, ax = plt.subplots(2,1, figsize=(10, 6))
    ax[0].plot([i+1 for i in range(len(graf_one))], graf_one)
    ax[1].plot([i+1 for i in range(len(graf_two))], graf_two)

    ax[0].set_xlabel('Попытки')
    ax[0].set_ylabel('Время')
    ax[1].set_xlabel('Попытки')
    ax[1].set_ylabel('Среднее время на один пример')

    ax[0].grid(True)
    ax[1].grid(True)
    plt.show()

