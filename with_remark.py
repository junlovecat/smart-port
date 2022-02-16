'''
플랫폼 4개, 배 4개, 스캐너 4개, cctv 13개 등을 표시한다.
상자들이 이동할 위치를 set으로 저장하고 각각의 상자에 틱을 부여한다.
틱이 추가될 때마다 상자는 그 틱번째 위치로 순간이동한다.
이 행동을 반복해 상자가 마치 이동하는 것처럼 보이게 한다.
'''

import pygame,random,numpy #모듈 임포트

def cmtopixel(cm:int): #cm 단위를 pixel로 변환
    return cm*37.7952755906

def cmtopixelset(cm:set): #cm 단위를 set 형태로 pixel로 변환
    return (cm[0]*37.7952755906,cm[1]*37.7952755906)

def chooseabox(): # 랜덤한 상자(빨강, 노랑, 초록, 파랑)의 정보를 반환
    return boxlist[random.randrange(0,4)]

pygame.init() #init

window=pygame.display.set_mode((cmtopixel(26),cmtopixel(19.05)))
#화면 크기 설정
pygame.display.set_caption('') #창 이름 설정(이름 없음)

rect1=pygame.image.load('rect1.png').convert() 
rect1=pygame.transform.scale(rect1,(cmtopixel(5.52),cmtopixel(1.6)))
# rect1 (1 플랫폼) 선언 및 이미지 로드, 크기 변경

rect2=pygame.image.load('rect2.png').convert()
rect2=pygame.transform.scale(rect2,(cmtopixel(5.52),cmtopixel(0.73)))
# rect2 (2, 3, 4 플랫폼) 선언 및 이미지 로드, 크기 변경

rect3=pygame.image.load('rect3.png').convert()
rect3=pygame.transform.scale(rect3,(cmtopixel(5.87),cmtopixel(0.78)))
# rect3 (배와 플랫폼 연결) 선언 및 이미지 로드, 크기 변경

smallrect1=pygame.image.load('smallrect1.png').convert()
smallrect1=pygame.transform.scale(smallrect1,(cmtopixel(0.8),cmtopixel(0.75)))
# smallrect1 (컨베이어 벨트) 선언 및 이미지 로드, 크기 변경

truck1=pygame.image.load('truck1.png').convert_alpha()
# truck1 (트럭) 선언 및 이미지 로드

backrect1=pygame.image.load('backrect1.png').convert()
# backrect1 (항구 배경 이미지) 선언 및 이미지 로드

backrect2=pygame.image.load('backrect2.png').convert()
# backrect2 (바다 배경 이미지) 선언 및 이미지 로드

trans1=pygame.image.load('trans1.png').convert_alpha()
trans1=pygame.transform.scale(trans1,(cmtopixel(2.2),cmtopixel(2.02)))
# trans1 (스캐너) 선언 및 이미지 로드, 배경색 투명화, 크기 변경

trucktracker=pygame.image.load('trucktracker.png').convert_alpha()
trucktracker=pygame.transform.scale(trucktracker,(cmtopixel(18.48),cmtopixel(2.68)))
# trucktracker (트럭 있는 곳) 선언 및 이미지 로드, 배경색 투명화, 크기 변경

controltower=pygame.image.load('controltower.png').convert_alpha()
# controltower (관제실) 선언 및 이미지 로드, 배경색 투명화

cctv=pygame.image.load('cctv.png').convert_alpha()
cctv=pygame.transform.scale(cctv,(cmtopixel(0.53),cmtopixel(0.51)))
# cctv (cctv) 선언 및 이미지 로드, 배경색 투명화, 크기 변경

redbox=pygame.image.load('redbox.png').convert()
mandbox=pygame.image.load('mandbox.png').convert()
yellowbox=pygame.image.load('yellowbox.png').convert()
greenbox=pygame.image.load('greenbox.png').convert()
# redbox, mandbox, yellowbox, greenbox (상자들) 선언 및 이미지 로드

boxlist=[redbox,mandbox,yellowbox,greenbox]
# boxlist 선언 및 내용 상자들로 채우기(상자 랜덤 반환에 사용)

moverrect1=pygame.image.load('moverrect1.png').convert()
moverrect1=pygame.transform.scale(moverrect1,(cmtopixel(0.8),cmtopixel(0.75)))
# moverrect1 (고속 자동 정렬 분배기) 선언 및 이미지 로드, 크기 변경

ship=pygame.image.load('ship.png').convert_alpha()
ship=pygame.transform.scale(ship,(cmtopixelset((7.77,1.77))))
# ship (배) 선언 및 이미지 로드, 배경색 투명화, 크기 변경

# 상자가 배 1에서 플랫폼 1로 이동하는데 사용됨
boxonetick=0 # 움직인 수를 저장
boxonemover=list(reversed([(xx,cmtopixel(2.3)) for xx in numpy.arange(215.43307087,780,0.1)]))
# 움직이는 위치를 저장
boxone=chooseabox() # 사용되는 상자 초기값 세팅

# 상자가 플랫폼 2에서 배 2로 이동하는데 사용됨
boxtwotwotick=0
boxtwotwomover=[(-100,-100) for xx in range(1000)]+[(xx,cmtopixel(5.6)) for xx in numpy.arange(215.43307087,780,0.1)]
boxtwotwo=chooseabox()

# 상자가 플랫폼 2에서 플랫폼 3으로, 플랫폼 3에서 배 3으로 이동하는데 사용됨
boxtwothreetick=0
boxtwothreemover=[(xx,cmtopixel(5.6)) for xx in numpy.arange(215,525,0.1)]+[(525,xx) for xx in numpy.arange(cmtopixel(5.6),cmtopixel(8),0.1)]+[(xx,cmtopixel(8)) for xx in numpy.arange(525,580,0.1)]+[(580,xx) for xx in numpy.arange(cmtopixel(8),cmtopixel(10.1),0.1)]+[(xx,cmtopixel(10.1)) for xx in numpy.arange(580,780,0.1)]
boxtwothree=chooseabox()

# 상자가 플랫폼 3에서 플랫폼 2로, 플랫폼 2에서 배 2로 이동하는데 사용됨
boxthreetwotick=0
boxthreetwomover=[(-100,-100) for xx in range(1050)]+[(xx,cmtopixel(8)) for xx in numpy.arange(215,525,0.1)]+[(525,xx) for xx in list(reversed(numpy.arange(cmtopixel(5.6),cmtopixel(8),0.1)))]+[(xx,cmtopixel(5.6)) for xx in numpy.arange(525,580,0.1)]+[(xx,cmtopixel(5.6)) for xx in numpy.arange(580,780,0.1)]
boxthreetwo=chooseabox()

# 상자가 플랫폼 3에서 배 3으로 이동하는데 사용됨
boxthreetick=0
boxthreemover=[(-100,-100) for xx in range(100)]+[(xx,cmtopixel(8)) for xx in numpy.arange(215.43307087,580,0.1)]+[(580,xx) for xx in numpy.arange(cmtopixel(8),cmtopixel(10.1),0.1)]+[(xx,cmtopixel(10.1)) for xx in numpy.arange(580,780,0.1)]
boxthree=chooseabox()

#상자가 배 4에서 플랫폼 4로 이동하는데 사용됨
boxfourtick=0
boxfourmover=list(reversed([(-100,-100) for xx in range(500)]+[(xx,cmtopixel(11.2)) for xx in numpy.arange(215.43307087,580,0.1)]+[(580,xx) for xx in numpy.arange(cmtopixel(11.2),cmtopixel(13.5),0.1)]+[(xx,cmtopixel(13.5)) for xx in numpy.arange(580,780,0.1)]))
boxfour=chooseabox()

#상자가 플랫폼 4에서 트럭 위치로 이동하는데 사용됨
boxfourtrucktick=0
boxfourtruckmover=[(-100,-100) for xx in range(250)]+[(xx,cmtopixel(11.2)) for xx in numpy.arange(215.43307087,328,0.1)]+[(328,xx) for xx in numpy.arange(cmtopixel(11.2),cmtopixel(18),0.1)]
boxfourtruck=chooseabox()

# 배의 위치를 플랫폼 1, 2, 3, 4로 옮기는데 사용됨
shipposition=[cmtopixelset((21.1,1.76)),cmtopixelset((21.1,4.92)),cmtopixelset((21.1,9.53)),cmtopixelset((21.1,12.53))]
while(1):
    for event in pygame.event.get(): # 이벤트 발생 대비
        if event.type==pygame.QUIT: # 종료 이벤트 발생시
            pygame.quit() # 종료
    window.fill([255,255,255]) # 배경 설정, #ffffff로 설정
    
    # background
    window.blit(backrect1,(0,0)) # 배경 설정 1
    window.blit(backrect2,(797.48031496,0)) # 배경 설정 2

    # input1
    window.blit(rect1,(0,54.803149606)) # 플랫폼 1

    # input 2~4
    a=[cmtopixel(5.34),cmtopixel(7.68),cmtopixel(10.88)]
    # 플랫폼 2, 3, 4 y좌표 설정
    for x in a: 
        window.blit(rect2,(0,x)) #정해진 위치에 플랫폼 2, 3, 4 표시
    
    n=28 # 트랙의 x좌표 사이의 거리
    # track1
    for x in range(13):
        window.blit(smallrect1,(cmtopixel(5.5)+x*n,cmtopixel(2.03)))
        # 플랫폼 1의 트랙 표시
    window.blit(rect3,(cmtopixel(15.2),cmtopixel(2)))
    # 플랫폼 1과 배 1 연결점 표시

    # track2
    for x in range(13):
        window.blit(smallrect1,(cmtopixel(5.5)+x*n,cmtopixel(5.3)))
        # 플랫폼 2의 트랙 표시
    window.blit(rect3,(cmtopixel(15.2),cmtopixel(5.3)))
    # 플랫폼 2와 배 2 연결점 표시

    # track2 mover
    for x in range(11,12):
        window.blit(moverrect1,(cmtopixel(5.5)+x*n,cmtopixel(5.3)))
        # 트랙 2에서 3으로 이동시키는 고속 자동정렬 분배기 표시
    
    # track2~3 joint
    window.blit(smallrect1,(cmtopixel(5.5)+11*n,cmtopixel(6.1)))
    window.blit(smallrect1,(cmtopixel(5.5)+11*n,cmtopixel(6.9)))
    # 트랙 2와 3 사이의 트랙 표시

    #track3
    for x in range(14):
        window.blit(smallrect1,(cmtopixel(5.5)+x*n,cmtopixel(7.73)))
        # 플랫폼 3의 트랙 표시
    window.blit(smallrect1,(cmtopixel(5.5)+13*n,317.85826772))
    window.blit(smallrect1,(cmtopixel(5.5)+13*n,343.55905512))
    # 플랫폼 3의 꺾이는 부분
    window.blit(rect3,(cmtopixel(15.13),369))
    # 플랫폼 3과 배 3 연결점 표시

    # track3mover
    for x in range(11,12):
        window.blit(moverrect1,(cmtopixel(5.5)+x*n,cmtopixel(7.73)))
        # 트랙 3에서 2로 이동시키는 고속 자동정렬 분배기 표시
    
    # track4
    for x in range(14):
        window.blit(smallrect1,(cmtopixel(5.5)+x*n,cmtopixel(10.93)))
        # 플랫폼 4의 트랙 표시
    window.blit(smallrect1,(cmtopixel(5.5)+13*n,cmtopixel(11.7)))
    window.blit(smallrect1,(cmtopixel(5.5)+13*n,cmtopixel(12.5)))
    # 플랫폼 4의 꺾이는 부분
    window.blit(rect3,(cmtopixel(15.15),cmtopixel(13.2)))
    # 플랫폼 4와 배 4 연결점 표시

    # cctv
    cctvlist=[(11.67,2.81),(15.19,2.81),(7.1,4.64),(10.25,4.71),(16.23,4.4),(10.43,6.63),(17.21,9.09),(14.4,9.9),(7.01,11.88),(9.73,12.53),(14.3,12.15),(7.7,14.73),(9.51,16.69)]
    # cctv 위치 저장 (cm 단위)
    for x in cctvlist:
        window.blit(cctv,cmtopixelset(x))
        # cctv 위치 변환 및 표시
    
    # trucktracker
    window.blit(trucktracker,(0,cmtopixel(16.38)))
    # 트럭 있는 공간 표시

    # truckconnector
    for x in range(10):
        window.blit(smallrect1,(cmtopixel(5.5)+4*n,441.82677165+27.22*x))
        # 트럭 연결 트랙 표시
    
    # trucks
    # 트럭 연결 트랙에 의해 앞-뒤로 구분됨
    for x in range(6):
        window.blit(truck1,(18.897637795+50*x,cmtopixel(17.42)))
        # 트럭 연결 트랙 앞 부분 표시
    for x in range(6):
        window.blit(truck1,(360+50*x,cmtopixel(17.42)))
        # 트럭 연결 트랙 뒷 부분 표시
    
    # control tower
    window.blit(controltower,(cmtopixel(0.7),cmtopixel(12.8)))
    # 관제실 표시

    # move block
    '''
    상자의 틱이 끝이 아닌 시 상자 1의 위치가 제대로 표시되지만,
    상자의 틱이 끝종에 다다르면 상자 틱이 초기화 되면서 
    틱이 끝나자마자 움직이지 않는 한, 상자는 (-100,-100)에 고정되어
    100,500,1000 시간동안 움직이지 않는다.
    '''
    # box one
    if boxonetick<len(boxonemover)-1: # 상자 1 틱이 끝이 아닐 때
        window.blit(boxone,boxonemover[boxonetick]) # 상자 1의 위치 이동 표시
        boxonetick+=1 #상자 1 틱 증가
    else: # 상자 1 틱이 끝종에 다다랐을 때
        boxonetick=0 # 상자 1 틱 초기화
        boxone=chooseabox() # 상자 1 색깔 랜덤 바꾸기
    
    # box two - two
    if boxtwotwotick<len(boxtwotwomover)-1: # 상자 2-2 틱이 끝이 아닐 때
        window.blit(boxtwotwo,boxtwotwomover[boxtwotwotick])
        # 상자 2-2의 위치 이동 표시
        boxtwotwotick+=1 # 상자 2-2 틱 증가
    else: # 상자 2-2 틱이 끝종에 다다랐을 때
        boxtwotwotick=0 # 상자 2-2 틱 초기화
        boxtwotwo=chooseabox() # 상자 2-2 색깔 랜덤 바꾸기
    
    # box two - three
    if boxtwothreetick<len(boxtwothreemover)-1: # 상자 2-3 틱이 끝이 아닐 때
        window.blit(boxtwothree,boxtwothreemover[boxtwothreetick])
        # 상자 2-3의 위치 이동 표시
        boxtwothreetick+=1 # 상자 2-3 틱 증가
    else: # 상자 2-3 틱이 끝종에 다다랐을 때
        boxtwothreetick=0 # 상자 2-3 틱 초기화
        boxtwothree=chooseabox() # 상자 2-3 색깔 랜덤 바꾸기
    
    # box three - two
    if boxthreetwotick<len(boxthreetwomover)-1: #상자 3-2 틱이 끝이 아닐 때
        window.blit(boxthreetwo,boxthreetwomover[boxthreetwotick])
        # 상자 3-2의 위치 이동 표시
        boxthreetwotick+=1 # 상자 3-2 틱 증가
    else: # 상자 3-2 틱이 끝종에 다다랐을 때
        boxthreetwotick=0 # 상자 3-2 틱 초기화
        boxthreetwo=chooseabox() # 상자 3-2 색깔 랜덤 바꾸기
    
    # box three
    if boxthreetick<len(boxthreemover)-1: # 상자 3-3 틱이 끝이 아닐 때
        window.blit(boxthree,boxthreemover[boxthreetick])
        # 상자 3-3의 위치 이동 표시
        boxthreetick+=1 # 상자 3-3 틱 증가
    else: # 상자 3-3 틱이 끝종에 다다랐을 때
        boxthreetick=0 # 상자 3-3 틱 초기화
        boxthree=chooseabox() # 상자 3-3 색깔 랜덤 바꾸기
    
    # box four
    if boxfourtick<len(boxfourmover)-1: # 상자 4-4 틱이 끝이 아닐 때
        window.blit(boxfour,boxfourmover[boxfourtick])
        # 상자 4-4의 위치 이동 표시
        boxfourtick+=1 # 상자 4-4 틱 증가
    else: # 상자 4-4 틱이 끝종에 다다랐을 때
        boxfourtick=0 # 상자 4-4 틱 초기화
        boxfour=chooseabox() # 상자 4-4 색깔 랜덤 바꾸기
    
    # box four - truck
    if boxfourtrucktick<len(boxfourtruckmover)-1: # 상자 4-t 틱이 끝이 아닐 때
        window.blit(boxfourtruck,boxfourtruckmover[boxfourtrucktick])
        # 상자 4-t의 위치 이동 표시
        boxfourtrucktick+=1 # 상자 4-t 틱 증가
    else: #상자 4-t 틱이 끝종에 다다랐을 때
        boxfourtrucktick=0 # 상자 4-t 틱 초기화
        boxfourtruck=chooseabox() # 상자 4-t 색깔 랜덤 바꾸기
    
    # transparent checker
    window.blit(trans1,(cmtopixel(9.2),cmtopixel(1.31)))
    window.blit(trans1,(cmtopixel(12.3),cmtopixel(1.31)))
    window.blit(trans1,(cmtopixelset((7.7,10.24))))
    # 스캐너 표시

    # ship
    for x in range(4):
        window.blit(ship,shipposition[x])
        # 배 표시
    pygame.display.flip() # 파이게임 화면 초기화 및 표시
