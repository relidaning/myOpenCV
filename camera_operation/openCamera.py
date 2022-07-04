#coding=utf-8

import cv2 as cv

cap = cv.VideoCapture(cv.CAP_DSHOW)
cap.open(0)

while cap.isOpened():
    flag, frame = cap.read()
    cv.imshow('camera', frame)
    key_pressed = cv.waitKey(60)
    print('the key has been pressed.', key_pressed)
    if key_pressed == 27:
        break

cap.release()
cv.destroyAllWindows()