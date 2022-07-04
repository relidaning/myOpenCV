#coding=utf-8

#导入opencv-python
import cv2

#传入本地视频
cap = cv2.VideoCapture('vocation.mp4')

#校验本地视频是否捕获成功，如果未成功则输出提示

if not cap.isOpened():
    print("无法打开视频")
    exit(1)

#获取视频的高，宽信息，cap.get 传入的参数可以是0-18的整数，也可以设置宽高等信息
print("WIDH",cap.get(3))
print("WIDH",cap.get(4))

"""
python detect.py  --source 0  --weights yolov5x.pt 
"""

#无限循环，直到触发break跳出
while True:
    #获取视频画面，返回ret,frame
    #ret的True/False反映是否捕获成功，frame是画面
    ret,frame = cap.read()
    #校验画面帧是否正确捕获，如果未成功则输出提示，跳出循环
    if not ret:
        print("无法获取画面")
        break

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame_show',gray)
    #检测时间25毫秒是最好的。
    if cv2.waitKey(25) == 27:
        break

cap.release()
cv2.destroyAllWindows()