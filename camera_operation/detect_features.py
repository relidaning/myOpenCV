#coding=utf-8

import cv2
#载入人脸检测器

face_cascade=cv2.CascadeClassifier("../data/haarcascades/haarcascade_frontalface_default.xml")
#载入眼睛检测器
eye_cascade=cv2.CascadeClassifier("../data/haarcascades/haarcascade_eye.xml")
#载入笑容检测器
smile_cascade=cv2.CascadeClassifier("../data/haarcascades/haarcascade_smile.xml")

#调用摄像头
cap = cv2.VideoCapture(0)

while (True):
    #获取摄像头拍摄到的图像
    ret ,frame = cap.read()

    faces=face_cascade.detectMultiScale(frame, 1.3, 2)
    img=frame
    for (x,y,w,h) in faces:
        #画出人脸框，蓝色，画笔宽度微
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        face_area=img[y:y+h,x:x+w]
        # 画出人脸框，在人脸区域而不是全图中进行人眼检测，节省计算资源
        eyes = eye_cascade.detectMultiScale(face_area,1.3,10)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(face_area,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)

        ##微笑检测
        smiles = smile_cascade.detectMultiScale(face_area,scaleFactor=1.16,minNeighbors=65,minSize=(25,25),flags=cv2.CASCADE_SCALE_IMAGE)
        for (ex, ey, ew, eh) in smiles:
            cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 1)
            cv2.putText(img,'Smile',(x,y-7),3,1.2,(0,0,255),2,cv2.LINE_AA)
        cv2.imshow("my_windows", img)

    key_pressed = cv2.waitKey(60)
    print("键盘上被按下的键提示",key_pressed)
    if key_pressed == 27:
        break

cap.release()
cv2.destroyAllWindows()