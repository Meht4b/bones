from classes import *

pygame.init()

window = pygame.display.set_mode((1000,1000))

a = bone(100,60,head=vector(100,100))
b = bone(100,0,parent=0)
c = bone(100,0,parent=1)

ch = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:

                ch +=1
                if ch == len(bone.bones):
                    ch =0
            if event.key == pygame.K_DOWN:

                
                ch -=1
                if ch <0:
                    ch = len(bone.bones)-1
                print(ch)

        if event.type == pygame.MOUSEWHEEL:
            bone.bones[ch].rotate(10*event.y)

            
    window.fill((0,0,0))
    #print(bone.bones[0].angle,bone.bones[1].rotation,bone.bones[1].rotation)
    bone.classupdate(window)
    

    pygame.display.update()