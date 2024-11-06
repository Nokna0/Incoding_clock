'''
!!! 중요 !!!
이 코드는 idle 환경에서 제대로 동작하지 않습니다.
꼭 터미널에서 실행해 주세요!

파일 우클릭 -> 연결 프로그램 -> python 클릭!
'''

import keyboard
import time

while True:
    menu = input('사용할 기능을 입력하세요(\'시계\', \'스톱워치\', \'타이머\', \'종료\')\n').strip()

    if menu == '시계' or menu == 'clock':
        realmenu = 'clock'
    elif menu == '스톱워치' or menu == 'stopwatch':
        realmenu = 'stopwatch'
    elif menu == '타이머' or menu == 'timer':
        realmenu = 'timer'
    elif menu == '종료' or menu == 'quit':
        realmenu = 'quit'
    else:
        print('유효하지 않은 메뉴')
        print('==========종료==========')
        continue

    if realmenu == 'clock':
        print('==========시계==========')
        print('\'space\'키를 눌러 정지')
        while True:
            if keyboard.is_pressed("space"):
                print('\n==========종료==========')
                break
            else:
                clock = list(time.localtime())

                clock_edit = f'{clock[0]}년 {clock[1]}월 {clock[2]}일 {clock[3]}시 {clock[4]}분 {clock[5]}초'
                print(f'\r{clock_edit}', end='')

    elif realmenu == 'stopwatch':
        print('==========스톱워치==========')
        print('\'space\'키를 눌러 정지')

        stopwatch_h = 0
        stopwatch_m = 0
        stopwatch_s = 0

        while True:
            if keyboard.is_pressed("space"):
                print('\n==========종료==========')
                break
            else:
                time.sleep(0.01)
                stopwatch_s += 0.01

                if stopwatch_s >= 60:
                    stopwatch_s -= 60
                    stopwatch_m += 1

                if stopwatch_m >= 60:
                    stopwatch_m -= 60
                    stopwatch_h += 1

                stopwatch_s = round(stopwatch_s, 2)

                if stopwatch_h != 0:
                    print(f'\r{stopwatch_h}시 {stopwatch_m}분 {stopwatch_s}초', end='')
                elif stopwatch_m != 0:
                    print(f'\r{stopwatch_m}분 {stopwatch_s}초', end='')
                else:
                    print(f'\r{stopwatch_s}초', end='')

    elif realmenu == 'timer':
        print('==========타이머==========')
        print('카운트다운할 시간 입력')
        timer = {'hour': 0, 'minute': 0, 'second': 0}

        timer['hour'] = input('시간 : ').strip()
        timer['minute'] = input('분 : ').strip()
        timer['second'] = input('초 : ').strip()

        try:
            timer['hour'] = float(timer['hour'])
            timer['minute'] = float(timer['minute'])
            timer['second'] = float(timer['second'])
        except ValueError:
            print('유효하지 않은 값')
            print('==========종료==========')
            continue
        
        print('\'space\'키를 눌러 정지')

        while not keyboard.is_pressed("space"):
            time.sleep(0.01)

            if timer['second'] <= 0:
                if timer['minute'] > 0:
                    timer['minute'] -= 1
                    timer['second'] += 60
                elif timer['hour'] > 0:
                    timer['hour'] -= 1
                    timer['minute'] += 59
                    timer['second'] += 60
                else:
                    break

            timer['second'] -= 0.01

            timer_result = f"{round(timer['hour'])}시 {round(timer['minute'])}분 {round(timer['second'], 2)}초"
            print(f'\r{timer_result}', end='')

        print('\n==========종료==========')

    elif realmenu == 'quit':
        break

    else:
        print('유효하지 않은 메뉴')
        print('==========종료==========')
        continue
