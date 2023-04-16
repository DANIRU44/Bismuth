import random
import os
import questions
# import matplotlib as mpl
import matplotlib.pyplot as plt

SYMBOLS = ['#', '$', '@', '■', '♣', '♦', '&', '₩']
OPERATION = ['+', '-', '*']
NUMS = [1,2,3,4,5,6,7,8,9]
N = 10
answers = []
choice = ''

def main_sub_count():
    global choice
    while True:
        try:
            print("""
Какой режим?
1 - стандартный (30)
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
                    print(questions.sub_count)
                case 'm' | 'M' | 'м' | 'М':
                    break
                case _ :
                    print('Не корректное значение')
        finally:
            main_sub_count()



def start():
    global N
    global answers
    
    if choice == '2':
        N = int((input("Cколько попыток? ")))
    print(f'''
Сейчас будут последовательно выводиться {N} примеров,
тебе необходимо будет в голове переводить из символа в математический знак и написать ответ.
Учитывается время и количество правильных ответов.
Если введёшь не число, то тест будет прерван.
''')


    association = [(SYMBOLS.pop(random.randint(0, len(SYMBOLS)-1)), OPERATION.pop(random.randint(0, len(OPERATION)-1))) for _ in range(3)]

    tabl = f"""
             +-----------+
      Было   | {association[0][1]} | {association[1][1]} | {association[2][1]} |
             +---+---+---+
      Стало  | {association[0][0]} | {association[1][0]} | {association[2][0]} |
             +-----------+
    """
    print(tabl)
    input('Нажми enter, чтобы начать')
    
    for _ in range(N):
        os.system('cls')
        print(tabl)

        a, b = random.choice(association)
        first, second = random.choice(NUMS), random.choice(NUMS)
        answer = int(eval(f'{first}{b}{second}'))
        user_ans = int(input(f'{first} {a} {second} = '))

        answers.append(answer == user_ans)

    input()
    os.system('cls')
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
            global N
            global answers

            if choice == '1':
                with open('default_sub.txt','a') as f:
                    f.write(f'{round(answers.count(True)/N, 1) * 100}\n')
            else:
                with open('average_sub.txt','a') as f:
                    f.write(f'{round(answers.count(True)/N, 1) * 100}\n')

        case '2':
            pass
        case '3':
            read_results()
        case 'q':
            print(questions.sub_count_save)
        case _ :
            print('Не корректное значение')
            save_result()
            
def read_results():
    graf_one = []
    graf_two = []

    with open('default_sub.txt', 'r') as file:
        for line in file.readlines():
            graf_one.append(line)
        graf_one = [float(i.rstrip()) for i in graf_one]


    with open('average_sub.txt', 'r') as file:
        for line in file.readlines():
            graf_two.append(line)
        graf_two = [float(i.rstrip()) for i in graf_two]

    fig, ax = plt.subplots(2,1, figsize=(10, 6))
    ax[0].plot([i+1 for i in range(len(graf_one))], graf_one)
    ax[1].plot([i+1 for i in range(len(graf_two))], graf_two)

    ax[0].set_xlabel('Попытки')
    ax[0].set_ylabel('% привильных (стандартный)')
    ax[1].set_xlabel('Попытки')
    ax[1].set_ylabel('% правильных (произвольный)')

    ax[0].grid(True)
    ax[1].grid(True)
    plt.show()

    print(graf_one)
    print(graf_two)

