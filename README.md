# MedSakhi

## 📌 Problem Statement
In many regions, patients struggle with deciphering doctors' handwritten prescriptions, leading to medication errors. Additionally, pharmacists often face difficulties in verifying prescriptions, increasing the risk of incorrect medication dispensing. **MedSakhi** is an AI-powered prescription assistant that extracts, analyzes, and verifies handwritten prescriptions to ensure accuracy and accessibility.

---

## ✅ Solution Overview
**MedSakhi** leverages Optical Character Recognition (OCR) and Deep Learning to extract text from prescriptions, validate medicine information, and suggest alternatives if needed. The system is designed to enhance medication safety and improve efficiency in pharmacies.

---

## 📖 Table of Contents

- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Directory Structure](#-directory-structure)
- [AI Integration](#-ai-integration)
- [Features](#-features)
- [References & Dataset](#-references--dataset)

---

## 🛠 Tech Stack
- **Pandas**
- **Numpy**
- **MatPlotLib**
- **Scikit-Learn**
- **TensorFlow**
- **Keras**
- **OpenCV**
- **Tesseract OCR**
- **GitHub**
- **CSV Files**
- **Virtual Environment (venv)**

---

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/preronagit/MedSakhi.git
   cd MedSakhi
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the dataset and models from Google Drive:
   ```bash
   wget --no-check-certificate "https://drive.google.com/uc?export=download&id=1XUQ_39GVvTNT1qzCpyv3z3Q7zc3Hm0pS" -O dataset.zip
   wget --no-check-certificate "https://drive.google.com/uc?export=download&id=1a4UnF6DYNy30YtPzer9uBQAirj3ABQaJ" -O model.zip
   ```
   Extract them:
   ```bash
   unzip dataset.zip -d dataset/
   unzip model.zip -d model/
   ```

---

## 🏗 Usage
### Activate the Virtual Environment:
**On Windows:**
```bash
.venv\Scripts\Activate
```
**On macOS and Linux:**
```bash
source .venv/bin/Activate
```
### Run the prescription processing pipeline:
```bash
python main.py
```
Follow the prompts to upload an image of a prescription and get extracted medication details.

---

## 📂 Directory Structure
```
MedSakhi/
│-- dataset/          # Training dataset (Download separately)
│-- model/            # Trained models (Download separately)
│-- scripts/
│   │-- preprocess.py # Preprocessing pipeline
│   │-- train.py      # Model training script
│   │-- predict.py    # Prescription text extraction
│   │-- order.py      # Medicine verification & ordering
│-- main.py           # Entry point
│-- requirements.txt  # Dependencies
│-- README.md         # Documentation
```

---

## 🤖 AI Integration
MedSakhi integrates AI-driven techniques to extract, analyze, and validate handwritten prescriptions efficiently:
- **OCR (Optical Character Recognition)**: Uses Tesseract OCR to extract text from images.
- **Deep Learning (CNN & LSTM)**: Deep Learning models process extracted text for structured information retrieval.


---

## ✨ Features
- 📸 **Handwritten Prescription Recognition**: Extracts text from scanned prescriptions.
- 🔍 **Text Extraction & Spell Correction**: Enhances accuracy by correcting OCR errors.
- 💊 **Medicine Verification**: Checks prescribed medicines and verifies them with the database.
  
- 🏥 **Auto Order Creation**: Creates orders for seamless transactions

---

## 📚 References & Dataset
### 🔗 **Dataset Used**
- [Doctors' Handwritten Prescription Dataset](https://www.kaggle.com/datasets/mamun1113/doctors-handwritten-prescription-bd-dataset)

### 📄 **Research Papers**
- E. Hassan et al., "Medical Prescription Recognition using Machine Learning," IEEE CCWC 2021. DOI: [10.1109/CCWC51732.2021.9376141](https://doi.org/10.1109/CCWC51732.2021.9376141)

---

🚀 **MedSakhi** aims to enhance prescription readability and medication safety through AI-driven automation. Let's revolutionize healthcare together! 🎯

