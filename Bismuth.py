import sys, os
import ultracryptographer
import questions
import development
import generators
import screenrecording
import games

os.system("cls")

if os.path.exists('default_skor.txt') or os.path.exists('average_skor.txt') or os.path.exists('default_sub.txt') or os.path.exists('average_sub.txt') or os.path.exists('snake.json') != True:
    with open('default_skor.txt','a') as f:
        f.close()
    with open('average_skor.txt','a') as f:
        f.close()
    with open('default_sub.txt','a') as f:
        f.close()
    with open('average_sub.txt','a') as f:
        f.close()
    with open('snake.json', 'a') as f:
        f.close()

def start_select():
    print('''
Выбери категорию:
1 - криптограф        
2 - игры
3 - запись экрана 
4 - развитие 
5 - генераторы
''')
    
    return input('Ввод: ')


def main():

    print('''

                        ████──███─███─█───█─█─█─███─█──█
                        █──██──█──█───██─██─█─█──█──█──█
                        ████───█──███─█─█─█─█─█──█──████
                        █──██──█────█─█───█─█─█──█──█──█
                        ████──███─███─█───█─███──█──█──█

                                    0.0.1

        
                                    
Привет! Здесь ты можешь воспользоваться  полезными програмками 
или поиграть в простенькие игры. 
Если что то не понятно, то про выборе пункта просто введи 'q' 
и получишь пояснение к текущему меню.

Powered by DANIRU44
''')
     

    while True:
      
        match start_select():
            case '1':
                os.system('cls')
                ultracryptographer.main_crypto()
            case '2':
                os.system('cls')
                games.main_games()
            case '3':
                os.system('cls')
                screenrecording.warn_record()
            case '4':
                os.system('cls')
                development.main_dev()
            case '5':
                os.system('cls')
                generators.main_gen()
            case 'q':
                os.system('cls')
                print (questions.lobby)
                continue
            case _:
                os.system('cls')
                print('Некорректное значение \n ')  
                continue  



if __name__ == "__main__":
    main()