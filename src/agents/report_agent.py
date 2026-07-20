from typing import Dict, Any, List
from src.reporting.audit_logger import CryptographicAuditLogger
from src.reporting.intelligence_report import IntelligenceReportGenerator
from src.utils.logger import setup_logger

logger = setup_logger("ReportAgent")

class ReportAgent:
    def __init__(self):
        self.audit_logger = CryptographicAuditLogger()
        self.generator = IntelligenceReportGenerator(self.audit_logger)
        
    def log_audit_event(self, action: str, summary: str) -> str:
        """Register a generic system event in the auditable hash ledger."""
        logger.info(f"Hashing event: [{action}] - {summary}")
        return self.audit_logger.log_event(action, summary)
        
    def create_intelligence_report(
        self, 
        scam_stats: Dict[str, Any], 
        currency_stats: Dict[str, Any], 
        graph_rings: List[Dict[str, Any]], 
        hotspots: List[Dict[str, Any]],
        speech_stats: Dict[str, Any] = None,
        citizen_shield_stats: Dict[str, Any] = None
    ) -> tuple[str, str]:
        """Compile a formal intelligence report and return both JSON and TXT report paths."""
        logger.info("Assembling multi-source public safety intelligence report...")
        return self.generator.generate_report(scam_stats, currency_stats, graph_rings, hotspots, speech_stats, citizen_shield_stats)
        
    def verify_ledger_integrity(self) -> bool:
        """Confirm that the audit log has not been modified or corrupted."""
        logger.info("Executing SHA-256 ledger integrity audit...")
        valid, _ = self.audit_logger.verify_chain()
        return valid
