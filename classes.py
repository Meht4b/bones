import pygame
from vector import vector
import math



class bone:

    bones = []
    
    def __init__(self,length,LocalRotation,parent=None,ik=False,head=vector(0,0)):
        
        self.head = head
        self.parent = parent
        self.ik = ik

        self.LocalRotation = LocalRotation
        self.GlobalRotation = LocalRotation

        if parent != None:
            self.head = bone.bones[parent].tail
            self.GlobalRotation = bone.bones[parent].GlobalRotation + self.LocalRotation                
                
        self.length = length
        self.tail = self.head + vector(self.length*math.cos(self.GlobalRotation),self.length*math.sin(self.GlobalRotation))

        bone.bones.append(self)

    def rotateGlobablAbsolute(self,angle):
        self.GlobalRotation = angle

    def rotateLocalAdditive(self,angle):
        self.LocalRotation+=angle
    
    def rotateLocalAbsolute(self,angle):
        self.LocalRotation = angle
        
    def inverseKinematics(self):
        x,y = pygame.mouse.get_pos()
        mouseVector = vector(x,y)
        parentObj = bone.bones[self.parent]

        bone.bones[self.parent].rotateGlobablAbsolute(0.1)

        if parentObj.length+self.length > (mouseVector-parentObj.head).magnitude():
            if x<self.head.x and y>self.head.y:
                gamma = math.atan(abs(y-parentObj.head.y)/abs(x-parentObj.head.x))
                alpha = (parentObj.length**2 -self.length**2 + (parentObj.head-mouseVector).magnitude()**2)/(2*parentObj.length*(parentObj.head-mouseVector).magnitude())
                bone.bones[self.parent].rotateGlobablAbsolute(3.14159-alpha-gamma)
                print(alpha,gamma)


    def update(self,win):
        if self.parent != None:           
            if self.ik:
                self.inverseKinematics()

            else:               
                self.GlobalRotation = bone.bones[self.parent].GlobalRotation + self.LocalRotation 
                
            self.head = bone.bones[self.parent].tail

        else:
            self.GlobalRotation = self.LocalRotation

        self.tail = self.head + vector(self.length*math.cos(self.GlobalRotation),self.length*math.sin(self.GlobalRotation))
        self.display(win)
        
    @classmethod
    def classupdate(cls,win):
        for i in cls.bones:
            i.update(win)

    def display(self,win):
        pygame.draw.line(win,(255,255,255),self.head.tupAdj(),self.tail.tupAdj())
        pygame.draw.rect(win,(255,0,0),(self.head.x-5,self.head.y-5,10,10))
        pygame.draw.rect(win,(255,0,0),(self.tail.x-5,self.tail.y-5,10,10))
    