Face Authentication Attendance System

Overview  
This project is a real-time face recognition based attendance system built using Python and OpenCV. It automates the attendance process by authenticating users through facial recognition using a live webcam feed.

The system is designed as an internship-level practical implementation to demonstrate computer vision concepts such as face detection, face recognition, real-time processing, and basic liveness checking.

---

Key Features  
Real-time face authentication using webcam  
Face registration and dataset creation  
Face model training using LBPH Face Recognizer  
Punch-In and Punch-Out attendance system  
Basic lighting normalization for better accuracy  
Simple spoof prevention using face movement check  
Automatic attendance logging to CSV file  

---

Technologies Used  
Python  
OpenCV  
NumPy  
Haar Cascade Classifier  
LBPH Face Recognizer  

---

Project Structure  

dataset/  
register_face.py  
train_model.py  
attendance.py  
README.md  

---

Setup and Installation  

1. Clone or download the repository  
2. Install required dependencies  

pip install opencv-python opencv-contrib-python numpy  

---

How to Run  

Step 1: Register Face  
python register_face.py  

Step 2: Train Face Model  
python train_model.py  

Step 3: Run Attendance System  
python attendance.py  

---

Controls  

Press I for Punch-In  
Press O for Punch-Out  
Press ESC to Exit  

---

Output  

attendance.csv file is automatically created and updated with:  
Name  
Date  
Time  
Punch Type  

---

Accuracy  

In good lighting conditions, the system achieves approximately 85 to 95 percent accuracy. Actual performance depends on camera quality, lighting, and face visibility.

---

Limitations  

Advanced liveness detection is not implemented  
Low light environments may reduce accuracy  
Face masks or occlusions may affect recognition  
Not suitable for high-security environments  

---

Learning Outcome  

This project helped me gain hands-on experience with real-time computer vision, face recognition systems, and integrating AI concepts into a practical application.

---

Author  

Raj Shukla  

