import pytest
from src.nlp.scam_classifier import ScamClassifier

def test_scam_classifier_initialization():
    classifier = ScamClassifier()
    assert classifier is not None

def test_rule_based_scam_detection():
    classifier = ScamClassifier()
    
    # Scam input
    scam_text = "I am from CBI. You are under digital arrest. Transfer money immediately to a secure account."
    label, confidence = classifier.predict_rule_based(scam_text)
    assert label == "scam"
    assert confidence > 0.5
    
    # Normal input
    normal_text = "Hi mom, I will be home by 7 PM for dinner."
    label, confidence = classifier.predict_rule_based(normal_text)
    assert label == "normal"

def test_evaluate_call():
    classifier = ScamClassifier()
    scam_text = "Enforcement Directorate calling regarding money laundering from your account. Connect on Skype."
    res = classifier.evaluate_call(scam_text, mode="rule")
    
    assert res["prediction"] == "scam"
    assert res["alert_triggered"] is True
    assert "reasoning" in res
