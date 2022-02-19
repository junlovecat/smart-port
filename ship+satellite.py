'''
인공위성과 무인 화물선이 통신해 자동으로 장애물을 피하는 시뮬레이션.
화물선이 빙산을 만나는데, 이 때 인공위성이 신호를 보내 화물선이 이를 피하게 된다.
총 3개의 배 이미지가 사용되는데, 각각의 방향을 가지고 있어 특정 방향이 필요할 때 (-100,-100)에서 이동한다.
시작 위치와 끝 위치를 서로 동일시 하여, 자연스럽게 움직이도록 한다.
'''

import pygame,numpy # 모듈 임포트

def cmtopixel(cm:int): #cm 단위를 pixel로 변환
    return cm*37.7952755906

def cmtopixelset(cm:set): #cm 단위를 set 형태로 pixel로 변환
    return (cm[0]*37.7952755906,cm[1]*37.7952755906)

pygame.init() # pygame 생성
window=pygame.display.set_mode((cmtopixel(26),cmtopixel(19.05))) # pygame 화면 크기 설정
pygame.display.set_caption('') # pygame 창 제목 설정: 이름 x

satellite=pygame.image.load('satellite.png')
satellite=pygame.transform.scale(satellite,(satellite.get_size()[0]/8,satellite.get_size()[1]/8))
# satellite(인공위성) 선언 및 크기 1/8로 조정

ship=pygame.image.load('shipupper.png').convert()
ship=pygame.transform.scale(ship,(ship.get_size()[0]/4,ship.get_size()[1]/4))
# ship(배) 선언 및 크기 1/4로 조정

rotatedship=pygame.image.load('rotatedship.png').convert_alpha()
rotatedship=pygame.transform.scale(rotatedship,(rotatedship.get_size()[0]/4,rotatedship.get_size()[1]/4))
# rotatedship(오른쪽 위(45°)를 향하는 배) 선언 및 크기 1/4로 조정

rotatedship2=pygame.image.load('rotatedship2.png').convert_alpha()
rotatedship2=pygame.transform.scale(rotatedship2,(rotatedship2.get_size()[0]/4,rotatedship2.get_size()[1]/4))
# rotatedship2(오른쪽 아래(135°)를 향하는 배) 선언 및 크기 1/4로 조정

iceberg=pygame.image.load('iceberg.png').convert_alpha()
iceberg=pygame.transform.scale(iceberg,(iceberg.get_size()[0]/2,iceberg.get_size()[1]/2))
iceberg=pygame.transform.smoothscale(iceberg,iceberg.get_size())
# iceberg(빙산) 선언 및 크기 1/2로 조정, 안티에일레이싱

shiptick=0 #배 이동 틱, 세개의 리스트가 이를 공유할 예정
shipmover=[(xx,440) for xx in numpy.arange(-100,250,0.1)]+[(-100,-100) for _ in numpy.arange(0,140,0.1)]+[(xx,300) for xx in numpy.arange(390,550,0.1)]+[(-100,-100) for _ in numpy.arange(0,110,0.1)]+[(xx,440) for xx in numpy.arange(660,1000,0.1)]
# 0°를 향하는 배가 움직일 곳, (-100,-100)일 때에는 다른 방향의 배가 움직임.

shiprotatedmover=[(-100,-100) for _ in numpy.arange(-100,250,0.1)]+[(250+xx,440-xx) for xx in numpy.arange(0,140,0.1)]+[(-100,-100) for _ in numpy.arange(390,550,0.1)]+[(-100,-100) for xx in numpy.arange(0,110,0.1)]+[(-100,-100) for xx in numpy.arange(660,1000,0.1)]
# 45°를 향하는 배가 움직일 곳, 이하 동일

ship2rotatedmover=[(-100,-100) for _ in numpy.arange(-100,250,0.1)]+[(-100,-100) for xx in numpy.arange(0,140,0.1)]+[(-100,-100) for _ in numpy.arange(390,550,0.1)]+[(550+xx,330+xx) for xx in numpy.arange(0,110,0.1)]+[(-100,-100) for xx in numpy.arange(660,1000,0.1)]
# 135°를 향하는 배가 움직일 곳, 이하 동일

while(1):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    # 이벤트를 불러들여 종료 이벤트 발생시 종료
    window.fill([135,206,235]) # 배경색(파랑) 설정
    window.blit(satellite,(0,0)) # satellite 위치 조정
    window.blit(iceberg,(400,360)) # iceberg 위치 조정
    if shiptick<len(shipmover)-1: # 틱이 리스트를 안 벗어날 때
        window.blit(ship,shipmover[shiptick])
        window.blit(rotatedship,shiprotatedmover[shiptick])
        window.blit(rotatedship2,ship2rotatedmover[shiptick])
        '''
        세 개를 동시에 다 움직이는데,
        이러한 이유는 if문을 사용해 구별 시 더 어려운 구문을 사용해야 하기 때문
        '''
        shiptick+=1 # 틱 1 추가
    else:
        shiptick=0 # 틱 초기화
    pygame.display.flip() # 화면 초기화
