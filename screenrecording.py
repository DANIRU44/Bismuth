import os
import numpy as np
import cv2
import pyautogui
from datetime import datetime


def main_recording():
    screen_size = pyautogui.size()

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    out = cv2.VideoWriter(f'{now}.avi', fourcc, 8.0, screen_size) 

    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        out.write(frame)
        cv2.imshow('screen recording', frame)

        if cv2.waitKey(1) == ord('q'):
            break

        
    cv2.destroyAllWindows()
    out.release()

def warn_record():
    print('''
    В этой версии запись экрана немного лагает, и нет возможности записывать звук,
    если всё устраивает, то нажми enter, если нет, то введи любую букву
    (для остановки записи, в окне записи нажми на q)
    ''')
    while True:
        i = input('Ввод: ')
        if i == '':
            main_recording()
        else: 
            os.system('cls')
            break
