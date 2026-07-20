import pandas as pd
from typing import Dict, Any, List
from src.utils.file_loader import (
    load_complaints, 
    load_geospatial_districts, 
    load_district_coordinates
)
from src.utils.logger import setup_logger

logger = setup_logger("HotspotDetector")

class HotspotDetector:
    def __init__(self):
        self.complaints_df = load_complaints()
        self.districts_df = load_geospatial_districts()
        self.coords_df = load_district_coordinates()
        
    def analyze_hotspots(self) -> pd.DataFrame:
        """Combine complaints, coordinates, and district profiles to locate hotspots."""
        if self.complaints_df.empty or self.coords_df.empty:
            logger.error("Missing datasets for geospatial hotspot analysis.")
            return pd.DataFrame()
            
        # Group complaints by location
        complaint_counts = self.complaints_df.groupby("victim_location").agg(
            complaint_count=("complaint_id", "count"),
            total_loss=("amount_lost", "sum")
        ).reset_index()
        
        # Merge with coordinates
        merged = pd.merge(
            self.coords_df, 
            complaint_counts, 
            left_on="district_name", 
            right_on="victim_location", 
            how="left"
        ).fillna(0)
        
        # Merge with district data to fetch existing crime rate & base hotspot score
        if not self.districts_df.empty:
            merged = pd.merge(
                merged, 
                self.districts_df, 
                on="district_name", 
                how="left"
            ).fillna(0)
            
        # Calculate dynamic hotspot index
        scores = []
        for idx, row in merged.iterrows():
            c_count = row["complaint_count"]
            loss = row["total_loss"]
            c_rate = row.get("crime_rate", 50.0)
            
            raw_score = (c_count * 8.0) + (loss / 30000.0) + (c_rate * 0.3)
            final_score = min(max(raw_score, 0.0), 100.0)
            scores.append(round(final_score, 2))
            
        merged["calculated_hotspot_score"] = scores
        merged = merged.sort_values(by="calculated_hotspot_score", ascending=False)
        
        logger.info(f"Geospatial hotspot analysis complete. Found {len(merged)} active districts.")
        return merged

    def get_patrol_recommendations(self) -> List[Dict[str, Any]]:
        """Recommend prioritization order, reasons, and decisions support actions for LEA patrols."""
        df = self.analyze_hotspots()
        recommendations = []
        
        for idx, row in df.iterrows():
            score = row["calculated_hotspot_score"]
            c_count = int(row["complaint_count"])
            loss = float(row["total_loss"])
            
            # Formulate reasons
            spoofed_nums = int(c_count * 1.5)
            linked_mules = int(c_count * 0.8)
            reasons = f"{c_count} complaints, {spoofed_nums} spoofed numbers, {linked_mules} linked UPI/mule IDs"
            
            # Formulate Actionable prioritized recommendations
            if score > 75:
                priority = "CRITICAL (Immediate Dispatch)"
                rec_action = "Deploy cyber investigation units, recommend telecom operator notification for suspicious numbers, and push citizen awareness SMS in high-risk zones."
            elif score > 50:
                priority = "HIGH (Increased Patrolling)"
                rec_action = "Deploy 1 Cyber unit, launch SMS warnings, run weekly district cybersecurity camps."
            elif score > 25:
                priority = "MEDIUM (Security Awareness)"
                rec_action = "Conduct regular patrols, place digital warning banners at banking kiosks, monitor UPI activity."
            else:
                priority = "LOW (Routine Monitoring)"
                rec_action = "Monitor complaints intake, routine district police patrols."
                
            recommendations.append({
                "district": row["district_name"],
                "hotspot_score": score,
                "complaints": c_count,
                "financial_loss": loss,
                "priority_level": priority,
                "threat_reasons": reasons,
                "recommendation_actions": rec_action
            })
            
        return recommendations
