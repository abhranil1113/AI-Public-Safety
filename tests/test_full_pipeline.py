import os
import pytest
from src.agents.orchestrator_agent import PublicSafetyOrchestrator
from src.utils.constants import PREDICTIONS_OUT_DIR, REPORTS_DIR, OUTPUTS_DIR

def test_full_pipeline_orchestration():
    # Make sure we clean up outputs if they exist to verify creation
    scam_csv = os.path.join(PREDICTIONS_OUT_DIR, "scam_predictions.csv")
    curr_csv = os.path.join(PREDICTIONS_OUT_DIR, "currency_predictions.csv")
    graph_json = os.path.join(PREDICTIONS_OUT_DIR, "graph_clusters.json")
    geo_json = os.path.join(PREDICTIONS_OUT_DIR, "geo_hotspots.json")
    
    for f in [scam_csv, curr_csv, graph_json, geo_json]:
        if os.path.exists(f):
            try:
                os.remove(f)
            except Exception:
                pass
                
    orchestrator = PublicSafetyOrchestrator()
    results = orchestrator.run_full_analysis()
    
    assert results is not None
    assert results["rings_count"] >= 0
    assert results["ledger_verified"] is True
    
    # Assert expected prediction files exist
    assert os.path.exists(scam_csv)
    assert os.path.exists(curr_csv)
    assert os.path.exists(graph_json)
    assert os.path.exists(geo_json)
    
    # Assert reports exist
    assert os.path.exists(results["report_path_json"])
    assert os.path.exists(results["report_path_txt"])
    
    # Assert maps and graphs exist
    assert os.path.exists(results["map_path"])
    
    full_net_png = os.path.join(OUTPUTS_DIR, "graphs", "fraud_network.png")
    assert os.path.exists(full_net_png)
