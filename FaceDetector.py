import cv2

face_cascade = cv2.CascadeClassifier(r'C:\Users\akhil\Downloads\haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)
while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.05,5)
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imshow(('Capturing'),frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()