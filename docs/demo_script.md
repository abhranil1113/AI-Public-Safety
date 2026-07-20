# Demo Script: AI for Digital Public Safety Platform

Follow this step-by-step script to walk judges or users through the prototype functionality.

## 🚀 Step 1: Initializing the Interface
Run the main script without arguments:
```bash
python main.py
```
Expected output: The interactive console menu displays with choices 1 to 6.

---

## 📞 Step 2: Testing Digital Arrest Scam Detection
1. Select **Option 1**.
2. When prompted for a transcript, paste the following text:
   > "I am calling from CBI Delhi headquarters. Your Aadhaar card has been found linked to a money laundering case. You are under digital arrest and must keep your video camera on. Do not contact anyone or you will face immediate police arrest."
3. Expected Output:
   - Risk Rating: **🚨 HIGH**
   - Prediction: **SCAM**
   - Confidence: **> 80.00%**
   - Reasoning: Mentions impersonation cues (CBI, Aadhaar, money laundering, digital arrest).

---

## 💰 Step 3: Testing Counterfeit Currency Detection
1. Select **Option 2**.
2. Enter the path:
   `datasets/currency/test/fake/fake_500_1.png`
   *(If you enter a non-existent path, the system will fall back to the first available mock image).*
3. Expected Output:
   - Prediction: **FAKE**
   - Alert: **🚨 SUSPICIOUS (COUNTERFEIT DETECTED)**
   - Features Extracted: `thread_continuity` value will be lower than `1.0` (indicates broken security thread).

---

## 🕸️ Step 4: Testing Fraud Network Graph Intelligence
1. Select **Option 3**.
2. Expected Output:
   - A list of identified money mule accounts.
   - Total volume of fraudulent transactions flowing into each mule.
   - Connected active device IDs (detecting syndicates sharing devices).
   - High/Medium risk level assessment.

---

## 🗺️ Step 5: Testing Geospatial Hotspot Detection
1. Select **Option 4**.
2. Expected Output:
   - A prioritised list of crime hotspots.
   - Outputs a table ranking districts (e.g. New Delhi, Mumbai, Bengaluru) by incident counts and financial loss.
   - Prioritization levels (CRITICAL, HIGH, MEDIUM, LOW).

---

## 🤖 Step 6: Running the Full Agentic Pipeline
1. Select **Option 5**.
2. Expected Output:
   - The Central Orchestrator runs all tasks in sequence.
   - Exports the following files:
     - `reports/intelligence_report.json`
     - `reports/intelligence_report.txt`
     - `reports/audit_log.csv` (SHA-256 hashed ledger)
     - `outputs/graphs/fraud_network.png` (dark network map)
     - `outputs/maps/hotspot_map.html` (interactive folium map)
     - Predictions folder populated with batch analysis CSVs.
   - Prints a confirmation table detailing all statistics and confirmation that the forensic audit log is secure.
