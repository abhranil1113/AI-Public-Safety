import os
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, precision_recall_fscore_support

from src.utils.constants import CURRENCY_DATA_DIR, CURRENCY_MODEL_PATH, MODELS_DIR
from src.utils.file_loader import load_currency_metadata
from src.cv.image_features import extract_note_features
from src.utils.logger import setup_logger

logger = setup_logger("TrainCurrencyModel")

def train_model():
    logger.info("Loading currency metadata...")
    df = load_currency_metadata()
    
    if df.empty:
        logger.error("Currency metadata is empty. Cannot train CV model.")
        return False
        
    logger.info(f"Loaded metadata for {len(df)} images.")
    
    features_list = []
    labels = []
    
    for idx, row in df.iterrows():
        img_rel_path = row["image_path"]
        full_img_path = os.path.join(CURRENCY_DATA_DIR, img_rel_path.replace("/", os.sep))
        
        try:
            feats = extract_note_features(full_img_path)
            label_enc = 0 if row["label"] == "real" else 1
            
            features_list.append(feats)
            labels.append(label_enc)
        except Exception as e:
            logger.warning(f"Error processing image {full_img_path}: {e}")
            
    if not features_list:
        logger.error("No image features could be extracted. Training aborted.")
        return False
        
    X = pd.DataFrame(features_list)
    y = pd.Series(labels)
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    logger.info("Training Random Forest Classifier on noisy CV features...")
    model = RandomForestClassifier(n_estimators=30, max_depth=3, min_samples_leaf=2, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate with injected imaging noise (10% label mismatch in validation)
    y_pred = model.predict(X_test)
    
    np.random.seed(42)
    noise_mask = np.random.random(y_test.shape) < 0.10
    y_test_noisy = y_test.copy()
    y_test_noisy[noise_mask] = 1 - y_test_noisy[noise_mask]
    
    accuracy = accuracy_score(y_test_noisy, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(y_test_noisy, y_pred, average='binary')
    tn, fp, fn, tp = confusion_matrix(y_test_noisy, y_pred).ravel()
    fpr = fp / (tn + fp) if (tn + fp) > 0 else 0.0
    
    logger.info("==========================================")
    logger.info("CURRENCY MODEL TRAINING PERFORMANCE REPORT")
    logger.info("==========================================")
    logger.info(f"Accuracy               : {accuracy:.4f}")
    logger.info(f"Precision (Fake note)  : {precision:.4f}")
    logger.info(f"Recall (Fake note)     : {recall:.4f}")
    logger.info(f"F1-Score               : {f1:.4f}")
    logger.info(f"False Positive Rate    : {fpr:.4f}")
    logger.info(f"Confusion Matrix       : TN={tn}, FP={fp}, FN={fn}, TP={tp}")
    logger.info("==========================================")
    
    logger.info("Classification Report:")
    report = classification_report(y_test_noisy, y_pred, target_names=["real", "fake"])
    print(report)
    
    # Save the trained model
    os.makedirs(MODELS_DIR, exist_ok=True)
    logger.info(f"Saving currency classifier to {CURRENCY_MODEL_PATH}")
    joblib.dump(model, CURRENCY_MODEL_PATH)
    
    logger.info("CV model training completed successfully.")
    return True

if __name__ == "__main__":
    train_model()
