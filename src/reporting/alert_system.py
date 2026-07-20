import time
import random
from typing import Dict, Any
from src.utils.logger import setup_logger

logger = setup_logger("AlertSystem")

class RealtimeAlertSystem:
    """
    Simulated Real-Time Alert Engine that triggers warnings to Telecom providers,
    MHA portals, and citizen devices, calculating lead times before financial damage occurs.
    """
    
    def dispatch_scam_alert(self, call_id: str, caller_number: str, text_snippet: str) -> Dict[str, Any]:
        """
        Dispatches warnings to multiple channels and logs estimated lead times.
        """
        logger.info(f"🚨 SCAM ALERT TRIGGERED for Call ID {call_id} (Caller: {caller_number})")
        
        # Simulate millisecond latencies
        ingestion_time_sec = float(np_random_uniform(0.1, 0.4))
        classification_time_sec = float(np_random_uniform(0.2, 0.5))
        dispatch_delay_sec = float(np_random_uniform(0.05, 0.15))
        
        total_reaction_time = ingestion_time_sec + classification_time_sec + dispatch_delay_sec
        
        # In a real digital arrest scam, the average psychological build-up takes 15-30 minutes 
        # before the fraudster mentions bank transfers. 
        # By detecting the threat in under 1 minute, we gain a massive "Lead Time Gained".
        lead_time_minutes_gained = float(np_random_uniform(15.0, 45.0)) 
        
        # Estimate damage prevented (average transaction value in our complaints is ~3 Lakhs)
        estimated_savings = float(random.choice([150000.0, 250000.0, 450000.0, 1200000.0]))
        
        alerts = {
            "telecom_operator": {
                "action": "BLOCK_NUMBER_AND_IMMEDIATE_CELL_TOWER_TRACE",
                "target_number": caller_number,
                "status": "DISPATCHED_TO_OPERATOR_CIRCLE"
            },
            "citizen_device": {
                "action": "DISPLAY_CRITICAL_FULLSCREEN_ALERT_ALERT",
                "message": "🚨 WARNING: This caller is impersonating a police/CBI officer. Disconnect immediately!",
                "status": "PUSHED"
            },
            "mha_national_portal": {
                "action": "AUTO_LOG_NCRB_DRAFT",
                "priority": "P1_DIGITAL_ARREST",
                "status": "QUEUED"
            }
        }
        
        return {
            "incident_call_id": call_id,
            "caller_number": caller_number,
            "reaction_latency_seconds": round(total_reaction_time, 3),
            "lead_time_minutes_preventive": round(lead_time_minutes_gained, 1),
            "estimated_loss_prevented_inr": estimated_savings,
            "dispatched_alerts": alerts,
            "timestamp": pd_now_str()
        }

def np_random_uniform(low, high):
    import numpy as np
    return np.random.uniform(low, high)

def pd_now_str():
    import pandas as pd
    return pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
