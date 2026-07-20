import os
import csv
import random
import numpy as np
import cv2
from datetime import datetime, timedelta

def generate_scam_data(base_dir):
    print("Generating noisy scam and normal call transcripts...")
    scam_templates = [
        "This is Officer Sharma from the Central Bureau of Investigation. Your Aadhaar card number {aadhaar} is linked to a drug trafficking case in Mumbai. You are under digital arrest. You must keep your camera on and stay in this room.",
        "Hello, this is Delhi Customs. We have intercepted a parcel sent in your name containing illegal passports and synthetic drugs. To avoid immediate police arrest, you must cooperate with our officers over Skype.",
        "Calling from Enforcement Directorate. A bank account under your name has laundered 2.5 Crore rupees. You must transfer your funds to a safe government holding account for verification immediately.",
        "Your mobile number is going to be blocked in 2 hours by TRAI due to illegal advertising. Connect to senior officials immediately by pressing 9.",
        "Congratulations! You have won a lottery of 25 Lakh Rupees from KBC. Please pay a processing fee of Rs 25,000 to release your funds.",
        # Ambiguous / spelling error scam cases (noise)
        "Urgent: CBI police officer call back immediately on 9876543210. Your card is frozen due to Mumbai court order.",
        "this is custom officer. your parcel has drug. go to skype call for digital arrest process now.",
        "TRAI warning: Mobile connection block in 1 hour. Press 9 to talk to executive about verification."
    ]
    
    normal_templates = [
        "Hey, can you send me the reports for the quarterly budget? We need to submit it to the manager by evening.",
        "Hello, I am calling from your internet provider. Is your Wi-Fi connection working fine now?",
        "Hi Mom, I will be late for dinner today. Please don't wait for me.",
        "Dear customer, your credit card statement is ready. Please pay by the due date to avoid interest.",
        "Hi, is this the delivery agent? I am not at home, please leave the package with the security guard.",
        # Borderline / Ambiguous normal cases (critical for test robustness)
        "Delhi Police Public Advisory: Beware of fraudsters impersonating CBI, ED or police on video calls. Do not agree to Skype verification or digital arrest. Report scam calls to 1930 immediately.",
        "HDFC Bank Security Update: Please complete your KYC verification online to keep your account active. We never ask for password.",
        "Your courier package from Mumbai customs requires tax payment verification. Please check status online.",
        "TRAI official message: Please link your Aadhaar card with your mobile number to avoid disconnect. Visit nearest franchise store."
    ]

    scam_calls_path = os.path.join(base_dir, "datasets", "scam_text", "scam_calls.csv")
    sample_inputs_path = os.path.join(base_dir, "datasets", "scam_text", "sample_scam_inputs.csv")

    calls = []
    sample_inputs = []

    # Generate 150 total records with noise
    for i in range(1, 151):
        is_scam = random.choice([0, 1])
        call_id = f"CALL_{1000 + i}"
        duration = random.randint(15, 700)
        
        if is_scam:
            template = random.choice(scam_templates)
            aadhaar = f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
            text = template.format(aadhaar=aadhaar) if "{aadhaar}" in template else template
            label = "scam"
            features = "digital_arrest,threat,verification"
        else:
            text = random.choice(normal_templates)
            label = "normal"
            features = "personal,business,advisory"

        calls.append([call_id, text, duration, label, features])
        sample_inputs.append([text, label])

    # Write scam_calls.csv
    with open(scam_calls_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["call_id", "transcription", "duration", "label", "features"])
        writer.writerows(calls)

    # Write sample_scam_inputs.csv
    with open(sample_inputs_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["text", "label"])
        writer.writerows(sample_inputs)

    print(f"Noisy scam data generated: {len(calls)} rows.")


def generate_currency_images(base_dir):
    print("Generating noisy currency note images and metadata...")
    
    metadata_path = os.path.join(base_dir, "datasets", "currency", "metadata.csv")
    metadata_rows = []
    
    subfolders = [
        ("train/real", 20, "real"),
        ("train/fake", 20, "fake"),
        ("test/real", 10, "real"),
        ("test/fake", 10, "fake")
    ]
    
    denominations = [100, 200, 500]
    
    for subfolder, count, label in subfolders:
        folder_path = os.path.join(base_dir, "datasets", "currency", subfolder)
        os.makedirs(folder_path, exist_ok=True)
        
        for i in range(1, count + 1):
            denom = random.choice(denominations)
            img_name = f"{label}_{denom}_{i}.png"
            img_path = os.path.join(folder_path, img_name)
            
            # note size 120 x 250
            img = np.zeros((120, 250, 3), dtype=np.uint8)
            
            # Introduce slight random variations in brightness
            noise_val = random.randint(-15, 15)
            
            if label == "real":
                # Real notes
                base_color = np.array([180, 200, 180]) + noise_val
                img[:] = np.clip(base_color, 0, 255).astype(np.uint8)
                
                # Security thread (green)
                cv2.line(img, (180, 0), (180, 120), (0, 150, 0), 3)
                
                # Microprint (sharp text)
                cv2.putText(img, "RBI RBI RBI", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (50, 50, 50), 1)
                
                # Add some simulated background noise to make it realistic (prevent 100% clean edges)
                gaussian_noise = np.random.normal(0, 5, img.shape).astype(np.uint8)
                img = cv2.add(img, gaussian_noise)
                
                security_thread = 1
                microprint = 1
            else:
                # Fake notes (imperfect print)
                base_color = np.array([155, 165, 155]) + noise_val
                img[:] = np.clip(base_color, 0, 255).astype(np.uint8)
                
                # Broken or off-color security thread (sometimes they print it, but broken)
                if random.choice([True, False]):
                    cv2.line(img, (180, 0), (180, 45), (10, 110, 10), 2)
                    cv2.line(img, (180, 75), (180, 120), (10, 110, 10), 2)
                else:
                    # Thread entirely missing or drawn as normal grey line
                    cv2.line(img, (180, 0), (180, 120), (100, 100, 100), 1)
                    
                # Smudged microprint
                cv2.putText(img, "R8I R8I R8I", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (80, 80, 80), 1)
                
                # Apply heavier gaussian noise to simulate bad printing press noise
                gaussian_noise = np.random.normal(0, 15, img.shape).astype(np.uint8)
                img = cv2.add(img, gaussian_noise)
                
                security_thread = random.choice([0, 1]) # Some fakes might visually simulate thread
                microprint = 0
            
            # Common text
            cv2.putText(img, f"Rs {denom}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (10, 10, 10), 2)
            cv2.putText(img, "RESERVE BANK OF INDIA", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (10, 10, 10), 1)
            
            serial_no = f"{random.randint(0, 9)}{random.choice(['A','B','C','D'])}{random.choice(['A','B','C','D'])} {random.randint(100000, 999999)}"
            cv2.putText(img, serial_no, (140, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (10, 10, 10), 1)
            
            cv2.imwrite(img_path, img)
            
            rel_img_path = f"{subfolder}/{img_name}"
            metadata_rows.append([
                rel_img_path, denom, label, serial_no, microprint, security_thread
            ])
            
    with open(metadata_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["image_path", "denomination", "label", "serial_number", "microprint_visible", "security_thread_ok"])
        writer.writerows(metadata_rows)
        
    print(f"Noisy currency images and metadata generated ({len(metadata_rows)} notes).")


def generate_transactions(base_dir):
    print("Generating transaction data...")
    tx_path = os.path.join(base_dir, "datasets", "transactions", "transactions.csv")
    sample_tx_path = os.path.join(base_dir, "datasets", "transactions", "sample_transactions.csv")
    
    accounts = [f"ACC_{random.randint(100000, 999999)}" for _ in range(50)]
    scammer_accounts = [f"MULE_{random.randint(10000, 99999)}" for _ in range(5)]
    
    txs = []
    start_time = datetime.now() - timedelta(days=30)
    
    for i in range(1, 301):
        tx_id = f"TX_{10000 + i}"
        amount = round(random.uniform(500, 500000), 2)
        timestamp = (start_time + timedelta(hours=i * 2.4)).strftime("%Y-%m-%d %H:%M:%S")
        device = f"DEV_{random.randint(100, 999)}"
        
        is_fraud = 0
        dest = random.choice(accounts)
        source = random.choice(accounts)
        
        # Coordinated scam/fraud behavior
        if random.random() < 0.15:
            is_fraud = 1
            dest = random.choice(scammer_accounts)
            amount = round(random.uniform(100000, 1500000), 2)
            device = "DEV_FRAUD_999"
            
        if source == dest:
            dest = f"ACC_{random.randint(100000, 999999)}"
            
        txs.append([tx_id, source, dest, amount, timestamp, is_fraud, device])

    for path in [tx_path, sample_tx_path]:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["transaction_id", "source_acc", "dest_acc", "amount", "timestamp", "is_fraud", "device_fingerprint"])
            writer.writerows(txs)
            
    print(f"Transaction data generated: {len(txs)} rows.")


def generate_complaints(base_dir):
    print("Generating complaints data...")
    complaints_path = os.path.join(base_dir, "datasets", "complaints", "complaints.csv")
    sample_complaints_path = os.path.join(base_dir, "datasets", "complaints", "sample_complaints.csv")
    
    districts = ["New Delhi", "Mumbai", "Bengaluru", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad", "Gurugram", "Noida"]
    scam_types = ["Digital Arrest", "Phishing", "Lottery Scam", "Counterfeit Currency", "Job Fraud"]
    
    names = ["Aarav", "Vivaan", "Aditya", "Sai", "Reyansh", "Krishna", "Ishaan", "Shaurya", "Atharva", "Arjun",
             "Diya", "Aanya", "Pari", "Pihu", "Riya", "Aadhya", "Ananya", "Ira", "Avani", "Prisha"]
             
    complaints = []
    start_time = datetime.now() - timedelta(days=20)
    
    for i in range(1, 101):
        comp_id = f"CMP_{2000 + i}"
        name = random.choice(names) + " " + random.choice(["Sharma", "Verma", "Patel", "Reddy", "Nair", "Das", "Joshi", "Gupta"])
        location = random.choice(districts)
        scam_type = random.choice(scam_types)
        amount_lost = random.randint(5000, 1200000) if scam_type != "Counterfeit Currency" else random.randint(500, 10000)
        timestamp = (start_time + timedelta(hours=i * 4)).strftime("%Y-%m-%d %H:%M:%S")
        
        scammer_num = f"+91 {random.randint(70000, 99999)} {random.randint(10000, 99999)}"
        scammer_acc = f"MULE_{random.randint(10000, 99999)}"
        
        complaints.append([comp_id, name, location, scam_type, amount_lost, timestamp, scammer_num, scammer_acc])

    for path in [complaints_path, sample_complaints_path]:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["complaint_id", "victim_name", "victim_location", "scam_type", "amount_lost", "timestamp", "scammer_number", "scammer_acc"])
            writer.writerows(complaints)
            
    print(f"Complaints generated: {len(complaints)} rows.")


def generate_geospatial_data(base_dir):
    print("Generating geospatial data...")
    districts_path = os.path.join(base_dir, "datasets", "geospatial", "crime_districts.csv")
    coords_path = os.path.join(base_dir, "datasets", "geospatial", "district_coordinates.csv")
    
    district_data = [
        ("New Delhi", "Delhi", 28.6139, 77.2090),
        ("Mumbai", "Maharashtra", 19.0760, 72.8777),
        ("Bengaluru", "Karnataka", 12.9716, 77.5946),
        ("Hyderabad", "Telangana", 17.3850, 78.4867),
        ("Chennai", "Tamil Nadu", 13.0827, 80.2707),
        ("Kolkata", "West Bengal", 22.5726, 88.3639),
        ("Pune", "Maharashtra", 18.5204, 73.8567),
        ("Ahmedabad", "Gujarat", 23.0225, 72.5714),
        ("Gurugram", "Haryana", 28.4595, 77.0266),
        ("Noida", "Uttar Pradesh", 28.5355, 77.3910)
    ]
    
    districts_csv = []
    coords_csv = []
    
    for i, (name, state, lat, lon) in enumerate(district_data, 1):
        crime_rate = round(random.uniform(5.0, 95.0), 2)
        hotspot_score = round(crime_rate * random.uniform(0.8, 1.2), 2)
        if hotspot_score > 100: hotspot_score = 100.0
        
        districts_csv.append([f"DIST_{100 + i}", name, state, crime_rate, hotspot_score])
        coords_csv.append([name, lat, lon])
        
    with open(districts_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["district_id", "district_name", "state", "crime_rate", "hotspot_score"])
        writer.writerows(districts_csv)
        
    with open(coords_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["district_name", "latitude", "longitude"])
        writer.writerows(coords_csv)
        
    print("Geospatial data generated.")


def main():
    base_dir = r"D:\Ai Public Safety"
    generate_scam_data(base_dir)
    generate_currency_images(base_dir)
    generate_transactions(base_dir)
    generate_complaints(base_dir)
    generate_geospatial_data(base_dir)
    print("All noisy sample datasets generated successfully!")

if __name__ == "__main__":
    main()
