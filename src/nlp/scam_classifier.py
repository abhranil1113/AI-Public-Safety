import os
import joblib
from typing import Dict, Any, Tuple, List
import google.generativeai as genai

from src.utils.constants import SCAM_CLASSIFIER_PATH, SCAM_VECTORIZER_PATH
from src.utils.config import GEMINI_API_KEY
from src.nlp.text_features import preprocess_text, extract_explainable_factors, detect_scam_stage
from src.utils.logger import setup_logger

logger = setup_logger("ScamClassifier")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

class ScamClassifier:
    def __init__(self):
        self.model = None
        self.vectorizer = None
        self.load_model()

    def load_model(self):
        """Loads TF-IDF vectorizer and Logistic Regression model if they exist."""
        if os.path.exists(SCAM_CLASSIFIER_PATH) and os.path.exists(SCAM_VECTORIZER_PATH):
            try:
                self.model = joblib.load(SCAM_CLASSIFIER_PATH)
                self.vectorizer = joblib.load(SCAM_VECTORIZER_PATH)
                logger.info("Successfully loaded ML scam classification models.")
            except Exception as e:
                logger.warning(f"Failed to load ML models: {e}. Falling back to rule-based classification.")
        else:
            logger.info("ML scam classification models not found. Running in rule-based fallback mode.")

    def predict_rule_based(self, text: str) -> Tuple[str, float]:
        """Classify scam status based on explainability features."""
        factors = extract_explainable_factors(text)
        triggered_count = sum(1 for v in factors.values() if v)
        
        if triggered_count >= 2:
            confidence = min(0.5 + (triggered_count * 0.1), 0.95)
            return "scam", confidence
        else:
            confidence = max(0.95 - (triggered_count * 0.15), 0.5)
            return "normal", confidence

    def predict_ml(self, text: str) -> Tuple[str, float]:
        """Classify scam status using the trained TF-IDF Logistic Regression model."""
        if not self.model or not self.vectorizer:
            return self.predict_rule_based(text)
            
        clean_text = preprocess_text(text)
        features_vec = self.vectorizer.transform([clean_text])
        prediction = self.model.predict(features_vec)[0]
        probabilities = self.model.predict_proba(features_vec)[0]
        
        label = "scam" if prediction == 1 else "normal"
        confidence = probabilities[prediction]
        
        return label, float(confidence)

    def predict_llm(self, text: str) -> Tuple[str, float, str]:
        """Classify scam status using Google Gemini LLM API for advanced reasoning."""
        if not GEMINI_API_KEY:
            logger.warning("Gemini API key is not configured. Falling back to ML/Rule-based prediction.")
            label, confidence = self.predict_ml(text)
            return label, confidence, "Local ML/Rule-based prediction (Gemini key missing)."
            
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            
            prompt = f"""
            Analyze the following phone call transcript and determine if it represents a digital arrest scam or general financial fraud.
            
            Respond strictly in the following JSON format:
            {{
              "is_scam": boolean,
              "confidence": float (between 0.0 and 1.0),
              "reasoning": "brief explanation of why this call is or is not flagged as a scam"
            }}

            Call Transcript:
            \"\"\"{text}\"\"\"
            """
            
            response = model.generate_content(
                prompt,
                generation_config={"response_mime_type": "application/json"}
            )
            
            import json
            data = json.loads(response.text.strip())
            
            label = "scam" if data.get("is_scam", False) else "normal"
            confidence = float(data.get("confidence", 0.5))
            reasoning = data.get("reasoning", "No reasoning provided.")
            
            return label, confidence, reasoning
        except Exception as e:
            logger.error(f"Gemini API invocation failed: {e}")
            label, confidence = self.predict_ml(text)
            return label, confidence, f"Fallback to local prediction due to LLM error: {e}"

    def evaluate_call(self, text: str, mode: str = "ml") -> Dict[str, Any]:
        """
        Evaluate a call transcript and provide detailed explainability features,
        threat stages, and audit details.
        """
        factors = extract_explainable_factors(text)
        stage_info = detect_scam_stage(factors)
        
        if mode == "rule":
            label, confidence = self.predict_rule_based(text)
            reasoning = "Evaluated via heuristic explainable factor rules."
        elif mode == "llm":
            label, confidence, reasoning = self.predict_llm(text)
        else:
            label, confidence = self.predict_ml(text)
            reasoning = "Evaluated via ML TF-IDF Logistic Regression classifier."
            
        # Ensure consistency (if ML says normal but explainable flags are highly suspicious, adjust confidence)
        if label == "normal" and factors["fake_authority"] and factors["psychological_pressure"]:
            # Borderline case trigger: flag as borderline warning
            label = "scam"
            confidence = 0.55
            reasoning += " (Borderline override: detected multiple critical coercion indicators)."
            
        # Format explainability indicators list for presentation / CLI
        explainable_list = []
        if factors["fake_authority"]: explainable_list.append("Fake authority impersonation detected")
        if factors["psychological_pressure"]: explainable_list.append("Psychological pressure/coercion language")
        if factors["isolation_instructions"]: explainable_list.append("Isolation/Video call monitoring instruction")
        if factors["payment_request"]: explainable_list.append("Immediate bank/payment transfer request")
        if factors["spoofed_details"]: explainable_list.append("Spoofed account/number coordinates mentioned")
        
        return {
            "transcript_preview": text[:100] + "..." if len(text) > 100 else text,
            "prediction": label,
            "confidence": round(confidence, 4),
            "reasoning": reasoning,
            "explainability_factors": factors,
            "explainable_indicators": explainable_list,
            "threat_stage": stage_info["current_stage"],
            "predicted_next_stage": stage_info["next_likely_stage"],
            "alert_triggered": label == "scam"
        }
