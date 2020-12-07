
import cv2 
import numpy as np


cap = cv2.VideoCapture(0)


while(1):

        ret,frame  = cap.read()

       # hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        #definerangeofredcolorinHSV\n",
        #lower_red=np.array([30,150,50])
        #upper_red=np.array([255,255,180])

        #create are HSV colour boundary and
        #thresholdHSVimage\n",
       #mask=cv2.inRange(hsv,lower_red,upper_red)

        #Bitwise-ANDmaskandoriginalimage\n",
        #res =cv2.bitwise_and(frame,frame,mask=mask)

        #Displayanoriginalimage
        
        cv2.imshow('Original',frame)

        #findsedgesintheinputimageimageand
        #marksthemintheoutputmapedges
        edges=cv2.Canny(frame,100,200)

        #Displayedgesinaframe\n",
        cv2.imshow('Edges',edges)
        #WaitforEsckeytostop\n",
        k=cv2.waitKey(5)
        if k==27:
            break


cap.release()

cv2.destroyAllWindows()

