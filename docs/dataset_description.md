# Datasets Description

This project utilizes a combination of real-world metadata patterns, telecom scripts, and geographic coordinates to simulate and verify public safety threat detection.

## 📂 1. Scam Call Transcripts (`datasets/scam_text/`)
- **scam_calls.csv**: Contains 100 entries of synthesized telephone transcriptions. Half represent digital arrest scams referencing CBI/ED/TRAI/Customs enforcement officers threatening victims with arrest. The other half represent normal conversational dialogues.
- **sample_scam_inputs.csv**: 100 rows containing transcript inputs and labels for rapid testing.

## 📂 2. Currency Images (`datasets/currency/`)
- **metadata.csv**: Catalogues all currency note test files. Columns: `image_path`, `denomination`, `label` (real/fake), `serial_number`, `microprint_visible`, `security_thread_ok`.
- **train/ and test/**: Contains generated image note representations (PNGs) of ₹100, ₹200, and ₹500 bills. Real notes draw sharp text watermarks and continuous green lines for the security thread. Fake notes omit or break the line and smudge printing.

## 📂 3. Financial Transactions (`datasets/transactions/`)
- **transactions.csv / sample_transactions.csv**: 300 rows logging transaction details between source accounts and destination accounts. Includes transaction amount, timestamp, is_fraud flags, and device fingerprints. High-volume bursts towards mule accounts trigger security flags.

## 📂 4. Citizen Complaints (`datasets/complaints/`)
- **complaints.csv / sample_complaints.csv**: 100 records logging formal complaints reported to the platform. Captures victim names, geographical locations, scam types (Digital Arrest, Phishing, Counterfeit, etc.), amount lost, and scammer phone/account numbers.

## 📂 5. Geospatial coordinates (`datasets/geospatial/`)
- **crime_districts.csv**: Baseline crime levels and hotspot index scores across 10 major Indian district areas.
- **district_coordinates.csv**: Latitude and longitude mappings (e.g. New Delhi, Mumbai, Bengaluru) for folium map visual pins.
