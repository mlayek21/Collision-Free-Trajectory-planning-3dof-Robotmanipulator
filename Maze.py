import numpy as np
import matplotlib.pyplot as plt


"""
Generating object for the maze:
"""

class maze:
    # function for generating Rhombus object
    def obj1(a,x,y):
        X = []
        Y = []
        for i in range (10*a):
            for j in range(10*a):
                Y.append(j)
                X.append(i)
        d = np.dot((np.array([X,Y]).T/20),np.array([[1,1],[-1,1]]) )       
        return (d+np.array([x,y]))

    # function for generating Triangle object
    def obj2(r,x,y):
        X = []
        Y = []
        for i in range (10*r):
            for j in range(i):
                Y.append(2.5*j+1.5*i)
                X.append(3.5*i)
        return (np.array([X,Y]).T)/25+np.array([x,y])

    # function for generating Oval object
    def obj3(r,x,y):
        X = []
        a = np.arange(0,r,0.25)
        b = np.zeros(len(a))
        m = np.vstack(np.array([a,b])).T
        for i in range (360):
            t = np.deg2rad(i)
            rot = np.array([[np.cos(t),np.sin(t)],[-np.sin(t),np.cos(t)]])
            X.append(np.dot(m,rot))
        n=np.dot(np.vstack(X),np.array([[1,0],
                                       [0,1.5]]))
        return n/1.5+np.array([x,y])
    
    # function for generating link 1, link2
    def links(a,b):
        Link1 = np.array([[np.arange(0,a,0.1)],[np.zeros(np.arange(0,a,0.1).shape)]])
        Link2 = np.array([[np.arange(0,b,0.1)],[np.zeros(np.arange(0,b,0.1).shape)]])
        return np.vstack(Link1).T,np.vstack(Link2).T
    
    # function for generating maze size in Cartesian Space 
    def getFigure( sizex , sizey ):
        fig = plt.figure( figsize = (sizex, sizey) )
        return fig