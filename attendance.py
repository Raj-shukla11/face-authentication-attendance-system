import cv2
import csv
from datetime import datetime

label_map = {}
try:
    with open("label_map.txt", "r") as f:
        for line in f:
            k,v = line.strip().split(":")
            label_map[int(k)] = v
except:
    print("Label map not found.")

model = cv2.face.LBPHFaceRecognizer_create()
model.read("face_model.yml")

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cam = cv2.VideoCapture(0)

last_positions = {}
mode = "Punch-In"

print("Press I for Punch-In, O for Punch-Out, ESC to exit")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        face_img = gray[y:y+h, x:x+w]
        label, confidence = model.predict(face_img)
        name = label_map.get(label, "Unknown")

        prev = last_positions.get(name)
        current = (x,y)
        live = True
        if prev:
            dist = abs(prev[0]-x) + abs(prev[1]-y)
            if dist < 5:
                live = False
        last_positions[name] = current

        status = "LIVE" if live else "POSSIBLE SPOOF"

        cv2.putText(frame, f"{name} - {mode}", (x,y-25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
        cv2.putText(frame, status, (x,y-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        if live:
            with open("attendance.csv", "a", newline="") as file:
                writer = csv.writer(file)
                now = datetime.now()
                writer.writerow([name, now.date(), now.strftime("%H:%M:%S"), mode])

    cv2.imshow("Attendance System", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == ord('i'):
        mode = "Punch-In"
    elif key == ord('o'):
        mode = "Punch-Out"

cam.release()
cv2.destroyAllWindows()
