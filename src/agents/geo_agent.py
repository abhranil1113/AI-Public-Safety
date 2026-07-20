from typing import List, Dict, Any
import pandas as pd
from src.geo.hotspot_detector import HotspotDetector
from src.geo.map_generator import generate_crime_map
from src.utils.logger import setup_logger

logger = setup_logger("GeoAgent")

class GeoAgent:
    def __init__(self):
        self.detector = HotspotDetector()
        
    def get_district_hotspots(self) -> pd.DataFrame:
        """Run geospatial clustering to locate hot zones."""
        logger.info("Computing geospatial crime hotspot metrics...")
        return self.detector.analyze_hotspots()
        
    def get_patrol_priorities(self) -> List[Dict[str, Any]]:
        """Compute actionable patrols order."""
        logger.info("Generating patrol deployment prioritization matrix...")
        return self.detector.get_patrol_recommendations()
        
    def render_map(self) -> str:
        """Create the dark-theme HTML map in outputs/maps/ folder."""
        logger.info("Rendering interactive leaflet HTML map...")
        return generate_crime_map(self.detector)
