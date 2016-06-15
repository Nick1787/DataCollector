# THIS PROGRAM USES A MONTE-CARLO APPROACH TO DETERMINE THE MAXIMUM AREA OF A TRIANGLE 
# GIVE TWO SIDES OF THE TRIANGLE AND VARYING THE ANGLE BETWEEN THOSE SIDES.
#
#          /\
#         /  \
#       A/    \     AREA = 0.5(B*A*sin(C)) 
#       /      \
#      /c)______\
#          B 
#
# USING CALCULUS, THE ANSWER IS MAXIMUM AREA IS 90 degrees
#     
# FOR A TRIANGLE WITH B=3, A=3, THE MAX AREA IS 0.5*3*3*sin(90*pi/180) = 4.5
#

import DataCollector
import math
import numpy as np
import matplotlib.pyplot as plt

#Create a basic class for calculating the area of a triangle
class triangle(object):
    def __init__(self, A, B):
        self.A = A;
        self.B = B;
        
    def calcArea(self,angle):
        self.c = angle;
        self.area = 0.5*self.B*self.A*math.sin(self.c);
        
tri = triangle(3,3);

#Setup the DAta Collector
DC = DataCollector.DataCollector()
DC.addParams(['tri.A','tri.B','tri.c','tri.area','deg','rad'])

#Run the simulation
for c in range(0, 180):
    deg = c;
    rad = deg*3.1415/180;
    tri.calcArea(rad);
    DC.slurp();
    
#Find the maximum
area = DC.get('tri.area');
angle = DC.get('deg');
maxArea = np.max(area);
i = np.where(area==maxArea)
solution = angle[i][0]

#print out the solution
Soln = "The Maximum Area is %f when the angle is %f." % (maxArea, solution)
print(Soln)