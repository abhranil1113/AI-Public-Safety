import os
import joblib
import pandas as pd
from typing import Dict, Any, Tuple

from src.utils.constants import CURRENCY_MODEL_PATH
from src.cv.image_features import extract_note_features
from src.utils.logger import setup_logger

logger = setup_logger("CurrencyDetector")

class CurrencyDetector:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        """Load Random Forest classifier from models directory."""
        if os.path.exists(CURRENCY_MODEL_PATH):
            try:
                self.model = joblib.load(CURRENCY_MODEL_PATH)
                logger.info("Successfully loaded CV currency model.")
            except Exception as e:
                logger.warning(f"Failed to load CV model: {e}. Falling back to rule-based verification.")
        else:
            logger.info("CV model not found. Running in rule-based fallback mode.")

    def predict_rule_based(self, features: Dict[str, Any]) -> Tuple[str, float]:
        """Fall back to basic heuristics if the ML model isn't trained yet."""
        thread_ok = features["security_thread"] == "PASS"
        sharpness_ok = features["watermark_microprint"] == "PASS"
        
        if thread_ok and sharpness_ok:
            confidence = min(0.6 + (features["thread_continuity"] * 0.2) + (features["sharpness_score"] / 2000.0), 0.98)
            return "real", confidence
        else:
            confidence = 0.85
            return "fake", confidence

    def detect(self, image_path: str) -> Dict[str, Any]:
        """Detect whether a note is real or fake, providing a full security checksheet."""
        try:
            # Features now contain check flags (security_thread, watermark_microprint, uv_fluorescence, serial_number_pattern)
            features = extract_note_features(image_path)
        except Exception as e:
            logger.error(f"Failed to extract features from image {image_path}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
            
        # Extract features vector for model evaluation
        feats_model = {k: v for k, v in features.items() if not isinstance(v, str)}
        
        if self.model:
            df_feat = pd.DataFrame([feats_model])
            prediction = self.model.predict(df_feat)[0]
            probabilities = self.model.predict_proba(df_feat)[0]
            
            label = "fake" if prediction == 1 else "real"
            confidence = float(probabilities[prediction])
            method = "Random Forest CV Model"
        else:
            label, confidence = self.predict_rule_based(features)
            method = "Rule-based security thread & sharpness heuristics"
            
        # Ensure consistency: if multiple check flags fail, force suspect alert
        failed_checks = sum(1 for k in ["security_thread", "watermark_microprint", "uv_fluorescence", "serial_number_pattern"] if features[k] == "FAIL")
        
        if failed_checks >= 2 and label == "real":
            label = "fake"
            confidence = 0.75
            method += " (Rule Override: Multiple security checkpoints failed)"
            
        counterfeit_prob = confidence if label == "fake" else (1.0 - confidence)
        
        return {
            "success": True,
            "prediction": label,
            "confidence": round(confidence, 4),
            "counterfeit_probability": round(counterfeit_prob, 4),
            "checksheet": {
                "security_thread": features["security_thread"],
                "watermark_microprint": features["watermark_microprint"],
                "uv_fluorescence": features["uv_fluorescence"],
                "serial_number_pattern": features["serial_number_pattern"]
            },
            "features_extracted": feats_model,
            "method": method,
            "alert_triggered": label == "fake"
        }
DefinitionError = Exception
