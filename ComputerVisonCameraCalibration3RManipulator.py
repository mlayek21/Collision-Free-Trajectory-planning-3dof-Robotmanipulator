from inspect import getcallargs
from tkinter.dnd import DndHandler
import cv2
import numpy as np
from spatialmath.base import *
import sympy as sp

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
 
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    i=1
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area>250:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            print(i," area",area)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            # print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            print(i," xOld and yOld")
            print(x+w/2,y+h/2, "\n")
            print(i," xnew and ynew")
            print([5.2*(x+w/2),  5.2*(y+h/2)], "\n")
            if objCor ==3: 
                objectType ="_"
                
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio >0.98 and aspRatio <1.03: 
                    objectType= "Square"
                    print(x+w/2,y+h/2)
                    
                else:
                    objectType="Rectangle"
                    print(x+w/2,y+h/2)
            elif objCor>4: objectType= " _"
            else:objectType="None"
        
 
 
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2)
            i=i+1
    return [5.2*(x+w/2),  5.2*(y+h/2)]

path = 'img5.jpg'
img = cv2.imread(path)
sz = img.shape[0:2]
img=cv2.resize(img,[600,800])
rx = sz[0]/800; ry = sz[1]/600
imgContour = img.copy()
 
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
px=getContours(imgCanny)
 
imgBlank = np.zeros_like(img)

print("px ",px)

print("sz",sz)
# p = np.array([(px[0]-sz[1]/2)*0.2645833333, (-px[1]+sz[0]/2)*0.2645833333, 0,1])

p=np.array([[-1*0.2645833333, 0, 0, 4160/2*0.2645833333 ],
            [ 0, -1*0.2645833333 , 0, 3120/2*0.2645833333 ],
            [0 ,0,1,0],
            [0,0,0,1]])@np.array([(px[0])*0.2645833333, (px[1])*0.2645833333, 0,1])

# p = np.array([(px[0])*0.2645833333, (px[1])*0.2645833333, 0,1])
print(p)
# with open('readme.txt','w') as f:
#     f.write(p)
f=3.47; 

l = 878-1.2
xc=577; yc=430; zc=878
# f = sp.symbols('f')
pTc= sp.Matrix([[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, f, f*l/(f-l)],
                [0, 0, 1, f/(f-l)]])
pn=pTc@p.T
pn=pn/pn[3]

# print("pn",pn)
rot = roty(180,'deg')@rotz(180,'deg')
rot = np.linalg.inv(rot)
h = np.hstack((rot,np.array([xc,yc,zc]).reshape(3,1)))
cTb = np.vstack((h,np.array([0,0,0,1]).reshape(1,4)))
# print(cTb)
          
pTb= cTb@pn
# print("ptb",pTb)
# pTb=pTb/pTb[3]
print("part coordinate wrt to base\n",pTb.T)
# s1=sp.nonlinsolve([pTb[0]-240],f)
# print(s1)

cv2.imshow("ContorImg", imgContour) 
cv2.waitKey(0)
