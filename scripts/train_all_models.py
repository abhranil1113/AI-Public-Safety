from src.nlp.train_scam_model import train_model as train_nlp
from src.cv.train_currency_model import train_model as train_cv
from src.utils.logger import setup_logger

logger = setup_logger("TrainAllModels")

def main():
    logger.info("==========================================")
    logger.info("Starting Training Pipeline for AI Public Safety Platform")
    logger.info("==========================================")
    
    # 1. NLP Scam Classifier
    logger.info("--- Step 1: Training NLP Scam Classifier ---")
    nlp_success = train_nlp()
    if nlp_success:
        logger.info("NLP Model trained successfully.")
    else:
        logger.error("NLP Model training failed.")
        
    # 2. CV Currency Detector
    logger.info("--- Step 2: Training CV Currency Detector ---")
    cv_success = train_cv()
    if cv_success:
        logger.info("CV Model trained successfully.")
    else:
        logger.error("CV Model training failed.")
        
    logger.info("==========================================")
    if nlp_success and cv_success:
        logger.info("All models trained successfully!")
    else:
        logger.warning("Training completed with some warnings/failures.")
    logger.info("==========================================")

if __name__ == "__main__":
    main()
