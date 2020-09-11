import cv2

cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (frame_width,frame_height))
while cap.isOpened():

    ret, frame = cap.read()
    if ret == True:
        out.write(frame)

        cv2.imshow('frame', frame)
        #press 'q' to stop shooting
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
out.release()


cap1 = cv2.VideoCapture('output.avi')
while cap1.isOpened():
    ret, frame = cap1.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.cv2.COLOR_GRAY2BGR)
    gray = cv2.line(gray, (20, 400), (150, 200), (0, 125, 0), 5)
    gray = cv2.rectangle(gray, (500, 500), (600, 700), (255, 0, 0), 8)
    cv2.imshow('gray', gray)
    
    if cv2.waitKey(1) == ord('q'):
        break
cap1.release()
cv2.destroyAllWindows()