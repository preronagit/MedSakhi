import os
from scripts.predict import process_prescription
from scripts.order import generate_order

def main():
    
    image_path = input("Enter the path to the prescription image: ").strip().replace('"', '')

    if not os.path.exists(image_path):
        print("❌ Error: File does not exist.")
        return
    
    
    prescription_details = process_prescription(image_path)

    if not prescription_details or prescription_details.get("Medicines") == ["Not Found"]:
        print("❌ No medicines detected. Cannot generate order.")
        return

    
    generate_order(prescription_details)

if __name__ == "__main__":
    main()
