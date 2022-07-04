#coding=utf-8

#导入科学计算库
import numpy as np

#导入opencv-python
import cv2

#获取摄像头
cap = cv2.VideoCapture(0)

#指定videoWriter的fourCC视频编码
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

#指定输出文件，fourcc视频编码，FPS帧率、画面大小
#fourcc :视频编码
#FPS：帧率、
#画面大小
out = cv2.VideoWriter('output.avi',fourcc,24.0,(640,480))
while cap.isOpened():
    ret,frame = cap.read()
    #视频
    frame=cv2.flip(frame,0)
    out.write(frame)
    cv2.imshow('frame',frame)
    if not ret:
        print("无法打开摄像头")
    if cv2.waitKey(25) == 27:
        break

out.close()
cap.release()
cv2.destroyAllWindows()