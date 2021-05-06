import cv2
refPt = []
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Co-ordinates",x,",",y)
        refPt.append([x,y])
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x)+", "+str(y)
        cv2.putText(img, strXY, (x,y), font, 0.5, (255,255,0), 0)
        cv2.imshow("image", img)

    elif event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        #strBGR = str(blue)+", "+str(green)+","+str(red)
        a=int(blue)
        print("Blue",a)
        b=int(green)    
        print("Green",b)
        c=int(red)
        print("Red",c)
        largest=0
        if (a > b) and (a > c):
            print("Most prominent colour is Blue")
            largest = a
            largest="BLUE"
        elif (b > a) and (b > c):
            print("Most prominent colour is Green")
            largest = b
            largest="Green"
        elif(c>a and c>b):
            print("Most prominent colour is Red")
            largest = c
            largest ="Red" 
        elif (a==b==c == 0 ):
            largest="Black"
            print("Here it is Black Colour")
        elif (a==b==c ==255):
            largest="White"
            print("Here it is White colour")
        else:
            pass
        strBGR = largest        
        #print(largest)
        cv2.putText(img, strBGR, (x,y), font, 0.5, (0,255,255), 0)
        cv2.imshow("image", img)

    else:
        pass

img = cv2.imread("hello25.png")
cv2.imshow("image", img)
cv2.setMouseCallback("image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()