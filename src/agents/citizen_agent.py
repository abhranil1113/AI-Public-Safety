import os
import json
from typing import Dict, Any
from src.nlp.scam_classifier import ScamClassifier
from src.utils.logger import setup_logger

logger = setup_logger("CitizenAgent")

# Simple regional language translations for the public safety advisory
LANGUAGES_ADVISORY = {
    "English": {
        "verdict_scam": "⚠️ HIGH RISK ALERT: This matches typical patterns of digital arrest scams and financial fraud.",
        "verdict_normal": "✅ LOW RISK: This text does not appear to contain immediate fraud indicators.",
        "advisory": "1. Do NOT transfer any money.\n2. Do NOT share OTP, Aadhaar, or Bank credentials.\n3. Disconnect any active Skype, Zoom or WhatsApp video calls immediately.\n4. Call 1930 (National Cyber Crime Helpline) or report to www.cybercrime.gov.in."
    },
    "Hindi": {
        "verdict_scam": "⚠️ उच्च जोखिम चेतावनी: यह संदेश डिजिटल अरेस्ट स्कैम और वित्तीय धोखाधड़ी के पैटर्न से मेल खाता है।",
        "verdict_normal": "✅ कम जोखिम: इस संदेश में कोई तत्काल धोखाधड़ी के संकेत नहीं मिले हैं।",
        "advisory": "1. कोई भी पैसा ट्रांसफर न करें।\n2. ओटीपी, आधार या बैंक विवरण साझा न करें।\n3. स्काइप, ज़ूम या व्हाट्सएप वीडियो कॉल को तुरंत काट दें।\n4. राष्ट्रीय साइबर अपराध हेल्पलाइन 1930 पर कॉल करें या www.cybercrime.gov.in पर रिपोर्ट करें।"
    },
    "Telugu": {
        "verdict_scam": "⚠️ అధిక ప్రమాద హెచ్చరిక: ఇది డిజిటల్ అరెస్ట్ స్కామ్ మరియు ఆర్థిక మోసాల నమూనాలతో సరిపోలుతోంది.",
        "verdict_normal": "✅ తక్కువ ప్రమాదం: ఈ వచనంలో ఎలాంటి మోసపూరిత సంకేతాలు కనిపించడం లేదు.",
        "advisory": "1. ఎలాంటి డబ్బును బదిలీ చేయవద్దు.\n2. OTP, ఆధార్ లేదా బ్యాంక్ వివరాలను ఎవరితోనూ పంచుకోవద్దు.\n3. స్కైప్, జూమ్ లేదా వాట్సాప్ వీడియో కాల్స్ వెంటనే నిలిపివేయండి.\n4. నేషనల్ సైబర్ క్రైమ్ హెల్ప్‌లైన్ 1930 కి కాల్ చేయండి లేదా www.cybercrime.gov.in లో ఫిర్యాదు చేయండి."
    },
    "Tamil": {
        "verdict_scam": "⚠️ அதிக ஆபத்து எச்சரிக்கை: இது வழக்கமான டிஜிட்டல் கைது மோசடி மற்றும் நிதி மோசடி வடிவங்களுடன் ஒத்துப்போகிறது.",
        "verdict_normal": "✅ குறைந்த ஆபத்து: இந்த செய்தியில் மோசடி அறிகுறிகள் எதுவும் உடனடியாக தென்படவில்லை.",
        "advisory": "1. எந்தப் பணத்தையும் அனுப்ப வேண்டாம்.\n2. OTP, ஆதார் அல்லது வங்கி விவரங்களைப் பகிர வேண்டாம்.\n3. ஸ்கைப், ஜூம் அல்லது வாட்ஸ்அப் வீடியோ அழைப்புகளை உடனே துண்டிக்கவும்.\n4. தேசிய சைபர் குற்ற உதவி எண் 1930 ஐ அழைக்கவும் அல்லது www.cybercrime.gov.in இல் புகார் செய்யவும்."
    }
}

class CitizenFraudShieldAgent:
    def __init__(self):
        self.classifier = ScamClassifier()

    def run_assessment(self, input_text: str, preferred_language: str = "English") -> Dict[str, Any]:
        """
        Evaluate suspicious call text/message, returning risk levels, advisories in multiple languages,
        and generating NCRB registration packets.
        """
        logger.info(f"Citizen Fraud Shield assessing query in {preferred_language}...")
        
        # Classify the input
        res = self.classifier.evaluate_call(input_text, mode="ml")
        prediction = res["prediction"]
        confidence = res["confidence"]
        is_scam = res["alert_triggered"]
        
        # Fetch appropriate advisory
        lang = preferred_language if preferred_language in LANGUAGES_ADVISORY else "English"
        advisory_data = LANGUAGES_ADVISORY[lang]
        
        verdict = advisory_data["verdict_scam"] if is_scam else advisory_data["verdict_normal"]
        steps = advisory_data["advisory"]
        
        # Simulate NCRP (National Cyber Crime Reporting Portal) auto-filled packet
        ncrp_packet = {}
        if is_scam:
            ncrp_packet = {
                "portal": "NCRP (National Cyber Crime Reporting Portal)",
                "auto_form_data": {
                    "incident_category": "Online Financial Fraud / Digital Arrest",
                    "evidence_transcript_snippet": input_text[:150],
                    "reported_timestamp": pd_now_str(),
                    "recommended_action": "Freeze target account, notify Telecom Circle",
                    "source_channel": "Citizen Mobile Application/WhatsApp Shield"
                },
                "api_endpoint": "https://api.cybercrime.gov.in/v1/report_draft",
                "status": "DRAFT_READY_FOR_CITIZEN_SUBMISSION"
            }

        return {
            "query_text": input_text,
            "risk_assessment": "HIGH" if is_scam else "LOW",
            "confidence_score": confidence,
            "language_selected": lang,
            "verdict_advisory": verdict,
            "guided_steps": steps,
            "ncrp_handoff_packet": ncrp_packet
        }

def pd_now_str():
    import pandas as pd
    return pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
