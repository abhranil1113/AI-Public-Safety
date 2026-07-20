import os

# Project Root and Paths
PROJECT_ROOT = r"D:\Ai Public Safety"
DATASETS_DIR = os.path.join(PROJECT_ROOT, "datasets")
MODELS_DIR = os.path.join(PROJECT_ROOT, "models")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")
OUTPUTS_DIR = os.path.join(PROJECT_ROOT, "outputs")
LOGS_DIR = os.path.join(PROJECT_ROOT, "logs")

# Subdirectories
SCAM_DATA_DIR = os.path.join(DATASETS_DIR, "scam_text")
CURRENCY_DATA_DIR = os.path.join(DATASETS_DIR, "currency")
TRANSACTIONS_DATA_DIR = os.path.join(DATASETS_DIR, "transactions")
COMPLAINTS_DATA_DIR = os.path.join(DATASETS_DIR, "complaints")
GEOSPATIAL_DATA_DIR = os.path.join(DATASETS_DIR, "geospatial")

# Model Paths
SCAM_CLASSIFIER_PATH = os.path.join(MODELS_DIR, "scam_classifier.joblib")
SCAM_VECTORIZER_PATH = os.path.join(MODELS_DIR, "scam_vectorizer.joblib")
CURRENCY_MODEL_PATH = os.path.join(MODELS_DIR, "currency_detector.joblib")

# Output Subfolders
GRAPHS_OUT_DIR = os.path.join(OUTPUTS_DIR, "graphs")
MAPS_OUT_DIR = os.path.join(OUTPUTS_DIR, "maps")
PREDICTIONS_OUT_DIR = os.path.join(OUTPUTS_DIR, "predictions")

# NLP Constants
SCAM_LABEL_MAPPING = {"normal": 0, "scam": 1}

# Currency Detection Constants
DENOMINATIONS = [100, 200, 500]
CURRENCY_LABEL_MAPPING = {"real": 0, "fake": 1}

# Scam classification triggers / warning words for Hinglish & English
SCAM_KEYWORDS = [
    "cbi", "enforcement directorate", "customs", "digital arrest", "narcotics",
    "illegal package", "passport blocked", "police custody", "money laundering",
    "court order", "supreme court", "skype call", "seized", "under arrest",
    "lottery", "kbc", "won", "crore", "processing fee"
]
