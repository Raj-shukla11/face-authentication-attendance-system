import cv2
import os
import numpy as np

dataset_path = "dataset"
faces = []
labels = []
label_map = {}
current_label = 0

for user in os.listdir(dataset_path):
    user_path = os.path.join(dataset_path, user)
    if not os.path.isdir(user_path):
        continue

    label_map[current_label] = user

    for img_name in os.listdir(user_path):
        img_path = os.path.join(user_path, img_name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        if img is None:
            continue

        faces.append(img)
        labels.append(current_label)

    current_label += 1

labels = np.array(labels, dtype='int32')

model = cv2.face.LBPHFaceRecognizer_create()
model.train(faces, labels)
model.save("face_model.yml")

print("Model trained successfully!")
print("Label Map:", label_map)

with open("label_map.txt", "w") as f:
    for k, v in label_map.items():
        f.write(f"{k}:{v}\n")
