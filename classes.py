import pygame
from vector import vector
import math



class bone:

    bones = []
    
    def __init__(self,length,rotation,head=vector(0,0),parent=None):
    
        rotation = math.radians(rotation)

        self.head = head
        self.parent = parent
        self.rotation = rotation
        self.angle = rotation

        if parent!=None:
            
            print(bone.bones[parent].angle)
            self.angle = rotation+bone.bones[parent].angle
            self.head = bone.bones[parent].tail

        self.length = length
        self.rotation = rotation

        self.tail = self.head + vector(length*math.cos(self.angle),length*math.sin(self.angle))

        bone.bones.append(self)

    def rotate(self,angle):
        angle = self.rotation+math.radians(angle)
        self.tail = self.head + vector(self.length*math.cos(angle),self.length*math.sin(angle))
        self.rotation = angle
        self.angle = angle

    def rotateAbs(self,angle):

        self.tail = self.head + vector(self.length*math.cos(angle),self.length*math.sin(angle))
        self.rotation = angle
        self.angle = angle

    def update(self,win):
        
        if self.parent!=None:
            self.head = bone.bones[self.parent].tail
            self.angle = bone.bones[self.parent].angle + self.rotation
            self.tail = self.head + vector(self.length*math.cos(self.angle),self.length*math.sin(self.angle))
            

        self.display(win)

    @classmethod
    def classupdate(cls,win):
        for i in cls.bones:
            i.update(win)

    def display(self,win):
        pygame.draw.line(win,(255,255,255),self.head.tupAdj(),self.tail.tupAdj())
    
    