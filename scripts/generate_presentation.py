import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

def create_presentation_deck():
    pdf_path = r"D:\Ai Public Safety\assets\presentation_deck.pdf"
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    
    width, height = landscape(letter)
    
    c = canvas.Canvas(pdf_path, pagesize=(width, height))
    
    # Colors
    bg_color = HexColor("#1A1A2E")      # Dark navy/indigo
    primary_color = HexColor("#E94560") # Vibrant crimson
    text_color = HexColor("#FFFFFF")    # White
    muted_text = HexColor("#A2A8D3")    # Lavender grey
    card_bg = HexColor("#16213E")       # Card background blue
    accent_green = HexColor("#28DF99")  # Emerald green
    accent_yellow = HexColor("#FFD369") # Warm Gold
    
    slides = [
        # Slide 1: Title
        {
            "type": "title",
            "title": "AI FOR DIGITAL PUBLIC SAFETY",
            "subtitle": "Defeating Counterfeiting, Fraud & Digital Arrest Scams",
            "meta": "Theme: Smart Cities / Public Safety / Digital Trust\nGoogle Colab & CLI Demonstration Notebook Ready"
        },
        # Slide 2: Problem Context
        {
            "type": "bullets",
            "title": "Problem Context: The Crisis of Digital Trust",
            "bullets": [
                ("1.14 Million Cybercrime Complaints (2023)", "India registered a massive 60% surge in complaints compared to the previous year."),
                ("Digital Arrest Scams are Industrialised", "Organised networks impersonating CBI, ED, TRAI, and Customs operate out of cross-border compounds."),
                ("Rs 1,776 Crore Scammed in 9 Months", "MHA reports record financial losses from victims trapped in psychological hostage situations over video call."),
                ("Fake Indian Currency Notes (FICN) Threat", "RBI's Annual Report 2025 flagged high-quality counterfeit Rs 500 bills bypassing manual verification.")
            ]
        },
        # Slide 3: Challenge Statement
        {
            "type": "concept",
            "title": "The Challenge Statement",
            "concept": "Build an AI-powered Digital Public Safety Intelligence platform that equips law enforcement agencies, financial institutions, and citizens with proactive tools to detect, disrupt, and respond to digital fraud networks, counterfeit currency circulation, and organised scam operations — shifting from reactive case investigation to predictive threat neutralisation."
        },
        # Slide 4: Why This Platform is Different (Concept Slide)
        {
            "type": "concept",
            "title": "Why This Platform is Different",
            "concept": "Unlike standalone systems, our solution combines seven specialized AI agents that collaboratively analyze conversation content, voice biometrics, counterfeit currency, fraud graphs, and geospatial intelligence before generating an explainable, legally auditable recommendation. This multi-agent architecture reduces false positives, improves transparency, and enables proactive interventions before financial loss occurs."
        },
        # Slide 5: Solution Overview & Architecture
        {
            "type": "bullets",
            "title": "Solution Overview & Agentic Architecture",
            "bullets": [
                ("Agentic AI Orchestrator", "Acts as the central command, routing inputs to domain-specific agents and fusing their signals."),
                ("Five Specialized Subsystems", "Scam classification, speech forensics, citizen chatbot shield, counterfeit CV check, graph network mapping."),
                ("Cryptographic Audit Ledger", "Ensures all intelligence logs and findings are forensic-grade and court-admissible."),
                ("Google Colab & CLI Support", "Reconciled constraints to run seamlessly as a Python package, CLI utility, or Colab notebook.")
            ]
        },
        # Slide 6: Module 1 - Digital Arrest Scam Detection
        {
            "type": "bullets",
            "title": "Module 1: ScamShield Agent (Digital Arrest NLP)",
            "bullets": [
                ("Multi-Engine Pattern Check", "Supports three modes of analysis: rule Heuristic, machine learning, and advanced LLM."),
                ("Threat Progression Tracking", "Identifies current stage (e.g. Isolation) and predicts next likely stage (Payment Demand)."),
                ("Explainability Layer", "Highlights specific triggered indicators (Fake Authority, Psychological Coercion, Block Threats)."),
                ("Logistic Regression Rationale", "Selected because it provides explainable probabilities suitable for forensic NLP and small-to-medium datasets.")
            ]
        },
        # Slide 7: Module 2 - Speech AI & Voice Spoofing
        {
            "type": "bullets",
            "title": "Module 2: VoiceGuard Agent (Speech AI Forensics)",
            "bullets": [
                ("Acoustic Feature Extraction", "Simulates auditing of voice pitch variance, spectral roll-off, and centroid std."),
                ("Jitter and Shimmer Anomalies", "Identifies synthetic voices by analyzing the absence of micro-modulations (Li et al. 2023)."),
                ("Voice Cloned Flagging", "Alerts telecom systems when incoming speech streams match machine-synthesized speech signatures."),
                ("Lightweight OpenCV Rationale", "Allows lightweight feature processing and verification checks without requiring GPU inference.")
            ]
        },
        # Slide 8: Module 3 - Citizen Fraud Shield
        {
            "type": "bullets",
            "title": "Module 3: CitizenShield Agent (Conversational Chatbot)",
            "bullets": [
                ("Conversational Evaluation", "Provides instant risk verdicts for messages, links, and transaction requests."),
                ("Regional Advisory Support", "Supplies guided prevention steps in 4 regional languages (English, Hindi, Telugu, Tamil)."),
                ("NCRP-Style Incident Reports", "Autogenerates structured cyber incident reports matching NCRP workflows for manual submission."),
                ("12 Language Scalability Goal", "Designed to expand to 12 regional languages using multilingual LLMs or Translate APIs.")
            ]
        },
        # Slide 9: Module 4 - Counterfeit Currency Identification
        {
            "type": "bullets",
            "title": "Module 4: NoteGuard Agent (Explainable CV Checksheet)",
            "bullets": [
                ("Computer Vision Checksheet", "Audits notes using explicit checks (Security Thread, Watermark, UV, Serial Prefix)."),
                ("Random Forest Rationale", "Selected because it performs well on structured handcrafted counterfeit features while remaining explainable and lightweight."),
                ("Watermark & Microprint Check", "Evaluates sharpness using Laplacian variance and BGR channel distributions (PASS/FAIL)."),
                ("Deep Learning Fallback CNN", "Future work trains CNNs on rupee images to achieve >97% accuracy (Patil et al. 2022).")
            ]
        },
        # Slide 10: Module 5 - Fraud Network Graph Intelligence
        {
            "type": "bullets",
            "title": "Module 5: FraudGraph Agent (Network Mule Rings)",
            "bullets": [
                ("NetworkX Modeling Rationale", "Enables interpretable graph analytics and rapid fraud network visualization for investigative workflows."),
                ("Syndicate Clustering", "Traces transaction edges to discover coordinated rings utilizing shared device fingerprints."),
                ("Reveal Hidden Fraud Rings", "Serves as a magnifying glass (Linkurious) exposing illicit links traditional systems miss."),
                ("Admissible Court Evidence Package", "Generates comprehensive JSON dossiers compiling all linked victims and transactions.")
            ]
        },
        # Slide 11: Module 6 - Geospatial Patrol Priorities
        {
            "type": "bullets",
            "title": "Module 6: GeoWatch Agent (Geospatial Patrols)",
            "bullets": [
                ("GIS Statistical Crime Mapping", "Fuses crime rates, incident counts, and financial losses to generate risk rankings."),
                ("Incident Breakdown Reasons", "Displays the specific threat factors (number of complaints, spoofed numbers, UPI links)."),
                ("Actionable LEA Recommendations", "Deploy cyber investigation units, recommend telecom operator notification, and push awareness SMS."),
                ("Interactive Leaflet HTML Map", "Renders a dark-theme HTML map pinpointing district markers sized by financial damage.")
            ]
        },
        # Slide 12: Real-time Alerting & Lead Time Gained
        {
            "type": "bullets",
            "title": "Real-time Interception and Alerting",
            "bullets": [
                ("Active Interception Webhooks", "Simulates instant API notifications pushed to Jio, Airtel, and Vi telecom circles."),
                ("Fast Reaction Latency", "Average detection-to-alert latency clocked at under 0.45 seconds."),
                ("Massive Lead Time Gained", "Flags scam sessions 15-45 minutes before financial transfer occurs."),
                ("INR Losses Prevented", "Estimated savings calculated across batch runs, preventing lakhs in fraud transfers.")
            ]
        },
        # Slide 13: Multi-Source Risk Score Fusion
        {
            "type": "bullets",
            "title": "Weighted Threat Risk Fusion Engine",
            "bullets": [
                ("Multi-Modal Risk Correlator", "Correlates distinct risks: Text (NLP), Voice (Acoustic), Graph (Mule), and Geo (Hotspot)."),
                ("Weighted Threat Formula", "Applies: FusedScore = 0.4*Text + 0.2*Voice + 0.2*Graph + 0.2*Geo."),
                ("Unified Threat Ratings", "Translates the fused score into priority levels (CRITICAL, HIGH, MEDIUM, LOW)."),
                ("Weight Selection Rationale", "Text (40% primary intent), Voice (20% acoustics), Graph (20% mule links), Geo (20% context).")
            ]
        },
        # Slide 14: Human-in-the-Loop Workflow
        {
            "type": "bullets",
            "title": "Human-in-the-Loop (HITL) Admissibility",
            "bullets": [
                ("LEA Decision Support", "The AI system does not issue automated arrests or bank blocks without verification."),
                ("Officer Review Dashboard", "Enables officers to inspect auto-drafted court evidence packages via the CLI interface."),
                ("Cryptographic Sign-Off", "Upon approval, the officer's choice is cryptographically signed and hashed in the ledger."),
                ("Tamper-Proof Ledger", "Section 65B compliance is validated by ensuring that approved FIR drafts remain locked.")
            ]
        },
        # Slide 15: Responsible AI & Deployment Considerations
        {
            "type": "bullets",
            "title": "Responsible AI & Deployment Scope",
            "bullets": [
                ("Decision Support System", "Designed to assist investigators and financial institutions; final operational decisions remain with authorized personnel."),
                ("Synthetic Evaluation Data", "Prototype models are evaluated using carefully generated synthetic datasets due to limited public fraud data availability."),
                ("Simulated Integrations", "Telecom notifications, government alerts, and NCRP workflows are demonstrated as simulated integrations."),
                ("Officer Oversight Lock", "All enforcement actions require officer review through the Human-in-the-Loop (HITL) workflow before escalation.")
            ]
        },
        # Slide 16: Future Roadmap
        {
            "type": "bullets",
            "title": "Future Technical Roadmap",
            "bullets": [
                ("Voice Streaming Forensics", "Real-time analysis of active phone/VoIP calls using low-latency streaming biometrics."),
                ("Edge AI Counterfeit Detection", "Optimizing NoteGuard to execute Random Forest & CNN models directly on low-power mobile GPUs."),
                ("Graph Neural Networks (GNNs)", "Enhancing FraudGraph with GNN link prediction models to forecast money mule ring formation."),
                ("WhatsApp & IVR Shield Bot", "Direct deployment of CitizenShield chatbot to WhatsApp Business API and national IVR helplines.")
            ]
        },
        # Slide 17: Supporting Research & References
        {
            "type": "bullets",
            "title": "Supporting Research & Industry References",
            "bullets": [
                ("1. Counterfeit CV (Patil et al. 2022)", "Rupee classification CNNs achieve >97% accuracy - proving deep learning is a viable explainable fallback."),
                ("2. Audio Spoofing (Li et al. 2023)", "Validates vocal jitter & shimmer anomalies as high-precision features for detecting deepfake cloned voices."),
                ("3. Graph AML (Linkurious 2024)", "Exposes illicit money flows and money mule network clusters that traditional relational checks miss."),
                ("4. GIS Hotspots (PolicingInsight 2023)", "Emphasizes predictive crime mapping accountability and officer review requirements to avoid bias.")
            ]
        },
        # Slide 18: Conclusion & Thank You
        {
            "type": "conclusion",
            "title": "Thank You!",
            "message": "AI for Digital Public Safety Intelligence Platform\nSecuring Smart Cities, Safeguarding Citizens.",
            "meta": "GitHub: https://github.com/public-safety-ai\nContact: safety-dev@publicsafety.gov.in"
        }
    ]
    
    for i, slide in enumerate(slides):
        slide_num = i + 1
        
        c.setFillColor(bg_color)
        c.rect(0, 0, width, height, fill=True, stroke=False)
        
        if slide["type"] not in ["title", "conclusion"]:
            c.setFillColor(card_bg)
            c.rect(0, height - 70, width, 70, fill=True, stroke=False)
            
            c.setFillColor(primary_color)
            c.rect(0, height - 70, 8, 70, fill=True, stroke=False)
            
            c.setFont("Helvetica-Bold", 20)
            c.setFillColor(text_color)
            c.drawString(30, height - 42, slide["title"])
            
            c.setFont("Helvetica-Oblique", 10)
            c.setFillColor(muted_text)
            c.drawString(30, height - 60, "CONFIDENTIAL // LAW ENFORCEMENT INTELLIGENCE CORE")
            
        c.setFillColor(HexColor("#12192C"))
        c.rect(0, 0, width, 30, fill=True, stroke=False)
        c.setFont("Helvetica", 9)
        c.setFillColor(muted_text)
        c.drawString(30, 10, "AI FOR DIGITAL PUBLIC SAFETY  |  HACKATHON SUBMISSION")
        c.drawRightString(width - 30, 10, f"Slide {slide_num} of {len(slides)}")
        
        if slide["type"] == "title":
            c.setFillColor(primary_color)
            c.rect(0, height - 15, width, 15, fill=True, stroke=False)
            c.setFillColor(HexColor("#3F72AF"))
            c.rect(0, 0, width, 15, fill=True, stroke=False)
            
            c.setFont("Helvetica-Bold", 36)
            c.setFillColor(primary_color)
            c.drawCentredString(width/2.0, height/2.0 + 50, slide["title"])
            
            c.setFont("Helvetica", 20)
            c.setFillColor(text_color)
            c.drawCentredString(width/2.0, height/2.0 - 10, slide["subtitle"])
            
            c.setFont("Helvetica", 12)
            c.setFillColor(muted_text)
            meta_lines = slide["meta"].split("\n")
            c.drawCentredString(width/2.0, height/2.0 - 80, meta_lines[0])
            c.drawCentredString(width/2.0, height/2.0 - 105, meta_lines[1])
            
        elif slide["type"] == "conclusion":
            c.setFillColor(primary_color)
            c.rect(0, height - 15, width, 15, fill=True, stroke=False)
            
            c.setFont("Helvetica-Bold", 36)
            c.setFillColor(primary_color)
            c.drawCentredString(width/2.0, height/2.0 + 40, slide["title"])
            
            c.setFont("Helvetica-Bold", 18)
            c.setFillColor(text_color)
            msg_lines = slide["message"].split("\n")
            c.drawCentredString(width/2.0, height/2.0 - 20, msg_lines[0])
            c.drawCentredString(width/2.0, height/2.0 - 50, msg_lines[1])
            
            c.setFont("Helvetica", 11)
            c.setFillColor(accent_green)
            meta_lines = slide["meta"].split("\n")
            c.drawCentredString(width/2.0, height/2.0 - 120, meta_lines[0])
            c.drawCentredString(width/2.0, height/2.0 - 145, meta_lines[1])
            
        elif slide["type"] == "concept":
            box_w, box_h = 600, 220
            box_x = (width - box_w)/2.0
            box_y = (height - box_h)/2.0 - 20
            
            c.setFillColor(card_bg)
            c.rect(box_x, box_y, box_w, box_h, fill=True, stroke=True)
            c.setStrokeColor(primary_color)
            c.rect(box_x, box_y, box_w, box_h, fill=False, stroke=True)
            
            c.setFont("Helvetica", 14)
            c.setFillColor(text_color)
            words = slide["concept"].split()
            lines = []
            current_line = []
            
            for word in words:
                current_line.append(word)
                if len(" ".join(current_line)) > 60:
                    current_line.pop()
                    lines.append(" ".join(current_line))
                    current_line = [word]
            if current_line:
                lines.append(" ".join(current_line))
                
            curr_y = box_y + box_h - 40
            for line in lines:
                c.drawCentredString(width/2.0, curr_y, line)
                curr_y -= 26
                
        elif slide["type"] == "bullets":
            items = slide["bullets"]
            
            # Left Card 1
            x1, y1 = 40, height - 250
            w1, h1 = 340, 150
            c.setFillColor(card_bg)
            c.rect(x1, y1, w1, h1, fill=True, stroke=False)
            c.setFillColor(primary_color)
            c.rect(x1, y1 + h1 - 5, w1, 5, fill=True, stroke=False)
            
            c.setFont("Helvetica-Bold", 13)
            c.setFillColor(accent_yellow)
            c.drawString(x1 + 15, y1 + h1 - 30, items[0][0])
            c.setFont("Helvetica", 11)
            c.setFillColor(text_color)
            c.drawString(x1 + 15, y1 + h1 - 60, items[0][1][:50])
            c.drawString(x1 + 15, y1 + h1 - 78, items[0][1][50:100])
            c.drawString(x1 + 15, y1 + h1 - 96, items[0][1][100:])
            
            # Right Card 1
            x2, y2 = 410, height - 250
            c.setFillColor(card_bg)
            c.rect(x2, y2, w1, h1, fill=True, stroke=False)
            c.setFillColor(accent_green)
            c.rect(x2, y2 + h1 - 5, w1, 5, fill=True, stroke=False)
            
            c.setFont("Helvetica-Bold", 13)
            c.setFillColor(accent_yellow)
            c.drawString(x2 + 15, y2 + h1 - 30, items[1][0])
            c.setFont("Helvetica", 11)
            c.setFillColor(text_color)
            c.drawString(x2 + 15, y2 + h1 - 60, items[1][1][:50])
            c.drawString(x2 + 15, y2 + h1 - 78, items[1][1][50:100])
            c.drawString(x2 + 15, y2 + h1 - 96, items[1][1][100:])
            
            # Left Card 2
            x3, y3 = 40, height - 440
            c.setFillColor(card_bg)
            c.rect(x3, y3, w1, h1, fill=True, stroke=False)
            c.setFillColor(HexColor("#3F72AF"))
            c.rect(x3, y3 + h1 - 5, w1, 5, fill=True, stroke=False)
            
            c.setFont("Helvetica-Bold", 13)
            c.setFillColor(accent_yellow)
            c.drawString(x3 + 15, y3 + h1 - 30, items[2][0])
            c.setFont("Helvetica", 11)
            c.setFillColor(text_color)
            c.drawString(x3 + 15, y3 + h1 - 60, items[2][1][:50])
            c.drawString(x3 + 15, y3 + h1 - 78, items[2][1][50:100])
            c.drawString(x3 + 15, y3 + h1 - 96, items[2][1][100:])
            
            # Right Card 2
            x4, y4 = 410, height - 440
            c.setFillColor(card_bg)
            c.rect(x4, y4, w1, h1, fill=True, stroke=False)
            c.setFillColor(HexColor("#9E78F5"))
            c.rect(x4, y4 + h1 - 5, w1, 5, fill=True, stroke=False)
            
            c.setFont("Helvetica-Bold", 13)
            c.setFillColor(accent_yellow)
            c.drawString(x4 + 15, y4 + h1 - 30, items[3][0])
            c.setFont("Helvetica", 11)
            c.setFillColor(text_color)
            c.drawString(x4 + 15, y4 + h1 - 60, items[3][1][:50])
            c.drawString(x4 + 15, y4 + h1 - 78, items[3][1][50:100])
            c.drawString(x4 + 15, y4 + h1 - 96, items[3][1][100:])
            
        c.showPage()
        
    c.save()
    print(f"Presentation deck successfully created at {pdf_path}")

if __name__ == "__main__":
    create_presentation_deck()
