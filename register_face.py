import cv2
import os

user_name = input("Enter user name: ")

dataset_path = "dataset"
user_path = os.path.join(dataset_path, user_name)

if not os.path.exists(user_path):
    os.makedirs(user_path)

cam = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

count = 0
print("Look at the camera. Capturing face images...")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        face_img = gray[y:y+h, x:x+w]
        cv2.imwrite(f"{user_path}/{count}.jpg", face_img)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow("Register Face", frame)

    if cv2.waitKey(1) == 27 or count >= 30:
        break

print("Face registration completed!")
cam.release()
cv2.destroyAllWindows()
