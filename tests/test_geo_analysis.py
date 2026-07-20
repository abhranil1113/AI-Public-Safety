import pytest
import pandas as pd
from src.geo.hotspot_detector import HotspotDetector
from src.geo.map_generator import generate_crime_map

def test_hotspot_detector():
    detector = HotspotDetector()
    df = detector.analyze_hotspots()
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "calculated_hotspot_score" in df.columns
    assert "latitude" in df.columns
    assert "longitude" in df.columns

def test_patrol_recommendations():
    detector = HotspotDetector()
    recs = detector.get_patrol_recommendations()
    
    assert isinstance(recs, list)
    assert len(recs) > 0
    assert "district" in recs[0]
    assert "priority_level" in recs[0]
    assert "hotspot_score" in recs[0]

def test_map_generation(tmp_path):
    detector = HotspotDetector()
    filename = "test_map.html"
    out_dir = str(tmp_path)
    
    # Run mapping
    import src.geo.map_generator
    # Monkeypatch the output directory temporarily to tmp_path
    original_out = src.geo.map_generator.MAPS_OUT_DIR
    src.geo.map_generator.MAPS_OUT_DIR = out_dir
    
    try:
        path = generate_crime_map(detector, filename=filename)
        assert os.path.exists(path)
        assert path.endswith(".html")
    finally:
        src.geo.map_generator.MAPS_OUT_DIR = original_out
import os
