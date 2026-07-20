import os
import folium
import pandas as pd
from src.geo.hotspot_detector import HotspotDetector
from src.utils.constants import MAPS_OUT_DIR
from src.utils.logger import setup_logger

logger = setup_logger("MapGenerator")

def generate_crime_map(detector: HotspotDetector, filename="hotspot_map.html") -> str:
    """Generate an interactive Folium map showing crime hotspots."""
    df = detector.analyze_hotspots()
    if df.empty:
        logger.error("Hotspot dataframe is empty. Cannot generate map.")
        return ""
        
    # Center map in India (lat: 20.5937, lon: 78.9629)
    india_map = folium.Map(
        location=[20.5937, 78.9629],
        zoom_start=5,
        tiles="CartoDB dark_matter" # Sleek dark-mode aesthetic
    )
    
    for idx, row in df.iterrows():
        lat = row["latitude"]
        lon = row["longitude"]
        name = row["district_name"]
        score = row["calculated_hotspot_score"]
        count = int(row["complaint_count"])
        loss = float(row["total_loss"])
        
        # Color based on calculated hotspot score
        if score > 75:
            color = "#FF003C" # Bright Crimson Red
            radius = 18
        elif score > 50:
            color = "#FF8A00" # Orange
            radius = 14
        elif score > 25:
            color = "#FFD369" # Yellow
            radius = 10
        else:
            color = "#00ADB5" # Teal/Blue
            radius = 7
            
        # Create tooltip html with custom premium dark-themed styling
        popup_html = f"""
        <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 220px; color: #EAEAEA; background-color: #1A1A2E; padding: 10px; border-radius: 8px; border: 1px solid {color};">
            <h4 style="margin: 0 0 8px 0; color: #FFF; font-size: 14px; border-bottom: 1px solid #444; padding-bottom: 4px;">{name} District</h4>
            <table style="width: 100%; font-size: 12px; border-collapse: collapse;">
                <tr>
                    <td style="padding: 2px 0; color: #888;">Hotspot Index:</td>
                    <td style="text-align: right; font-weight: bold; color: {color};">{score}%</td>
                </tr>
                <tr>
                    <td style="padding: 2px 0; color: #888;">Scam Complaints:</td>
                    <td style="text-align: right; font-weight: bold;">{count}</td>
                </tr>
                <tr>
                    <td style="padding: 2px 0; color: #888;">Financial Defraud:</td>
                    <td style="text-align: right; font-weight: bold; color: #28DF99;">₹{loss:,.2f}</td>
                </tr>
            </table>
        </div>
        """
        
        # Add marker to map
        folium.CircleMarker(
            location=[lat, lon],
            radius=radius,
            popup=folium.Popup(popup_html, max_width=250),
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.6,
            weight=1.5
        ).add_to(india_map)
        
    os.makedirs(MAPS_OUT_DIR, exist_ok=True)
    out_path = os.path.join(MAPS_OUT_DIR, filename)
    india_map.save(out_path)
    logger.info(f"Geospatial HTML map saved to {out_path}")
    return out_path
