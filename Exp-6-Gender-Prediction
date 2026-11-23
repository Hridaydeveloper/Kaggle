import os
import cv2
import numpy as np
import kagglehub
from skimage.feature import hog
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Download dataset and get exact local path
dataset_path = kagglehub.dataset_download("jangedoo/utkface-new")
print("Dataset downloaded to:", dataset_path)

# 2. Collect valid image paths (skipping duplicate subfolders if present)
image_paths = []
seen_filenames = set()

for root, _, files in os.walk(dataset_path):
    for f in files:
        if f.endswith('.jpg') and f not in seen_filenames and len(f.split('_')) >= 4:
            seen_filenames.add(f)
            image_paths.append(os.path.join(root, f))

# Use first 5000 images for fast execution (remove [:5000] to use all ~23,700 images)
image_paths = image_paths[:5000]
print(f"Processing {len(image_paths)} unique images...")

# 3. Extract HOG Features and Labels
X, y = [], []
for path in image_paths:
    filename = os.path.basename(path)
    try:
        gender = int(filename.split('_')[1])  # 0 = Male, 1 = Female
        if gender not in (0, 1):
            continue

        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue

        img = cv2.resize(img, (64, 64))
        features = hog(img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2))
        X.append(features)
        y.append(gender)
    except ValueError:
        continue

X = np.array(X, dtype=np.float32)
y = np.array(y)

# 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 5. Scale and Apply PCA
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

pca = PCA(n_components=100, random_state=42)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# 6. Train & Evaluate Models
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train_pca, y_train)
print(f"Logistic Regression Accuracy: {accuracy_score(y_test, lr.predict(X_test_pca)):.4f}")

svm = SVC(kernel='rbf')
svm.fit(X_train_pca, y_train)
print(f"SVM Accuracy: {accuracy_score(y_test, svm.predict(X_test_pca)):.4f}")







def predict_gender(image_path):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        return "Image not found"

    img = cv2.resize(img, (64, 64))

    features = hog(
        img,
        orientations=9,
        pixels_per_cell=(8, 8),
        cells_per_block=(2, 2)
    )

    features = np.array(features).reshape(1, -1)

    features = scaler.transform(features)
    features = pca.transform(features)

    prediction = lr.predict(features)[0]

    return "Male" if prediction == 0 else "Female"





sample_path = image_paths[0]
actual_gender = "Female" if int(os.path.basename(sample_path).split('_')[1]) == 1 else "Male"

print("File:", os.path.basename(sample_path))
# print("Actual Gender:", actual_gender)
print("Gender Predicted:", predict_gender(sample_path))
