import cv2
import time

cap = cv2.VideoCapture(0)
time.sleep(2)
ret, frame = cap.read()
print(cap.isOpened())
cv2.imwrite('sample.jpg', frame)
img = cv2.imread('sample.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(gray, cv2.cv2.COLOR_GRAY2BGR)
gray = cv2.line(gray,(20,400),(150,200),(0,125,0),5)
gray = cv2.rectangle(gray, (500, 500), (600, 700), (255, 0, 0), 8)

cv2.imshow('frame', frame)
cv2.imshow('gray', gray)

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()