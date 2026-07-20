from typing import Dict, List, Any
from src.graph.fraud_graph import FraudGraphAnalyzer
from src.graph.graph_visualizer import visualize_mule_ring
from src.utils.logger import setup_logger

logger = setup_logger("GraphAgent")

class GraphAgent:
    def __init__(self):
        self.analyzer = FraudGraphAnalyzer()
        
    def find_networks(self) -> List[Dict[str, Any]]:
        """Identify clustered networks of mule accounts and shared devices."""
        logger.info("Extracting fraud network clusters...")
        return self.analyzer.find_mule_networks()
        
    def generate_evidence_package(self, mule_account: str) -> Dict[str, Any]:
        """Compile a court-admissible forensic package on a mule account."""
        logger.info(f"Generating court-ready intelligence packet for: {mule_account}")
        return self.analyzer.generate_intelligence_package(mule_account)
        
    def visualize_ring(self, mule_account: str) -> str:
        """Create a premium visualization map of the specified mule ring."""
        logger.info(f"Visualizing network topology of {mule_account} ring.")
        filename = f"ring_{mule_account}.png"
        return visualize_mule_ring(self.analyzer, mule_account, filename)
        
    def visualize_entire_network(self) -> str:
        """Create a premium visualization map of the entire transaction database."""
        logger.info("Visualizing full network database graph.")
        from src.graph.graph_visualizer import visualize_full_network
        return visualize_full_network(self.analyzer, "fraud_network.png")

