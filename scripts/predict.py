import cv2
import pytesseract
import re
import os
import numpy as np
from textblob import TextBlob


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    """
    Preprocesses the image for better OCR accuracy.
    """
    if not os.path.exists(image_path):
        print(f"❌ Error: Image not found at {image_path}")
        return None
    
    image = cv2.imread(image_path)
    if image is None:
        print(f"❌ Error: Could not read the image at {image_path}")
        return None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    blurred = cv2.GaussianBlur(gray, (5,5), 0)  # Reduce noise
    _, thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Apply thresholding
    return thresholded

def extract_text(image_path):
    """
    Extracts text from a prescription image using OCR.
    """
    processed_image = preprocess_image(image_path)
    if processed_image is None:
        return "❌ OCR Failed: Image preprocessing issue."
    
    ocr_text = pytesseract.image_to_string(processed_image)
    return ocr_text.strip()

def correct_spelling(text):
    """
    Applies spell correction to improve OCR output.
    ⚠️ WARNING: Avoids modifying medical terms.
    """
    return str(TextBlob(text).correct())

def extract_prescription_details(ocr_text):
    """
    Extracts relevant information from the OCR text.
    """
    details = {}

    # Extract Doctor's Name (First Line with "Dr.")
    doctor_match = re.search(r'Dr\.?\s+[A-Za-z\s]+', ocr_text)
    details["Doctor"] = doctor_match.group().strip() if doctor_match else "Not Found"

    # Extract Address (Next Line after Doctor’s Name)
    address_lines = ocr_text.split("\n")
    if len(address_lines) > 1:
        details["Address"] = address_lines[1].strip()
    else:
        details["Address"] = "Not Found"

    # Extract Date (Common formats like 12-12-2024, 12/12/24, 12 Dec 2024)
    date_match = re.search(r'\b\d{1,2}[-/\s]?[A-Za-z]*[-/\s]?\d{2,4}\b', ocr_text)
    details["Date"] = date_match.group() if date_match else "Not Found"

    # Extract Medicines 
    medicine_match = re.findall(r'(?:R/|Rx:|Medicines:)\s*(.*)', ocr_text)
    details["Medicines"] = [med.strip() for med in medicine_match] if medicine_match else ["Not Found"]

    return details

def process_prescription(image_path):
    """
    Full pipeline: Extract text -> Post-process -> Extract structured data.
    """
    raw_text = extract_text(image_path)
    if "❌ OCR Failed" in raw_text:
        return

    corrected_text = correct_spelling(raw_text)  # Spell Correction
    details = extract_prescription_details(corrected_text)

    print("\n📝 **Extracted Prescription Details:**\n")
    for key, value in details.items():
        print(f"{key}: {value}")

    return details

if __name__ == "__main__":
    image_path = input("Enter the path to the prescription image: ").strip().replace('"', '')
    process_prescription(image_path)
