import os
import matplotlib.pyplot as plt
import networkx as nx
from src.graph.fraud_graph import FraudGraphAnalyzer
from src.utils.constants import GRAPHS_OUT_DIR
from src.utils.logger import setup_logger

logger = setup_logger("GraphVisualizer")

def visualize_mule_ring(analyzer: FraudGraphAnalyzer, mule_account: str, filename="mule_ring.png"):
    """
    Visualize the fraud ring ego network around a specific mule account
    and save the output image.
    """
    if not analyzer.G.has_node(mule_account):
        logger.error(f"Cannot visualize: {mule_account} is not in the graph.")
        return None

    # Get ego graph (radius=2)
    undirected_G = analyzer.G.to_undirected()
    ego = nx.ego_graph(undirected_G, mule_account, radius=2)
    
    # Create matching directed subgraph from original G
    subgraph = analyzer.G.subgraph(ego.nodes())
    
    plt.figure(figsize=(12, 10), facecolor='#1A1A2E') # Premium Dark theme background
    ax = plt.gca()
    ax.set_facecolor('#1A1A2E')
    
    # Separate nodes by type for customized coloring/sizing
    node_colors = []
    node_sizes = []
    
    # Define color scheme
    color_map = {
        "mule": "#E94560",        # Red
        "account": "#0F3460",     # Deep blue
        "device": "#FFD369",      # Gold/Yellow
        "complaint": "#E2B2FF",   # Light Purple
        "phone": "#28DF99"        # Mint green
    }
    
    for node in subgraph.nodes():
        node_type = subgraph.nodes[node].get("type", "account")
        is_mule = subgraph.nodes[node].get("label") == "mule" or node == mule_account
        
        if is_mule:
            node_colors.append(color_map["mule"])
            node_sizes.append(1000)
        elif node_type == "device":
            node_colors.append(color_map["device"])
            node_sizes.append(400)
        elif node_type == "complaint":
            node_colors.append(color_map["complaint"])
            node_sizes.append(500)
        elif node_type == "phone":
            node_colors.append(color_map["phone"])
            node_sizes.append(600)
        else: # general account
            node_colors.append(color_map["account"])
            node_sizes.append(700)
            
    # Set layout
    pos = nx.spring_layout(subgraph, k=0.5, seed=42)
    
    # Draw nodes
    nx.draw_networkx_nodes(
        subgraph, pos, 
        node_color=node_colors, 
        node_size=node_sizes,
        alpha=0.9,
        edgecolors='#EEEEEE',
        linewidths=1.5
    )
    
    # Draw edges
    # Distinguish transaction edges from other relations
    tx_edges = [(u, v) for u, v, k, d in subgraph.edges(keys=True, data=True) if d.get("type") == "transaction"]
    other_edges = [(u, v) for u, v, k, d in subgraph.edges(keys=True, data=True) if d.get("type") != "transaction"]
    
    nx.draw_networkx_edges(
        subgraph, pos, 
        edgelist=tx_edges, 
        edge_color="#00ADB5", 
        width=2.0, 
        arrowsize=15, 
        arrowstyle="->"
    )
    
    nx.draw_networkx_edges(
        subgraph, pos, 
        edgelist=other_edges, 
        edge_color="#393E46", 
        style="dashed", 
        width=1.2, 
        arrowsize=10
    )
    
    # Labels
    labels = {node: f"{node}\n({subgraph.nodes[node].get('type', 'acc')})" for node in subgraph.nodes()}
    nx.draw_networkx_labels(
        subgraph, pos, 
        labels=labels, 
        font_size=8, 
        font_color="#FFFFFF", 
        font_weight="bold"
    )
    
    plt.title(f"Fraud Ring Analysis: {mule_account} Network", color="#FFFFFF", fontsize=14, fontweight="bold", pad=20)
    plt.axis("off")
    
    # Save diagram
    os.makedirs(GRAPHS_OUT_DIR, exist_ok=True)
    out_path = os.path.join(GRAPHS_OUT_DIR, filename)
    plt.tight_layout()
    plt.savefig(out_path, facecolor='#1A1A2E', edgecolor='none', dpi=300)
    plt.close()
    
    logger.info(f"Mule ring visualization saved to {out_path}")
    return out_path

def visualize_full_network(analyzer: FraudGraphAnalyzer, filename="fraud_network.png") -> str:
    """
    Visualize the entire heterogeneous fraud transaction network.
    Saves a high-quality visualization map.
    """
    plt.figure(figsize=(14, 12), facecolor='#1A1A2E')
    ax = plt.gca()
    ax.set_facecolor('#1A1A2E')
    
    # We will sample or plot the entire graph if it's not too big. 
    # Our generated data is small enough (~150 nodes).
    subgraph = analyzer.G
    
    pos = nx.spring_layout(subgraph, k=0.3, seed=42)
    
    # Node color scheme
    color_map = {
        "mule": "#E94560",        # Red
        "account": "#0F3460",     # Deep blue
        "device": "#FFD369",      # Gold/Yellow
        "complaint": "#E2B2FF",   # Light Purple
        "phone": "#28DF99"        # Mint green
    }
    
    node_colors = []
    node_sizes = []
    for node in subgraph.nodes():
        node_type = subgraph.nodes[node].get("type", "account")
        is_mule = subgraph.nodes[node].get("label") == "mule"
        
        if is_mule:
            node_colors.append(color_map["mule"])
            node_sizes.append(400)
        elif node_type == "device":
            node_colors.append(color_map["device"])
            node_sizes.append(150)
        elif node_type == "complaint":
            node_colors.append(color_map["complaint"])
            node_sizes.append(200)
        elif node_type == "phone":
            node_colors.append(color_map["phone"])
            node_sizes.append(250)
        else:
            node_colors.append(color_map["account"])
            node_sizes.append(250)
            
    # Draw nodes
    nx.draw_networkx_nodes(
        subgraph, pos,
        node_color=node_colors,
        node_size=node_sizes,
        alpha=0.8,
        edgecolors='#EEEEEE',
        linewidths=0.8
    )
    
    # Draw edges
    tx_edges = [(u, v) for u, v, k, d in subgraph.edges(keys=True, data=True) if d.get("type") == "transaction"]
    other_edges = [(u, v) for u, v, k, d in subgraph.edges(keys=True, data=True) if d.get("type") != "transaction"]
    
    nx.draw_networkx_edges(
        subgraph, pos,
        edgelist=tx_edges,
        edge_color="#00ADB5",
        width=1.0,
        alpha=0.6,
        arrowsize=8
    )
    nx.draw_networkx_edges(
        subgraph, pos,
        edgelist=other_edges,
        edge_color="#393E46",
        style="dashed",
        width=0.8,
        alpha=0.5
    )
    
    # Draw labels for top mule accounts only to prevent clutter
    mule_labels = {
        node: f"MULE:{node}" 
        for node in subgraph.nodes() 
        if subgraph.nodes[node].get("label") == "mule"
    }
    nx.draw_networkx_labels(
        subgraph, pos,
        labels=mule_labels,
        font_size=8,
        font_color="#FFFFFF",
        font_weight="bold"
    )
    
    plt.title("Multi-Entity Digital Public Safety Fraud Network Map", color="#FFFFFF", fontsize=16, fontweight="bold", pad=20)
    plt.axis("off")
    
    os.makedirs(GRAPHS_OUT_DIR, exist_ok=True)
    out_path = os.path.join(GRAPHS_OUT_DIR, filename)
    plt.tight_layout()
    plt.savefig(out_path, facecolor='#1A1A2E', edgecolor='none', dpi=300)
    plt.close()
    
    logger.info(f"Full network map saved to {out_path}")
    return out_path

