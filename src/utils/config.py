import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# API Keys and configuration settings
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# App setting flags
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() in ("true", "1", "t")

# Helper checking function
def validate_config():
    """Verify if essential configurations are present."""
    warnings = []
    if not GEMINI_API_KEY and not OPENROUTER_API_KEY and not GROQ_API_KEY:
        warnings.append("No active LLM API key detected in environmental variables (.env). Direct API calls will fail.")
    return len(warnings) == 0, warnings
