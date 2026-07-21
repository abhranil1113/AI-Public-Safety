# 🛡️ AI for Digital Public Safety Intelligence Platform — Completed Work

> An Agentic AI system that detects digital arrest scams, cloned voices, counterfeit currency, fraud networks, and crime hotspots — generating auditable intelligence reports and auto-drafted court evidence under Human-in-the-Loop workflows.

---

## 🚨 Problem Statement
- **1.14 million** cybercrime complaints in India (2023) — up 60% from 2022
- **₹1,776 crore** lost to digital arrest scams in just 9 months (2024)
- **Record FICN seizures** reported by RBI Annual Report 2025
- Law enforcement lacks **proactive intelligence** — only reactive investigation

---

## 💡 Solution Overview
Our **Agentic AI Digital Public Safety Platform** coordinates multiple specialized AI agents:

| Agent Name | Technology / Algorithms | Function & Responsibilities |
| :--- | :--- | :--- |
| 🧠 **ScamShield Agent** | NLP (TF-IDF + Logistic Reg) / LLM (Gemini) | Detect digital arrest patterns with explainable coercion indicators and threat timeline stage tracking |
| 🗣️ **VoiceGuard Agent** | Acoustic Speech AI (Jitter, Shimmer, Pitch) | Analyze vocal micro-fluctuations to identify deepfakes and machine-cloned voice clones |
| 💬 **CitizenShield Agent** | Conversational Chatbot (WhatsApp/IVR wrapper) | Audit citizen queries in regional languages (English, Hindi, Telugu, Tamil) and draft NCRP cybercrime reports |
| 💰 **NoteGuard Agent** | OpenCV Feature Extractions + Random Forest | Screen notes against visual checksheet parameters (Security Thread, Watermark, UV, Serial Prefix) |
| 🕸️ **FraudGraph Agent** | NetworkX MultiDiGraph (Mule Ring Clustered) | Analyze transaction flows, cluster nodes, and reveal hidden rings |
| 🗺️ **GeoWatch Agent** | GIS-based Spatial Crime Mapping | Locate hotspots, map district coordinate indices, and calculate actionable LEA patrol recommendations |
| 🎛️ **Orchestrator Agent** | Weighted Risk Fusion Engine | Combine Text (40%), Voice (20%), Graph (20%), and Geo (20%) scores into a consolidated overall risk rating |
| 🔒 **Audit Logger** | SHA-256 Cryptographic Chain Ledger | Compile tamper-proof audit trails (Section 65B-aligned) linked to officer approvals |

---

## ✨ Innovation Highlights
- **Multi-Agent AI Architecture**: Collaborative routing to dedicated domain agents.
- **Explainable AI**: Breaks down classification logic into explicit checkpoints.
- **Predictive Threat Timeline**: Maps digital arrest scams through sequential psychological coercion stages.
- **Multi-Source Risk Fusion**: Fuses NLP, voice acoustics, mule graph, and geospatial indices.
- **Court-Ready Evidence Packages**: Automatic generation of signed incident dossiers.
- **Cryptographic Audit Trails**: Tamper-proof logs designed to support audit trails aligned with the evidentiary requirements of Section 65B of the Indian Evidence Act.
- **Human-in-the-Loop (HITL) Workflow**: Enforcement actions are locked pending officer verification.
- **Voice Deepfake Detection**: Acoustic forensics based on vocal jitter, shimmer, and spectral variance.
- **Fraud Ring Intelligence**: Dynamic transaction ego-graph clustering exposing money mule rings.
- **Crime Hotspot Mapping**: GIS spatial priority indexing for LEA routing.

---

## 🧠 Core Intelligent Components

### 1. ScamShield Agent (Digital Arrest Classifier)
- **Coercion Indicators**: Evaluates text for explicit patterns (Authority Claims, Psychological Coercion, Isolation Cues, Payment Cues).
- **Threat Stage Timeline**: Tracks call progression: `Greeting` ➔ `Authority Claim` ➔ `Fear Creation` ➔ `Isolation` ➔ `Payment Demand` ➔ `Completed Scam`.
- **Algorithm Choice**: **Logistic Regression** (with TF-IDF) for explainable probabilities and weight inspection.

### 2. VoiceGuard Agent (Speech AI & Voice Spoofing Forensics)
- **Acoustic Profiling**: Measures pitch variance (Hz), Vocal Jitter %, Vocal Shimmer %, and Spectral Centroid SD to detect machine-synthesized voices.
- **Technology Choice**: **Acoustic feature engineering using speech signal analysis** (pitch variance, jitter, shimmer, spectral statistics). Lightweight handcrafted features were selected because they are interpretable and computationally efficient for forensic screening. OpenCV was used for supporting visual checksheet validation in the NoteGuard module.

### 3. CitizenShield Agent (Citizen Fraud Shield Advisor)
- Evaluates suspicious phone coordinates or messages and outputs risk summaries in 4 languages: **English, Hindi, Telugu, and Tamil**.
- Automatically drafts structured incident filings aligned with NCRP reporting workflows.

### 4. NoteGuard Agent (Currency CV Checksheet)
- Audits bills via explicit security features: Security Thread continuity, Watermark & Microprint sharpness, UV balance, and Serial Prefix regex.
- **Algorithm Choice**: **Random Forest** for structured feature checks, with CNN deep learning fallback support.

### 5. FraudGraph Agent (Coordinated Mule Rings)
- **NetworkX MultiDiGraph Modeling**: Maps transaction chains, nodes, devices, phone numbers, and NCRB complaints.
- Isolates money mule account rings and generates court evidence packs.

### 6. GeoWatch Agent (Geospatial Patrol Recommendations)
- GIS Crime Mapping using Folium to generate interactive hotspot maps and LEA routing advice.

---

## 🎛️ Multi-Source Risk Score Fusion
$$\text{FusedScore} = 0.40 \times \text{TextNLP} + 0.20 \times \text{VoiceAcoustics} + 0.20 \times \text{GraphMule} + 0.20 \times \text{GeoHotspot}$$

---

## 🔒 Human-in-the-Loop & Cryptographic Audit Ledgers
- **HITL Workflow**: Automated actions remain locked pending officer review and sign-off inside CLI.
- **Section 65B Admissibility**: Logs are chained with SHA-256 cryptographic hashes ($\text{Hash}_n = \text{SHA256}(\text{Event}_n + \text{Hash}_{n-1})$), guaranteeing evidence tamper-proof integrity.

---

## 📊 Generated Outputs (Tangible Artifacts)

Every full pipeline run produces the following auditable files:

| File | Description |
| :--- | :--- |
| `reports/intelligence_report.json` | Full structured intelligence package |
| `reports/intelligence_report.txt` | Human-readable summary for officers |
| `reports/audit_log.csv` | SHA-256 cryptographically chained audit trail |
| `outputs/maps/hotspot_map.html` | Interactive Leaflet crime heatmap |
| `outputs/graphs/fraud_network.png` | Fraud-ring network visualization |
| `outputs/predictions/counterfeit_report.json` | Per-note forensic breakdown |
| `outputs/predictions/ncrp_report.txt` | NCRP-style incident report |

---

## 🔒 Prototype Scope & Deployment Considerations
- **Prototype Scope**: Demonstrates the AI decision pipeline using synthetic datasets and simulated integrations.
- **Production Requirements**: Direct integration with Telecom CDR APIs, Banking IMPS/UPI APIs, authenticated NCRP endpoints, live audio stream ingestion, and mandatory human officer sign-off.

---

## 📚 Official References & Data Sources

1. **National Cyber Crime Reporting Portal, Ministry of Home Affairs, Government of India.**  
   Used as the reference model for cybercrime complaint reporting workflows and citizen-facing reporting concepts.  
   [https://cybercrime.gov.in](https://cybercrime.gov.in)

2. **Indian Cyber Crime Coordination Centre, Ministry of Home Affairs, Government of India.**  
   Used as contextual reference for NCRP, cybercrime reporting infrastructure, and cyber fraud reporting mechanisms.  
   [https://i4c.mha.gov.in](https://i4c.mha.gov.in)

3. **Reserve Bank of India. (2025). Annual Report 2024–25: Currency Management.**  
   Used as an official reference for currency-management context and counterfeit-currency discussion.  
   [https://www.rbi.org.in](https://www.rbi.org.in)

4. **Indian Computer Emergency Response Team, Ministry of Electronics and Information Technology, Government of India.**  
   Used as an official cybersecurity reference for cyber incident response, advisories, and national cyber threat context.  
   [https://www.cert-in.org.in](https://www.cert-in.org.in)

5. **National Crime Records Bureau, Ministry of Home Affairs, Government of India.**  
   Used as an official reference for crime data, cybercrime reporting context, and law-enforcement data systems.  
   [https://ncrb.gov.in](https://ncrb.gov.in)

6. **Google. Gemini API Documentation.**  
   Used for LLM-based reasoning fallback and explanation support.  
   [https://ai.google.dev/gemini-api/docs](https://ai.google.dev/gemini-api/docs)

7. **OpenCV Foundation. OpenCV Image Processing Documentation.**  
   Used for image processing, feature extraction, thresholding, contour analysis, and counterfeit-note visual checks.  
   [https://docs.opencv.org](https://docs.opencv.org/)

8. **NetworkX Developers. NetworkX Documentation.**  
   Used for graph construction, connected components, fraud-ring mapping, and transaction-network analysis.  
   [https://networkx.org/documentation/stable/](https://networkx.org/en/)

> **Note:** The prototype models are evaluated using carefully generated synthetic and simulated datasets due to the limited availability of publicly accessible digital arrest scam, telecom, banking, and counterfeit currency incident datasets. The system is designed as a decision-support prototype and not as a legally certified enforcement system.
