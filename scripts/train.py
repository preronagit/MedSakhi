import os
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from scripts.preprocess import preprocess_image  # Importing preprocessing function

DATASET_DIR = "dataset"
TRAIN_CSV = os.path.join(DATASET_DIR, "train_labels.csv")
TEST_CSV = os.path.join(DATASET_DIR, "test_labels.csv")
VAL_CSV = os.path.join(DATASET_DIR, "val_labels.csv")

# Read CSV files
train_df = pd.read_csv(TRAIN_CSV)
test_df = pd.read_csv(TEST_CSV)
val_df = pd.read_csv(VAL_CSV)


label_col = "MEDICINE_NAME"  
train_df[label_col] = train_df[label_col].astype(str)
test_df[label_col] = test_df[label_col].astype(str)
val_df[label_col] = val_df[label_col].astype(str)

# Get unique medicine names as labels
unique_labels = train_df[label_col].unique()
label_to_index = {label: i for i, label in enumerate(unique_labels)}

# Function to load and preprocess images
def load_images(df, dataset_type):
    images, labels = [], []
    IMAGE_DIR = os.path.join(DATASET_DIR, dataset_type)

    for _, row in df.iterrows():
        image_path = os.path.join(IMAGE_DIR, row["IMAGE"])
        if os.path.exists(image_path):
            processed_image = preprocess_image(image_path)
            images.append(processed_image)
            labels.append(label_to_index[row[label_col]])

    return np.array(images).reshape(-1, 128, 128, 1), to_categorical(labels, num_classes=len(unique_labels))

# Load training, validation, and test datasets
X_train, y_train = load_images(train_df, "train")
X_val, y_val = load_images(val_df, "val")
X_test, y_test = load_images(test_df, "test")

# Apply data augmentation
datagen = ImageDataGenerator(
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=False,
    fill_mode="nearest"
)

# Define CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 1)),
    MaxPooling2D((2, 2)),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),

    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),  # Prevent overfitting
    Dense(64, activation='relu'),
    Dense(len(unique_labels), activation='softmax')
])

# Compile model
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss="categorical_crossentropy",
              metrics=["accuracy"])

# Train model
model.fit(datagen.flow(X_train, y_train, batch_size=32),
          validation_data=(X_val, y_val),
          epochs=20)

# Evaluate on test data
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc * 100:.2f}%")

# Save trained model
MODEL_PATH = "model/handwriting_model.h5"
model.save(MODEL_PATH)
print(f"Model saved at: {MODEL_PATH}")
