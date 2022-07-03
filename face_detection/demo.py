import cv2 as cv

def markFace(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detector=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_detector.detectMultiScale(gray, 1.02, 5)
    for x,y,w,h in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), color=(255,255,255))

if __name__ == '__main__':
    img = cv.imread('lena.jpg')
    markFace(img)
    cv.imshow('img', img)
    cv.waitKey(0)
    cv.destroyAllWindows()