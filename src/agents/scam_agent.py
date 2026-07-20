import pandas as pd
from typing import Dict, Any
from src.nlp.scam_classifier import ScamClassifier
from src.nlp.speech_detector import SpeechAIVoiceDetector
from src.reporting.alert_system import RealtimeAlertSystem
from src.utils.logger import setup_logger

logger = setup_logger("ScamAgent")

class ScamAgent:
    def __init__(self):
        self.classifier = ScamClassifier()
        self.speech_detector = SpeechAIVoiceDetector()
        self.alert_system = RealtimeAlertSystem()
        
    def analyze_transcript(self, text: str, mode: str = "ml") -> Dict[str, Any]:
        """Verify if a single transcript represents a digital arrest scam."""
        logger.info("Analyzing transcript for digital arrest signature...")
        return self.classifier.evaluate_call(text, mode=mode)
        
    def analyze_voice_clip(self, file_path: str) -> Dict[str, Any]:
        """Analyze a mock voice clip path for deepfake / cloned voice signatures."""
        logger.info("Auditing audio sample for voice cloning patterns...")
        return self.speech_detector.analyze_audio_file(file_path)
        
    def trigger_incident_alerts(self, call_id: str, caller_number: str, text_snippet: str) -> Dict[str, Any]:
        """Simulate real-time warnings to telecom carriers and MHA when scam is detected."""
        return self.alert_system.dispatch_scam_alert(call_id, caller_number, text_snippet)
        
    def batch_process_calls(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Compute statistics and flag scams over a batch of calls, including alert simulation."""
        if df.empty:
            return {
                "total_scanned": 0, 
                "scams_detected": 0, 
                "trigger_rate": 0.0,
                "total_alert_latencies_sum": 0.0,
                "total_lead_time_minutes_prevented": 0.0,
                "total_savings_inr": 0.0
            }
            
        logger.info(f"Batch processing {len(df)} call logs.")
        scam_count = 0
        predictions = []
        
        total_latencies = 0.0
        total_lead_time = 0.0
        total_savings = 0.0
        dispatched_alerts_count = 0
        
        for idx, row in df.iterrows():
            res = self.classifier.evaluate_call(row["transcription"], mode="ml")
            predictions.append(res["prediction"])
            
            if res["alert_triggered"]:
                scam_count += 1
                
                # Simulate real-time alerts
                caller_num = f"+91 {random_num()}"
                alert_res = self.trigger_incident_alerts(row["call_id"], caller_num, row["transcription"])
                
                total_latencies += alert_res["reaction_latency_seconds"]
                total_lead_time += alert_res["lead_time_minutes_preventive"]
                total_savings += alert_res["estimated_loss_prevented_inr"]
                dispatched_alerts_count += 1
                
        df["detected_label"] = predictions
        
        return {
            "total_scanned": len(df),
            "scams_detected": scam_count,
            "trigger_rate": (scam_count / len(df)) * 100.0,
            "avg_reaction_latency_seconds": round(total_latencies / max(1, dispatched_alerts_count), 3),
            "total_lead_time_minutes_prevented": round(total_lead_time, 1),
            "total_savings_inr": total_savings,
            "alerts_dispatched": dispatched_alerts_count,
            "processed_df": df
        }

def random_num():
    import random
    return f"{random.randint(70000, 99999)} {random.randint(10000, 99999)}"
