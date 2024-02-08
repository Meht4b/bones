import math
import pygame

def coord(y):
    #return pygame.display.get_surface().get_size()[1]-y
    return y

class vector:
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y)
    
    def __sub__(self,other):
        return vector(self.x-other.x,self.y-other.y)
    
    def __mul__(self,other):
        if isinstance(other,float) or isinstance(other,int):
            return vector(self.x*other,self.y*other)
    
    def __truediv__(self,other):
        if isinstance(other,int):
            return vector(self.x*1/other,self.y*1/other)
    
    def __repr__(self):
        return f'{self.x},{self.y}'

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
        
    def unitVector(self):
        return vector(self.x/self.magnitude(),self.y/self.magnitude())

    def tup(self):
        return (self.x,self.y)
    
    def tupAdj(self):
        
        return (self.x,coord(self.y))
    
    
def equationroots( a, b, c): 
 
    # calculating discriminant using formula
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
    return (-b + sqrt_val)/(2 * a)
     

'''
    # checking condition for discriminant
    if dis > 0: 
        print("real and different roots") 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
     
    elif dis == 0: 
        print("real and same roots") 
        print(-b / (2 * a)) 
     
    # when discriminant is less than 0
    else:
        print("Complex Roots") 
'''