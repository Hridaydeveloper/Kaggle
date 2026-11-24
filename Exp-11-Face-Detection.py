Datasets: https://www.kaggle.com/datasets/memesstar/face-detection-dataset



import cv2
import matplotlib.pyplot as plt

# 1. Load face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml"
)

# 2. Image paths
image_paths = [
    "/kaggle/input/datasets/memesstar/face-detection-dataset/human_img.jpg",
    "/kaggle/input/datasets/memesstar/face-detection-dataset/computer-img.jpg"
]

# 3. Process images
for path in image_paths:

    img = cv2.imread(path)

    if img is None:
        print("Image not found:", path)
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Improve image contrast
    gray = cv2.equalizeHist(gray)

    # 4. Detect faces with stricter settings
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(80, 80)
    )

    # 5. Display detection result
    if len(faces) > 0:

        for (x, y, w, h) in faces:
            cv2.rectangle(
                img, (x, y), (x+w, y+h),
                (0, 255, 0), 2
            )

        print("\nFace Detected in this image!")
        print("Image Path: ", path)
        
        # print("Image:", path.split("/")[-1])
        # print("Number of faces detected:", len(faces))
    
        # 6. Display image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
        plt.figure(figsize=(8, 5))
        plt.imshow(img)
        plt.title("Face Detected")
        plt.axis("off")
        plt.show()
        

    else:
        print("\nFace Not Detected in this image!")
        print("Image path: ", path)
    
        # 6. Display image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
        plt.figure(figsize=(8, 5))
        plt.imshow(img)
        plt.title("Face Not Detected")
        plt.axis("off")
        plt.show()






import os

print("Checking Kaggle input folder...")

if os.path.exists("/kaggle/input"):
    print("Input folder exists!")

    for root, dirs, files in os.walk("/kaggle/input"):
        print("\nFolder:", root)
        print("Files:", files)

else:
    print("Kaggle input folder not found!")
