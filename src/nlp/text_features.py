import re
from typing import Dict, Any, List
from src.utils.constants import SCAM_KEYWORDS

def preprocess_text(text: str) -> str:
    """Basic text cleanup."""
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

def extract_explainable_factors(text: str) -> Dict[str, Any]:
    """
    Examine call transcript to check for specific coercion and scam indicators.
    Returns boolean flags for explainability and legal evidence tracking.
    """
    clean_text = preprocess_text(text)
    
    # 1. Authority Claim
    authority_words = ["cbi", "officer", "customs", "enforcement", "police", "trai", "government"]
    authority_detected = any(re.search(r'\b' + w + r'\b', clean_text) for w in authority_words)
    
    # 2. Psychological Pressure / Threat
    pressure_words = ["arrest", "illegal", "drug", "trafficking", "seized", "laundering", "prison", "block"]
    pressure_detected = any(re.search(r'\b' + w + r'\b', clean_text) for w in pressure_words)
    
    # 3. Isolation Instructions
    isolation_words = ["skype", "zoom", "camera", "stay in room", "do not disconnect", "secret", "video call"]
    isolation_detected = any(re.search(r'\b' + w + r'\b', clean_text) for w in isolation_words) or \
                         ("camera" in clean_text and "on" in clean_text) or \
                         ("disconnect" in clean_text and "not" in clean_text)
                         
    # 4. Payment Request / Financial
    payment_words = ["transfer", "money", "account", "rupees", "lakh", "crore", "processing", "fee", "verify"]
    payment_detected = any(re.search(r'\b' + w + r'\b', clean_text) for w in payment_words)
    
    # 5. Spoofed / Caller details (heuristics based on numbers in text)
    digits = re.findall(r"\d+", clean_text)
    spoof_detected = len(digits) > 2  # multiple tracking numbers or phone details
    
    factors = {
        "fake_authority": authority_detected,
        "psychological_pressure": pressure_detected,
        "isolation_instructions": isolation_detected,
        "payment_request": payment_detected,
        "spoofed_details": spoof_detected
    }
    
    return factors

def detect_scam_stage(factors: Dict[str, bool]) -> Dict[str, str]:
    """
    Map threat factors to the sequential stages of a Digital Arrest scam,
    predicting the next logical stage to assist in proactive intervention.
    """
    # Progression: Greeting -> Authority Claim -> Fear Creation -> Isolation -> Payment Demand -> Completed Scam
    
    if factors["payment_request"]:
        current_stage = "Payment Demand"
        next_stage = "Completed Scam (Financial Loss)"
    elif factors["isolation_instructions"]:
        current_stage = "Isolation (Psychological Hostage)"
        next_stage = "Payment Demand"
    elif factors["psychological_pressure"]:
        current_stage = "Fear Creation (Threats)"
        next_stage = "Isolation (Psychological Hostage)"
    elif factors["fake_authority"]:
        current_stage = "Authority Claim (Impersonation)"
        next_stage = "Fear Creation (Threats)"
    else:
        current_stage = "Greeting / Setup"
        next_stage = "Authority Claim (Impersonation)"
        
    return {
        "current_stage": current_stage,
        "next_likely_stage": next_stage
    }
