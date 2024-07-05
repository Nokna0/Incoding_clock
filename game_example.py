# 'pygame' 라이브러리의 함수들을 가져옵니다.
import pygame

# 게임 엔진을 초기화합니다.
pygame.init()

# 사용할 RGB 형식으로 색상을 정의합니다.
BLACK = (  0,   0,   0)   # 검정색
WHITE = (255, 255, 255)  # 흰색
BLUE  = (  0,   0, 255)  # 파란색
GREEN = (  0, 255,   0)  # 초록색
RED   = (255,   0,   0)  # 빨간색
 
# 화면의 너비와 높이를 설정합니다.
size   = [512, 512]
SCREEN = pygame.display.set_mode(size)
  
# 창의 제목을 설정합니다.
pygame.display.set_caption("BOOOOOOM")
  
# 사용자가 창을 닫을 때까지 반복합니다.
done = False
clock = pygame.time.Clock()

while not done:
  
    # 이 코드는 초당 최대 10번 반복됩니다.
    # 이 부분을 빼면 가능한 CPU를 모두 사용합니다.
    clock.tick(10)

    # 메인 이벤트 루프
    for event in pygame.event.get(): # 사용자 입력 확인
        if event.type == pygame.QUIT: # 사용자가 창을 닫으면
            done=True # done 변수를 True로 설정하여 루프를 종료합니다.
  
    # 모든 그리기 코드는 for 루프 이후, 그리고
    # 메인 루프인 while done==False 내부에서 실행됩니다.
      
    # 화면을 지우고 배경을 설정합니다.
    SCREEN.fill(BLACK)
    
    # 게임 화면 그리기
    pygame.draw.rect(SCREEN, WHITE, [64, 64, 384, 384], 5)
    pygame.draw.line(SCREEN, WHITE, [64, 128], [448-5, 128], 5)
    pygame.draw.line(SCREEN, WHITE, [96, 128], [96, 448-5], 5)
    pygame.draw.line(SCREEN, WHITE, [416, 128], [416, 448-5], 5)

    for i in range(15):
        grid_y = 128 - (i * 0) # 128~448 좌표 사이의 격자 생성
        pygame.draw.line(SCREEN, WHITE, [64, 128], [448-5, 128], 5)


    # 화면에 그린 내용을 업데이트합니다.
    # 다른 그리기 명령들이 모두 실행된 후에 이 부분이 실행되어야 합니다.
    pygame.display.flip()
