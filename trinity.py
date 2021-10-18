#importing the libraries
import matplotlib.pyplot as plt
import numpy as np
import math

# BOTTOM ARC
# using linspace to get the angle points
t1 = np.linspace(0,np.pi,33)  
# initialising the x1 array
x1 = []  
# loop to insert the x coordinates
for j in t1:
    # formula of calculating x coordinates
    # if (Cx,Cy) is the center of the circle and radius = r
    # then x = Cx + (r * cosine(angle))
    # here 1 is the radius and 0 is y coordinate of center point
    x= 0 + 1 * np.cos(j) 
    # appending values to the x1 list
    x1.append(x)
# initialising y1 array    
y1 = []
for i in t1:   # getting the points of y axis
    # formula of calculating y coordinates
    # if (Cx,Cy) is the center of the circle and radius = r
    # then y = Cy + (r * sine(angle))
    # here 1 is the radius and 0 is y coordinate of center point
    y = 0 + 1 * np.sin(i)  
    # appending values to the y1 list
    y1.append(y)
# plotting the points of x1 and y1 with line color turquoise and width = 4
plt.plot(x1, y1, color='turquoise', linewidth=4)

# RIGHT ARC
# using linspace to get the angle points
t2 = np.linspace(2*np.pi/3, 5*np.pi/3, 33)
# initialising the x2 array
x2 = []
# loop to insert the x coordinates
for j in t2:
    # here 1 is the radius and 0.5 is y coordinate of center point
    xa= 0.5 + 1 * np.cos(j)  
    x2.append(xa)
y2 = []
for i in t2:
    sq = math.sqrt(3)
    # here 1 is the radius and √3/2 is y coordinate of center point
    ya = sq/2 + 1 * np.sin(i)
    y2.append(ya)
# plotting the points of x2 adn y2 with line color turquoise and width = 4
plt.plot(x2,y2, color='turquoise', linewidth=4)

# LEFT ARC
# using linspace to get the angle points
t3 = np.linspace(-2*np.pi/3, np.pi/3, 33)
# initialising the x2 array
x3 = []
# loop to insert the x coordinates
for j in t3:
    # here 1 is the radius and -0.5 is y coordinate of center point
    xb= -0.5 + 1 * np.cos(j)
    x3.append(xb)
y3 = []
for i in t3:
    sq = math.sqrt(3)
    # here 1 is the radius and √3/2 is y coordinate of center point
    yb = sq/2 + 1 * np.sin(i)
    y3.append(yb)
# plotting the points of x3 and y3 with line color turquoise and width = 4
plt.plot(x3,y3, color='turquoise', linewidth=4)

# Display the Triquetra
plt.axis("equal")
plt.title('Triquetra')
plt.show()
