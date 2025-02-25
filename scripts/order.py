import json
import os

def generate_order(prescription_details, output_dir="orders"):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the directory if it doesn’t exist

    patient_name = prescription_details.get("Patient", "Unknown_Patient")
    order_file = os.path.join(output_dir, f"{patient_name}_order.json")

    order_data = {
        "Doctor": prescription_details.get("Doctor", "Unknown"),
        "Address": prescription_details.get("Address", "Not Available"),
        "Date": prescription_details.get("Date", "Unknown"),
        "Medicines": prescription_details.get("Medicines", [])
    }

    with open(order_file, "w", encoding="utf-8") as f:
        json.dump(order_data, f, indent=4)

    print(f"✅ Order file generated: {order_file}")
    return order_file
