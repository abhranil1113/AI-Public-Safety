import os
import pandas as pd
from typing import Dict, Any
from src.cv.currency_detector import CurrencyDetector
from src.utils.constants import CURRENCY_DATA_DIR
from src.utils.logger import setup_logger

logger = setup_logger("CurrencyAgent")

class CurrencyAgent:
    def __init__(self):
        self.detector = CurrencyDetector()
        
    def check_bill(self, image_path: str) -> Dict[str, Any]:
        """Perform computer vision verification on a single note image."""
        logger.info(f"Forensic note check: {image_path}")
        return self.detector.detect(image_path)
        
    def batch_process_currency(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze a batch of note images described in the metadata."""
        if df.empty:
            return {"total_scanned": 0, "fakes_detected": 0, "fake_ratio": 0.0}
            
        logger.info(f"Batch auditing {len(df)} notes.")
        fakes = 0
        
        for idx, row in df.iterrows():
            img_rel = row["image_path"]
            full_img_path = os.path.join(CURRENCY_DATA_DIR, img_rel.replace("/", os.sep))
            
            res = self.detector.detect(full_img_path)
            if res.get("alert_triggered", False):
                fakes += 1
                
        return {
            "total_scanned": len(df),
            "fakes_detected": fakes,
            "fake_ratio": (fakes / len(df)) * 100.0
        }
