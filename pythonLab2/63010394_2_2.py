import math

class Spherical:
    radius = 0
    def __init__(self,r):
        self.radius = r
    def changeR(self,Radius):
       self.radius = Radius
    def findVolume(self):
        z = math.pow(self.radius,3)
        return (math.pi/3*4*z)
    def findArea(self):
        return self.radius*self.radius*math.pi*4
    def __str__(self):
        return f"Radius ={self.radius} Volumn = {self.findVolume()} Area = {self.findArea()}"
r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)
'''
x = (4/3)*math.pi*27.0
print(x)
'''