import os
import pytest
import numpy as np
import cv2
from src.cv.image_features import extract_note_features
from src.cv.currency_detector import CurrencyDetector

@pytest.fixture
def temp_note_images(tmp_path):
    # Create temporary clean images for testing feature extraction logic precisely
    real_path = os.path.join(tmp_path, "real_500.png")
    fake_path = os.path.join(tmp_path, "fake_500.png")
    
    # Real note image
    img_real = np.zeros((120, 250, 3), dtype=np.uint8)
    img_real[:] = [180, 180, 180] # Neutral background
    cv2.line(img_real, (180, 0), (180, 120), (0, 200, 0), 3) # Pure green continuous thread
    cv2.putText(img_real, "RBI RBI RBI", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (50, 50, 50), 1)
    cv2.imwrite(real_path, img_real)
    
    # Fake note image (no green thread, smudged print)
    img_fake = np.zeros((120, 250, 3), dtype=np.uint8)
    img_fake[:] = [180, 180, 180]
    # No line drawn (continuity will be 0)
    cv2.putText(img_fake, "R8I R8I R8I", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (80, 80, 80), 1)
    cv2.imwrite(fake_path, img_fake)
    
    return str(real_path), str(fake_path)

def test_feature_extraction(temp_note_images):
    real_img, fake_img = temp_note_images
    
    # Extract real features
    real_feats = extract_note_features(real_img)
    assert real_feats["thread_continuity"] == 1.0
    assert real_feats["thread_pixel_count"] > 0
    assert real_feats["security_thread"] == "PASS"
    
    # Extract fake features
    fake_feats = extract_note_features(fake_img)
    assert fake_feats["thread_continuity"] == 0.0
    assert fake_feats["security_thread"] == "FAIL"

def test_currency_detector(temp_note_images):
    real_img, fake_img = temp_note_images
    detector = CurrencyDetector()
    
    # Verify real note prediction
    res_real = detector.detect(real_img)
    assert res_real["success"] is True
    # Real image in test will trigger real note label
    assert res_real["prediction"] == "real"
    assert res_real["alert_triggered"] is False
    
    # Verify fake note prediction
    res_fake = detector.detect(fake_img)
    assert res_fake["success"] is True
    assert res_fake["prediction"] == "fake"
    assert res_fake["alert_triggered"] is True
