'''
!!! 중요 !!!
이 코드는 idle 환경에서 제대로 동작하지 않습니다.
꼭 터미널에서 실행해 주세요!

파일 우클릭 -> 연결 프로그램 -> python 클릭!
'''

# 필요한 모듈 수입
import keyboard  # 키보드 입력을 감지하는 모듈
import time  # 시간을 다루기 위한 모듈

# 무한 루프 시작
while True:
    # 사용자에게 사용할 기능을 입력받음
    menu = input('사용할 기능을 입력하세요(\'시계\', \'스톱워치\', \'타이머\', \'종료\')\n').strip()

    # 입력한 값을 읽기 쉽게 변환
    if menu == '시계' or menu == 'clock':
        realmenu = 'clock'  # 사용자가 '시계' 또는 'clock'을 입력하면 realmenu에 'clock' 저장
    elif menu == '스톱워치' or menu == 'stopwatch':
        realmenu = 'stopwatch'  # 사용자가 '스톱워치' 또는 'stopwatch'을 입력하면 realmenu에 'stopwatch' 저장
    elif menu == '타이머' or menu == 'timer':
        realmenu = 'timer'  # 사용자가 '타이머' 또는 'timer'를 입력하면 realmenu에 'timer' 저장
    elif menu == '종료' or menu == 'quit':
        realmenu = 'quit'  # 사용자가 '종료' 또는 'quit'을 입력하면 realmenu에 'quit' 저장
    else:
        print('유효하지 않은 메뉴')  # 잘못된 입력일 경우 에러 메시지 출력
        print('-----------종료-----------')
        continue  # 루프 처음으로 돌아가 다시 입력받음

    # 시계 기능
    if realmenu == 'clock':
        print('----------시계----------')
        print('\'space\'키를 눌러 정지')  # 정지할 때 스페이스 키 안내 메시지
        while True:
            if keyboard.is_pressed("space"):
                print('\n-----------종료-----------')  # 정지할 때 종료 안내 메시지
                break  # 스페이스 키가 눌리면 루프를 빠져나감
            else:
                clock = list(time.localtime())  # 현재 시간을 리스트 형식으로 가져옴

                # 현재 시간을 보기 좋게 편집
                clock_edit = f'{clock[0]}년 {clock[1]}월 {clock[2]}일 {clock[3]}시 {clock[4]}분 {clock[5]}초'
                print(f'\r{clock_edit}', end='')  # 편집된 시간을 같은 줄에 출력

    # 스톱워치 기능
    elif realmenu == 'stopwatch':
        print('----------스톱워치----------')
        print('\'space\'키를 눌러 정지')  # 정지할 때 스페이스 키 안내 메시지

        stopwatch_h = 0  # 시간 초기화
        stopwatch_m = 0  # 분 초기화
        stopwatch_s = 0  # 초 초기화

        while True:
            if keyboard.is_pressed("space"):
                print('\n-----------종료-----------')  # 정지할 때 종료 안내 메시지
                break  # 스페이스 키가 눌리면 루프를 빠져나감
            else:
                time.sleep(0.01)  # 0.01초 대기
                stopwatch_s += 0.01  # 초를 0.01씩 증가시킴

                # 초가 60 이상이면 분으로 전환
                if stopwatch_s >= 60:
                    stopwatch_s -= 60
                    stopwatch_m += 1

                # 분이 60 이상이면 시간으로 전환
                if stopwatch_m >= 60:
                    stopwatch_m -= 60
                    stopwatch_h += 1

                stopwatch_s = round(stopwatch_s, 2)  # 소수점 두 자리로 반올림

                # 시간, 분, 초를 각각 조건에 맞게 출력
                if stopwatch_h != 0:
                    print(f'\r{stopwatch_h}시 {stopwatch_m}분 {stopwatch_s}초', end='')
                elif stopwatch_m != 0:
                    print(f'\r{stopwatch_m}분 {stopwatch_s}초', end='')
                else:
                    print(f'\r{stopwatch_s}초', end='')

    # 타이머 기능
    elif realmenu == 'timer':
        print('----------타이머----------')
        print('카운트다운할 시간 입력')
        timer = {'hour': 0, 'minute': 0, 'second': 0}  # 타이머 딕셔너리 생성

        timer['hour'] = input('시간 : ').strip()
        timer['minute'] = input('분 : ').strip()
        timer['second'] = input('초 : ').strip()

        try:
            timer['hour'] = float(timer['hour'])  # 시간 변환
            timer['minute'] = float(timer['minute'])  # 분 변환
            timer['second'] = float(timer['second'])  # 초 변환 
        except ValueError:
            print('유효하지 않은 값')  # 변환 오류 발생 시 에러 메시지 출력
            print('-----------종료-----------')
            continue  # 루프 처음으로 돌아가 다시 입력받음
        
        print('\'space\'키를 눌러 정지')  # 정지할 때 스페이스 키 안내 메시지

        while not keyboard.is_pressed("space"):
            time.sleep(0.01)  # 0.01초 대기

            if timer['second'] <= 0:
                if timer['minute'] > 0:
                    timer['minute'] -= 1  # 분 감소
                    timer['second'] += 60  # 초 증가
                elif timer['hour'] > 0:
                    timer['hour'] -= 1  # 시간 감소
                    timer['minute'] += 59  # 분 증가
                    timer['second'] += 60  # 초 증가
                else:
                    break  # 타이머 종료

            timer['second'] -= 0.01  # 초 감소

            # 현재 타이머 상태를 보기 좋게 편집
            timer_result = f"{round(timer['hour'])}시 {round(timer['minute'])}분 {round(timer['second'], 2)}초"
            print(f'\r{timer_result}', end='')

        print('\n-----------종료-----------')  # 타이머 종료 메시지 출력

    # 종료 명령
    elif realmenu == 'quit':
        break  # 루프 종료

    else:
        print('유효하지 않은 메뉴')  # 잘못된 입력일 경우 에러 메시지 출력
        print('-----------종료-----------')
        continue  # 루프 처음으로 돌아가 다시 입력받음
