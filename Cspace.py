import numpy as np
import matplotlib.pyplot as plt
'''
Generating the cspace of the maze:
'''
class c_space:
    #initilize all the variables
    def __init__(self, obj1, obj2, obj3, start, goal):
        self.L1 = None                     #link1
        self.L2 = None                      #link2
        self.obj1 = obj1                     #rhombus
        self.obj2 = obj2                      #triangle
        self.obj3 = obj3                       #oval
        self.start = start
        self.goal = goal
    
    #rotation matrix in 2D
    def rot(self, theta):
        t = np.deg2rad(theta)                   #converting degree into rad
        rot = np.array([[np.cos(t),np.sin(t)],
                       [-np.sin(t),np.cos(t)]])
        return rot
 
   #function for collision detection 
    def collision(self,link, obj):
        ax_set = set(np.round(link.T[0],1))    #x axes set for the link
        bx_set = set(np.round(obj.T[0],1))      #x axes set for the object
        ay_set = set(np.round(link.T[1],1))       #y axes set for the link
        by_set = set(np.round(obj.T[1],1))         #y axes set for the object
        collision = None

        #whether the link element belong to the object set
        if (ax_set & bx_set) and (ay_set & by_set):
            collision=True                                     #if yes then indicate collision
        else:
            collision=False                                 #else no collision
        return collision
    
    # train the modle
    def fit(self,arm1, arm2 ):
        map1 = []   #blank list for the cspace of rhombus
        map2 = []    #blank list for the cspace of triangle
        map3 = []     #blank list for the cspace of oval
        start = []
        goal = []
        P =[]          #blank list for storing the endeffetor ond joints position
        
        #rotation for link 1
        for i in range (360):
            #joint1 position
            self.L1=np.dot(arm1,self.rot(i))
            a = np.vstack(np.array([np.zeros(2),self.L1[-1]])).T  
            
            #rotation for link2
            for j in range (360):
                self.L2=(self.L1[-1]+np.dot(arm2,self.rot(i+j)))
                #endeffector position
                b = np.vstack(np.array([self.L1[-1],self.L2[-1]])).T 
                P.append(np.array([a,b]))
                # print(self.L2[-1])
                #checking the collision of the endeffector with rhombus
                #if collision occure then stroing the angle of joint0 and joint1   
                if self.collision(self.L2,self.obj1)==True:
                    map1.append(np.array([i,j]))  
                
                #checking the collision of the endeffector with triangle
                #if collision occure then stroing the angle of joint0 and joint1 
                elif self.collision(self.L2,self.obj2)==True:
                    map2.append(np.array([i,j]))       
                
                #checking the collision of the endeffector with oval
                #if collision occure then stroing the angle of joint0 and joint1 
                elif self.collision(self.L2,self.obj3)==True:
                    map3.append(np.array([i,j])) 
                       
                elif (set(np.round(self.L2[-1],1))==set(self.start))==True:
                    start.append(np.array([i,j]))
                    
                elif (set(np.round(self.L2[-1],1))==set(self.goal))==True:
                    goal.append(np.array([i,j]))
                    
        return np.vstack(map1),np.vstack(map2), np.vstack(map3), P, np.vstack(start),np.vstack(goal)