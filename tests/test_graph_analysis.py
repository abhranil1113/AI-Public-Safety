import pytest
import networkx as nx
from src.graph.fraud_graph import FraudGraphAnalyzer

def test_graph_construction():
    analyzer = FraudGraphAnalyzer()
    
    # Verify graph exists and has nodes
    assert analyzer.G is not None
    assert analyzer.G.number_of_nodes() > 0
    assert analyzer.G.number_of_edges() > 0

def test_find_mule_networks():
    analyzer = FraudGraphAnalyzer()
    networks = analyzer.find_mule_networks()
    
    assert isinstance(networks, list)
    if networks:
        first_net = networks[0]
        assert "mule_account" in first_net
        assert "total_fraud_volume" in first_net
        assert "syndicate_risk" in first_net

def test_generate_evidence_package():
    analyzer = FraudGraphAnalyzer()
    networks = analyzer.find_mule_networks()
    
    if networks:
        mule = networks[0]["mule_account"]
        packet = analyzer.generate_intelligence_package(mule)
        
        assert packet["target_mule_account"] == mule
        assert "evidence_summary" in packet
        assert "detailed_transactions" in packet
        assert packet["legal_admissibility_status"] is not None
