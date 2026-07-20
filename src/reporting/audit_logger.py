import os
import json
import csv
import hashlib
from datetime import datetime
from src.utils.constants import LOGS_DIR, REPORTS_DIR
from src.utils.logger import setup_logger

logger = setup_logger("AuditLogger")

class CryptographicAuditLogger:
    def __init__(self, log_filename="audit_trail.jsonl"):
        self.log_path = os.path.join(LOGS_DIR, log_filename)
        self.csv_path = os.path.join(REPORTS_DIR, "audit_log.csv")
        self.last_hash = "0" * 64
        self.ensure_log_file()
        
    def ensure_log_file(self):
        """Create the log file if it doesn't exist, or verify existing history."""
        os.makedirs(LOGS_DIR, exist_ok=True)
        os.makedirs(REPORTS_DIR, exist_ok=True)
        if not os.path.exists(self.log_path):
            # Write genesis block
            genesis_entry = self.create_block("GENESIS", "System Initialization", "0" * 64)
            self.write_entry(genesis_entry)
            self.last_hash = genesis_entry["hash"]
            logger.info("Cryptographic audit log initialized with Genesis block.")
        else:
            # Verify and read last entry to continue chain
            valid, last_h = self.verify_chain()
            if valid:
                self.last_hash = last_h
                logger.info("Cryptographic audit log verified. Ready to append.")
            else:
                logger.error("AUDIT LOG INTEGRITY COMPROMISED! Tampering detected in audit_trail.jsonl")
                raise SecurityError("Audit log chain is broken or tampered with!")
        self.export_to_csv()

    def calculate_hash(self, block: dict) -> str:
        """Compute SHA-256 hash of a block's contents (excluding the hash itself)."""
        block_string = json.dumps({
            "timestamp": block["timestamp"],
            "action": block["action"],
            "payload_summary": block["payload_summary"],
            "previous_hash": block["previous_hash"]
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()

    def create_block(self, action: str, payload_summary: str, prev_hash: str) -> dict:
        block = {
            "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "action": action,
            "payload_summary": payload_summary,
            "previous_hash": prev_hash
        }
        block["hash"] = self.calculate_hash(block)
        return block

    def write_entry(self, entry: dict):
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")

    def log_event(self, action: str, payload_summary: str) -> str:
        """Append an auditable event to the chain."""
        block = self.create_block(action, payload_summary, self.last_hash)
        self.write_entry(block)
        self.last_hash = block["hash"]
        self.export_to_csv()
        return block["hash"]

    def export_to_csv(self):
        """Export the jsonl audit trail to a CSV format for legal audit reviews."""
        if not os.path.exists(self.log_path):
            return
            
        try:
            with open(self.log_path, "r", encoding="utf-8") as f_in, \
                 open(self.csv_path, "w", newline="", encoding="utf-8") as f_out:
                writer = csv.writer(f_out)
                writer.writerow(["timestamp", "action", "payload_summary", "previous_hash", "hash"])
                
                for line in f_in:
                    if line.strip():
                        block = json.loads(line)
                        writer.writerow([
                            block.get("timestamp"),
                            block.get("action"),
                            block.get("payload_summary"),
                            block.get("previous_hash"),
                            block.get("hash")
                        ])
        except Exception as e:
            logger.error(f"Failed to export audit log to CSV: {e}")

    def verify_chain(self) -> tuple[bool, str]:
        """Validate the cryptographic integrity of the log file from beginning to end."""
        if not os.path.exists(self.log_path):
            return False, "0" * 64
            
        current_prev_hash = "0" * 64
        last_h = "0" * 64
        
        with open(self.log_path, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    block = json.loads(line)
                except Exception:
                    return False, "0" * 64
                    
                # 1. Check link to previous block
                if block["previous_hash"] != current_prev_hash:
                    return False, "0" * 64
                    
                # 2. Check hash validity
                calculated = self.calculate_hash(block)
                if block["hash"] != calculated:
                    return False, "0" * 64
                    
                current_prev_hash = block["hash"]
                last_h = block["hash"]
                
        return True, last_h

class SecurityError(Exception):
    pass
