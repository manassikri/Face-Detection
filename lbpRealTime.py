import cv2


cam = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\lbpcascades\lbpcascade_frontalface.xml')
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
while True:
    
    ret_val,img=cam.read(0)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th =50.0


    faces = face_cascade.detectMultiScale(gray, 1.1, 12)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
        if (w*h > th):
            print "face deteced"

        
    cv2.imshow('output',img)
    




    
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
