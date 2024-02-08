from classes import *

pygame.init()

window = pygame.display.set_mode((1000,1000))

a = bone(500,60,head=vector(100,100))
b = bone(500,0,parent=0)



ch = 0

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        

        x,y = pygame.mouse.get_pos()
        mousepos = vector(x,y)
        mousevector =  a.head-mousepos 
        if x ==0 and y ==0:
            mousevector = vector(1,1)
            x,y=1,1
        theta = 0
        if mousevector.x!=0:
            
            theta = math.atan(mousevector.y/mousevector.x)

            theta = math.atan(mousevector.y/mousevector.x)

        print((math.pow(mousevector.magnitude(),2) + math.pow(a.length,2) - math.pow(b.length^2,2))/(2*mousevector.magnitude()*a.length))
        
        
        if mousevector.magnitude()<a.length+b.length:
            
            alpha = math.acos((math.pow(mousevector.magnitude(),2) + math.pow(a.length,2) - math.pow(b.length,2))/(2*mousevector.magnitude()*a.length))
            beta = math.acos((math.pow(mousevector.magnitude(),2) + math.pow(b.length,2) - math.pow(a.length,2))/(2*mousevector.magnitude()*b.length))
            
            if mousepos.x>a.head.x :

                a.rotateAbs(theta+alpha)
                b.rotateAbs(-(beta+alpha))

            else:
                a.rotateAbs(3.14159-2*(theta+alpha))
                b.rotateAbs((beta+alpha))

            
    window.fill((0,0,0))
    #print(bone.bones[0].angle,bone.bones[1].rotation,bone.bones[1].rotation)
    bone.classupdate(window)
    

    pygame.display.update()