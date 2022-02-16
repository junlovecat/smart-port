import pygame,random,numpy
def cmtopixel(cm:int):
    return cm*37.7952755906
def cmtopixelset(cm:set):
    return (cm[0]*37.7952755906,cm[1]*37.7952755906)
def chooseabox():
    return boxlist[random.randrange(0,4)]
pygame.init()
window=pygame.display.set_mode((cmtopixel(21.1+4.9),cmtopixel(19.05)))
pygame.display.set_caption('')
rect1=pygame.image.load('rect1.png').convert()
rect1=pygame.transform.scale(rect1,(cmtopixel(5.52),cmtopixel(1.6)))
rect2=pygame.image.load('rect2.png').convert()
rect2=pygame.transform.scale(rect2,(cmtopixel(5.52),cmtopixel(0.73)))
rect3=pygame.image.load('rect3.png').convert()
rect3=pygame.transform.scale(rect3,(cmtopixel(5.87),cmtopixel(0.78)))
smallrect1=pygame.image.load('smallrect1.png').convert()
smallrect1=pygame.transform.scale(smallrect1,(cmtopixel(0.8),cmtopixel(0.75)))
truck1=pygame.image.load('truck1.png').convert_alpha()
backrect1=pygame.image.load('backrect1.png').convert()
backrect2=pygame.image.load('backrect2.png').convert()
trans1=pygame.image.load('trans1.png').convert_alpha()
trans1=pygame.transform.scale(trans1,(cmtopixel(2.2),cmtopixel(2.02)))
trucktracker=pygame.image.load('trucktracker.png').convert_alpha()
trucktracker=pygame.transform.scale(trucktracker,(cmtopixel(18.48),cmtopixel(2.68)))
controltower=pygame.image.load('controltower.png').convert_alpha()
cctv=pygame.image.load('cctv.png').convert_alpha()
cctv=pygame.transform.scale(cctv,(cmtopixel(0.53),cmtopixel(0.51)))
redbox=pygame.image.load('redbox.png').convert()
mandbox=pygame.image.load('mandbox.png').convert()
yellowbox=pygame.image.load('yellowbox.png').convert()
greenbox=pygame.image.load('greenbox.png').convert()
boxlist=[redbox,mandbox,yellowbox,greenbox]
moverrect1=pygame.image.load('moverrect1.png').convert()
moverrect1=pygame.transform.scale(moverrect1,(cmtopixel(0.8),cmtopixel(0.75)))
ship=pygame.image.load('ship.png').convert_alpha()
ship=pygame.transform.scale(ship,(cmtopixelset((7.77,1.77))))
boxonetick=0
boxonemover=list(reversed([(xx,cmtopixel(2.3)) for xx in numpy.arange(215.43307087,780,0.1)]))
boxone=chooseabox()
boxtwotwotick=0
boxtwotwomover=[(-100,-100) for xx in range(1000)]+[(xx,cmtopixel(5.6)) for xx in numpy.arange(215.43307087,780,0.1)]
boxtwotwo=chooseabox()
boxtwothreetick=0
boxtwothreemover=[(xx,cmtopixel(5.6)) for xx in numpy.arange(215,525,0.1)]+[(525,xx) for xx in numpy.arange(cmtopixel(5.6),cmtopixel(8),0.1)]+[(xx,cmtopixel(8)) for xx in numpy.arange(525,580,0.1)]+[(580,xx) for xx in numpy.arange(cmtopixel(8),cmtopixel(10.1),0.1)]+[(xx,cmtopixel(10.1)) for xx in numpy.arange(580,780,0.1)]
boxtwothree=chooseabox()
boxthreetwotick=0
boxthreetwomover=[(-100,-100) for xx in range(1050)]+[(xx,cmtopixel(8)) for xx in numpy.arange(215,525,0.1)]+[(525,xx) for xx in list(reversed(numpy.arange(cmtopixel(5.6),cmtopixel(8),0.1)))]+[(xx,cmtopixel(5.6)) for xx in numpy.arange(525,580,0.1)]+[(xx,cmtopixel(5.6)) for xx in numpy.arange(580,780,0.1)]
boxthreetwo=chooseabox()
boxthreetick=0
boxthreemover=[(-100,-100) for xx in range(100)]+[(xx,cmtopixel(8)) for xx in numpy.arange(215.43307087,580,0.1)]+[(580,xx) for xx in numpy.arange(cmtopixel(8),cmtopixel(10.1),0.1)]+[(xx,cmtopixel(10.1)) for xx in numpy.arange(580,780,0.1)]
boxthree=chooseabox()
boxfourtick=0
boxfourmover=list(reversed([(-100,-100) for xx in range(500)]+[(xx,cmtopixel(11.2)) for xx in numpy.arange(215.43307087,580,0.1)]+[(580,xx) for xx in numpy.arange(cmtopixel(11.2),cmtopixel(13.5),0.1)]+[(xx,cmtopixel(13.5)) for xx in numpy.arange(580,780,0.1)]))
boxfour=chooseabox()
boxfourtrucktick=0
boxfourtruckmover=[(-100,-100) for xx in range(250)]+[(xx,cmtopixel(11.2)) for xx in numpy.arange(215.43307087,328,0.1)]+[(328,xx) for xx in numpy.arange(cmtopixel(11.2),cmtopixel(18),0.1)]
boxfourtruck=chooseabox()
shipposition=[cmtopixelset((21.1,1.76)),cmtopixelset((21.1,4.92)),cmtopixelset((21.1,9.53)),cmtopixelset((21.1,12.53))]
while(1):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    window.fill([255,255,255])
    #background
    window.blit(backrect1,(0,0))
    window.blit(backrect2,(797.48031496,0))
    #input1
    window.blit(rect1,(0,54.803149606))
    #input 2~4
    a=[cmtopixel(5.34),cmtopixel(7.68),cmtopixel(10.88)]
    for x in a:
        window.blit(rect2,(0,x))
    n=28
    #track1
    for x in range(13):
        window.blit(smallrect1,(cmtopixel(5.5)+x*n,cmtopixel(2.03)))
    window.blit(rect3,(cmtopixel(15.2),cmtopixel(2)))
    #track2
    for x in range(13):
        window.blit(smallrect1,(cmtopixel(5.5)+x*n,cmtopixel(5.3)))
    window.blit(rect3,(cmtopixel(15.2),cmtopixel(5.3)))
    #track2 mover
    for x in range(11,12):
        window.blit(moverrect1,(cmtopixel(5.5)+x*n,cmtopixel(5.3)))
    #track2~3 joint
    window.blit(smallrect1,(cmtopixel(5.5)+11*n,cmtopixel(6.1)))
    window.blit(smallrect1,(cmtopixel(5.5)+11*n,cmtopixel(6.9)))
    #track3
    for x in range(14):
        window.blit(smallrect1,(cmtopixel(5.5)+x*n,cmtopixel(7.73)))
    window.blit(smallrect1,(cmtopixel(5.5)+13*n,317.85826772))
    window.blit(smallrect1,(cmtopixel(5.5)+13*n,343.55905512))
    window.blit(rect3,(cmtopixel(15.13),369))
    #track3mover
    for x in range(11,12):
        window.blit(moverrect1,(cmtopixel(5.5)+x*n,cmtopixel(7.73)))
    #track4
    for x in range(14):
        window.blit(smallrect1,(cmtopixel(5.5)+x*n,cmtopixel(10.93)))
    window.blit(smallrect1,(cmtopixel(5.5)+13*n,cmtopixel(11.7)))
    window.blit(smallrect1,(cmtopixel(5.5)+13*n,cmtopixel(12.5)))
    window.blit(rect3,(cmtopixel(15.15),cmtopixel(13.2)))
    #cctv
    cctvlist=[(11.67,2.81),(15.19,2.81),(7.1,4.64),(10.25,4.71),(16.23,4.4),(10.43,6.63),(17.21,9.09),(14.4,9.9),(7.01,11.88),(9.73,12.53),(14.3,12.15),(7.7,14.73),(9.51,16.69)]
    for x in cctvlist:
        window.blit(cctv,cmtopixelset(x))
    #truck
    window.blit(trucktracker,(0,cmtopixel(16.38)))
    #tracktruck
    for x in range(10):
        window.blit(smallrect1,(cmtopixel(5.5)+4*n,441.82677165+27.22*x))
    #trucks
    for x in range(6):
        window.blit(truck1,(18.897637795+50*x,cmtopixel(17.42)))
    for x in range(6):
        window.blit(truck1,(360+50*x,cmtopixel(17.42)))
    #control tower
    window.blit(controltower,(cmtopixel(0.7),cmtopixel(12.8)))
    #move block
    #box one
    if boxonetick<len(boxonemover)-1:
        window.blit(boxone,boxonemover[boxonetick])
        boxonetick+=1
    else:
        boxonetick=0
        boxone=chooseabox()
    #box two - two
    if boxtwotwotick<len(boxtwotwomover)-1:
        window.blit(boxtwotwo,boxtwotwomover[boxtwotwotick])
        boxtwotwotick+=1
    else:
        boxtwotwotick=0
        boxtwotwo=chooseabox()
    #box two - three
    if boxtwothreetick<len(boxtwothreemover)-1:
        window.blit(boxtwothree,boxtwothreemover[boxtwothreetick])
        boxtwothreetick+=1
    else:
        boxtwothreetick=0
        boxtwothree=chooseabox()
    #box three - two
    if boxthreetwotick<len(boxthreetwomover)-1:
        window.blit(boxthreetwo,boxthreetwomover[boxthreetwotick])
        boxthreetwotick+=1
    else:
        boxthreetwotick=0
        boxthreetwo=chooseabox()
    #box three
    if boxthreetick<len(boxthreemover)-1:
        window.blit(boxthree,boxthreemover[boxthreetick])
        boxthreetick+=1
    else:
        boxthreetick=0
        boxthree=chooseabox()
    #box four
    if boxfourtick<len(boxfourmover)-1:
        window.blit(boxfour,boxfourmover[boxfourtick])
        boxfourtick+=1
    else:
        boxfourtick=0
        boxfour=chooseabox()
    #box four - truck
    if boxfourtrucktick<len(boxfourtruckmover)-1:
        window.blit(boxfourtruck,boxfourtruckmover[boxfourtrucktick])
        boxfourtrucktick+=1
    else:
        boxfourtrucktick=0
        boxfourtruck=chooseabox()
    #transparent checker
    window.blit(trans1,(cmtopixel(9.2),cmtopixel(1.31)))
    window.blit(trans1,(cmtopixel(12.3),cmtopixel(1.31)))
    window.blit(trans1,(cmtopixelset((7.7,10.24))))
    for x in range(4):
        window.blit(ship,shipposition[x])
    pygame.display.flip()