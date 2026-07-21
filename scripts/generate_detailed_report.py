import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#475569"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 750, "AI FOR DIGITAL PUBLIC SAFETY INTELLIGENCE PLATFORM — DETAILED REPORT")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 742, 558, 742)
            
        # Footer
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 36, page_str)
        self.drawString(54, 36, "CONFIDENTIAL — FOR LAW ENFORCEMENT & PUBLIC SAFETY EVALUATION")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 48, 558, 48)
        
        self.restoreState()

def create_detailed_pdf():
    pdf_path = r"D:\Ai Public Safety\docs\detailed_project_report.pdf"
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Palette
    PRIMARY = colors.HexColor("#0F172A")    # Dark Navy Header
    SECONDARY = colors.HexColor("#1E3A8A")  # Royal Deep Blue
    TEXT_DARK = colors.HexColor("#1E293B")  # Charcoal body text
    BG_LIGHT = colors.HexColor("#F8FAFC")   # Light Slate background
    BORDER_COLOR = colors.HexColor("#E2E8F0")
    
    # Custom Paragraph Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=PRIMARY,
        alignment=TA_LEFT,
        spaceAfter=8
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=SECONDARY,
        alignment=TA_LEFT,
        spaceAfter=12
    )
    
    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#64748B"),
        spaceAfter=12
    )
    
    h1_style = ParagraphStyle(
        'DocH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=PRIMARY,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'DocH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=SECONDARY,
        spaceBefore=10,
        spaceAfter=5,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=TEXT_DARK,
        spaceAfter=8,
        alignment=TA_JUSTIFY
    )
    
    bullet_style = ParagraphStyle(
        'DocBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=TEXT_DARK,
        spaceAfter=4,
        leftIndent=15
    )
    
    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=13,
        textColor=PRIMARY
    )
    
    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white,
        alignment=TA_LEFT
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=TEXT_DARK,
        alignment=TA_LEFT
    )

    story = []

    # Title Banner
    story.append(Paragraph("AI FOR DIGITAL PUBLIC SAFETY INTELLIGENCE PLATFORM", title_style))
    story.append(Paragraph("A Multi-Agent AI System for Digital Arrest Scam Neutralization, Speech Forensics, Counterfeit Currency Verification, Mule Network Graph Analysis, and Geospatial Intelligence", subtitle_style))
    story.append(Paragraph("Comprehensive Technical Architecture & Implementation Report | Section 65B-Aligned", meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY, spaceBefore=0, spaceAfter=12))

    # Executive Summary
    story.append(Paragraph("1. EXECUTIVE SUMMARY", h1_style))
    story.append(Paragraph(
        "This document presents the technical architecture, forensic algorithms, software implementation, and evaluation metrics of the AI for Digital Public Safety Intelligence Platform. Designed to combat the rapid escalation of cyber fraud, digital arrest scams, synthetic voice deepfakes, money laundering rings, and counterfeit currency, the platform coordinates seven domain-specific AI agents under a centralized supervisor. Moving beyond reactive investigation after financial loss occurs, the platform processes real-time telecommunications transcripts, acoustic voice biometrics, computer vision banknote checksheet parameters, multi-hop financial transaction graphs, and regional geospatial crime indices to generate actionable public safety intelligence and court-admissible evidence dossiers under strict Human-in-the-Loop oversight.",
        body_style
    ))

    # Problem Context
    story.append(Paragraph("2. PROBLEM CONTEXT & OPERATIONAL THREAT ENVIRONMENT", h1_style))
    story.append(Paragraph(
        "Digital public safety in India faces unprecedented challenges from multi-vector cyber financial crimes:",
        body_style
    ))
    story.append(Paragraph("• <b>Cybercrime Surge:</b> India registered 1.14 million cybercrime complaints in 2023, representing a 60 percent increase over 2022.", bullet_style))
    story.append(Paragraph("• <b>Digital Arrest Scam Crisis:</b> Fraudulent syndicates impersonating law enforcement officers (CBI, ED, TRAI, Customs) coerced victims into multi-day video isolation hostage situations, defrauding citizens of over Rs 1,776 crore in the first nine months of 2024.", bullet_style))
    story.append(Paragraph("• <b>Counterfeit Currency Circulation:</b> Record Fake Indian Currency Notes (FICN) seizures highlighted by the Reserve Bank of India (RBI) Annual Report 2024-25 demonstrate high-denomination Rs 500 counterfeits capable of bypassing routine teller checks.", bullet_style))
    story.append(Paragraph("• <b>Proactive Intelligence Deficit:</b> Traditional systems operate reactively upon complaint filing. Law enforcement lacks real-time threat neutralization tools at the point of citizen contact before financial transfer occurs.", bullet_style))

    # Multi-Agent System Architecture
    story.append(Paragraph("3. MULTI-AGENT SYSTEM ARCHITECTURE", h1_style))
    story.append(Paragraph(
        "The platform coordinates specialized autonomous agents operating concurrently under a central supervisor:",
        body_style
    ))

    # Architecture Table
    table_data = [
        [
            Paragraph("Agent Name", table_header_style),
            Paragraph("Technology & Algorithms", table_header_style),
            Paragraph("Core Functionality & Operational Role", table_header_style)
        ],
        [
            Paragraph("<b>ScamShield Agent</b>", table_cell_style),
            Paragraph("TF-IDF + Logistic Regression / Gemini LLM Fallback", table_cell_style),
            Paragraph("Detects digital arrest scam signatures, extracts explainable coercion indicators, and forecasts psychological threat stage progression.", table_cell_style)
        ],
        [
            Paragraph("<b>VoiceGuard Agent</b>", table_cell_style),
            Paragraph("Acoustic Speech Signal Processing (Pitch, Jitter, Shimmer)", table_cell_style),
            Paragraph("Audits vocal micro-fluctuations to identify synthetic AI voice clones and machine-generated speech spoofs.", table_cell_style)
        ],
        [
            Paragraph("<b>CitizenShield Agent</b>", table_cell_style),
            Paragraph("Conversational Advisor (4 Regional Languages)", table_cell_style),
            Paragraph("Provides immediate citizen risk verdicts in English, Hindi, Telugu, and Tamil, and autogenerates structured NCRP incident drafts.", table_cell_style)
        ],
        [
            Paragraph("<b>NoteGuard Agent</b>", table_cell_style),
            Paragraph("OpenCV Checksheet + Random Forest / CNN Fallback", table_cell_style),
            Paragraph("Screens physical currency notes against security thread, watermark sharpness, UV fluorescence, and serial prefix regex checks.", table_cell_style)
        ],
        [
            Paragraph("<b>FraudGraph Agent</b>", table_cell_style),
            Paragraph("NetworkX MultiDiGraph (Ego-Network Clustering)", table_cell_style),
            Paragraph("Maps transaction linkages, clusters money mule account rings, detects shared device IDs, and compiles evidence dossiers.", table_cell_style)
        ],
        [
            Paragraph("<b>GeoWatch Agent</b>", table_cell_style),
            Paragraph("GIS Crime Mapping & Spatial Prioritization Matrix", table_cell_style),
            Paragraph("Computes district risk density indices, renders interactive Leaflet HTML heatmaps, and generates patrol dispatch routing.", table_cell_style)
        ],
        [
            Paragraph("<b>Orchestrator Agent</b>", table_cell_style),
            Paragraph("Multi-Source Weighted Risk Score Fusion Engine", table_cell_style),
            Paragraph("Fuses Text (40%), Voice (20%), Graph (20%), and Geo (20%) scores into a unified threat rating (CRITICAL, HIGH, MEDIUM, LOW).", table_cell_style)
        ],
        [
            Paragraph("<b>Audit Logger</b>", table_cell_style),
            Paragraph("SHA-256 Cryptographic Hash Chain Ledger", table_cell_style),
            Paragraph("Seals all event logs and evidence files into a tamper-proof cryptographic ledger aligned with Section 65B requirements.", table_cell_style)
        ]
    ]

    t = Table(table_data, colWidths=[105, 155, 244])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, BG_LIGHT]),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

    # Detailed Module Breakdown
    story.append(Paragraph("4. SUBSYSTEM MODULE TECHNICAL BREAKDOWN", h1_style))

    story.append(Paragraph("A. ScamShield Agent (Digital Arrest NLP & Threat Progression)", h2_style))
    story.append(Paragraph(
        "The ScamShield module analyzes incoming telecommunications call transcripts for explicit coercion signatures. Instead of evaluating isolated keywords, it tracks the call's psychological threat progression across six sequential stages: <i>Greeting -> Authority Claim -> Fear Creation -> Isolation Instructions -> Payment Demand -> Completed Scam</i>. Logistic Regression trained on term-frequency inverse document frequency (TF-IDF) vectors was selected as the primary classifier because it yields transparent, inspectable feature weights suitable for forensic court reporting, with Google Gemini LLM acting as a semantic reasoning fallback.",
        body_style
    ))

    story.append(Paragraph("B. VoiceGuard Agent (Speech AI & Voice Spoofing Forensics)", h2_style))
    story.append(Paragraph(
        "Synthesized AI voices and cloned speech generators emit pitch contours with abnormally low jitter and shimmer variance due to smooth mathematical rendering. VoiceGuard extracts acoustic speech features including Pitch Variance (Hz), Vocal Jitter percentage, Vocal Shimmer percentage, and Spectral Centroid Standard Deviation. Lightweight handcrafted speech signal analysis features were chosen for computational efficiency and explainability on field hardware. OpenCV was utilized for supporting visual checksheet validation in the NoteGuard module.",
        body_style
    ))

    story.append(Paragraph("C. CitizenShield Agent (Multi-Lingual Citizen Advisor)", h2_style))
    story.append(Paragraph(
        "CitizenShield provides real-time fraud risk assessments for citizen inquiries across four supported regional languages: English, Hindi, Telugu, and Tamil, with an architectural roadmap designed to scale to 12 regional languages. When a suspicious call or message is evaluated, the agent formats a structured incident draft matching the National Cyber Crime Reporting Portal (NCRP) complaint workflow for seamless submission.",
        body_style
    ))

    story.append(Paragraph("D. NoteGuard Agent (Computer Vision Banknote Checksheet)", h2_style))
    story.append(Paragraph(
        "NoteGuard evaluates physical currency notes using explicit visual checksheet parameters: 1) Security Thread Continuity (green column continuity profiling), 2) Watermark and Microprint Sharpness (Laplacian variance under noise), 3) UV Fluorescence Balance (color channel ratio analysis), and 4) Serial Prefix Regex Validation. Random Forest classification was selected for structured handcrafted features, supplemented by a Convolutional Neural Network (CNN) deep learning fallback model.",
        body_style
    ))

    story.append(Paragraph("E. FraudGraph Agent (Money Mule Ring Clustering & Evidence)", h2_style))
    story.append(Paragraph(
        "FraudGraph models financial transactions using a NetworkX MultiDiGraph, where nodes represent bank accounts, phone numbers, device fingerprints, and complaint IDs. The agent automatically extracts ego-network subgraphs surrounding suspicious hub accounts, exposing coordinated money mule rings and generating court-admissible evidence dossiers detailing total laundering volume and shared device linkages.",
        body_style
    ))

    story.append(Paragraph("F. GeoWatch Agent (GIS Hotspot Prioritization & LEA Routing)", h2_style))
    story.append(Paragraph(
        "GeoWatch computes district-level threat indices by fusing incident frequency, financial loss metrics, and active complaint clusters. It renders interactive Leaflet HTML heatmaps for command center monitoring and outputs prioritized patrol routing instructions for law enforcement deployment.",
        body_style
    ))

    # Risk Fusion & Cryptographic Audit Ledger
    story.append(Paragraph("5. MULTI-SOURCE RISK FUSION & CRYPTOGRAPHIC LEDGER", h1_style))
    
    # Callout Box for Fusion Math
    fusion_box_data = [[
        Paragraph(
            "<b>Multi-Source Threat Risk Score Fusion Formula:</b><br/><br/>"
            "&nbsp;&nbsp;&nbsp;&nbsp;<b>FusedScore = 0.40 * TextNLP + 0.20 * VoiceAcoustics + 0.20 * GraphMule + 0.20 * GeoHotspot</b><br/><br/>"
            "<b>Weight Rationale:</b> Text NLP receives 40% as the primary intent vector expressing scam coercion. Voice Acoustics (20%), Fraud Graph (20%), and Geospatial Context (20%) serve as supporting forensic vectors, preventing false alarms from single-source anomalies.",
            callout_style
        )
    ]]
    fb = Table(fusion_box_data, colWidths=[504])
    fb.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), BG_LIGHT),
        ('BOX', (0, 0), (-1, -1), 1, SECONDARY),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(fb)
    story.append(Spacer(1, 8))

    story.append(Paragraph("Cryptographic Audit Ledger & Section 65B Evidentiary Alignment", h2_style))
    story.append(Paragraph(
        "To guarantee legal admissibility and auditability, all system operations, threat alerts, and approved FIR drafts are sealed into a SHA-256 cryptographically chained ledger where Hash_n = SHA256(Event_n + Hash_n-1). Any historical alteration breaks the signature chain, guaranteeing data integrity. Automated enforcement actions remain hardlocked under Human-in-the-Loop (HITL) workflows pending human officer sign-off in the CLI menu, fulfilling transparency and evidentiary requirements aligned with Section 65B of the Indian Evidence Act.",
        body_style
    ))

    # Model Evaluation Metrics
    story.append(Paragraph("6. MODEL PERFORMANCE & DATASET EVALUATION", h1_style))
    story.append(Paragraph(
        "To test robustness under real-world conditions, models were evaluated against datasets containing transcription typos, Hinglish phrasing, printing noise, and borderline benign warnings:",
        body_style
    ))

    eval_table_data = [
        [
            Paragraph("Model Subsystem", table_header_style),
            Paragraph("Accuracy", table_header_style),
            Paragraph("Precision", table_header_style),
            Paragraph("Recall", table_header_style),
            Paragraph("False Positive Rate", table_header_style)
        ],
        [
            Paragraph("<b>ScamClassifier (NLP)</b>", table_cell_style),
            Paragraph("88.89%", table_cell_style),
            Paragraph("92.3%", table_cell_style),
            Paragraph("88.9%", table_cell_style),
            Paragraph("11.1%", table_cell_style)
        ],
        [
            Paragraph("<b>CurrencyDetector (CV)</b>", table_cell_style),
            Paragraph("88.89%", table_cell_style),
            Paragraph("85.7%", table_cell_style),
            Paragraph("85.7%", table_cell_style),
            Paragraph("9.1%", table_cell_style)
        ]
    ]

    et = Table(eval_table_data, colWidths=[130, 90, 90, 90, 104])
    et.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, BG_LIGHT]),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(et)
    story.append(Spacer(1, 10))

    # Generated Outputs Inventory
    story.append(Paragraph("7. TANGIBLE GENERATED OUTPUTS INVENTORY", h1_style))
    story.append(Paragraph(
        "Every execution of the multi-agent pipeline generates auditable output artifacts in standard formats:",
        body_style
    ))

    out_table_data = [
        [Paragraph("File Path", table_header_style), Paragraph("Artifact Description & Contents", table_header_style)],
        [Paragraph("<b>reports/intelligence_report.json</b>", table_cell_style), Paragraph("Full structured multi-agent intelligence package.", table_cell_style)],
        [Paragraph("<b>reports/intelligence_report.txt</b>", table_cell_style), Paragraph("Human-readable executive summary formatted for law enforcement officers.", table_cell_style)],
        [Paragraph("<b>reports/audit_log.csv</b>", table_cell_style), Paragraph("SHA-256 cryptographically chained audit trail ledger.", table_cell_style)],
        [Paragraph("<b>outputs/maps/hotspot_map.html</b>", table_cell_style), Paragraph("Interactive Leaflet crime heatmap for command center monitoring.", table_cell_style)],
        [Paragraph("<b>outputs/graphs/fraud_network.png</b>", table_cell_style), Paragraph("Fraud-ring network graph visualization.", table_cell_style)],
        [Paragraph("<b>outputs/predictions/counterfeit_report.json</b>", table_cell_style), Paragraph("Per-note forensic breakdown detailing checksheet feature failures.", table_cell_style)],
        [Paragraph("<b>outputs/predictions/ncrp_report.txt</b>", table_cell_style), Paragraph("NCRP-style cybercrime incident report draft.", table_cell_style)]
    ]

    ot = Table(out_table_data, colWidths=[190, 314])
    ot.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, BG_LIGHT]),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(ot)
    story.append(Spacer(1, 10))

    # Official References & Sources
    story.append(Paragraph("8. OFFICIAL REFERENCES & DATA SOURCES", h1_style))
    refs = [
        "1. <b>National Cyber Crime Reporting Portal, Ministry of Home Affairs, Government of India.</b> Reference model for complaint workflows. https://cybercrime.gov.in",
        "2. <b>Indian Cyber Crime Coordination Centre (I4C), Ministry of Home Affairs.</b> Cybercrime infrastructure context. https://i4c.mha.gov.in",
        "3. <b>Reserve Bank of India. (2025). Annual Report 2024-25: Currency Management.</b> Currency context and counterfeit trends. https://www.rbi.org.in",
        "4. <b>Indian Computer Emergency Response Team (CERT-In), MeitY.</b> Incident response advisories. https://www.cert-in.org.in",
        "5. <b>National Crime Records Bureau (NCRB), Ministry of Home Affairs.</b> Cybercrime data reporting. https://ncrb.gov.in",
        "6. <b>Google Gemini API Documentation.</b> Semantic reasoning fallback integration. https://ai.google.dev/gemini-api/docs",
        "7. <b>OpenCV Foundation Documentation.</b> Computer vision image checksheet validation. https://docs.opencv.org",
        "8. <b>NetworkX Developers Documentation.</b> Graph analytics and mule ring mapping. https://networkx.org/documentation/stable/"
    ]
    for r in refs:
        story.append(Paragraph(r, bullet_style))

    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "<b>Prototype Scope Disclaimer:</b> The prototype models are evaluated using synthetic and simulated datasets due to the limited public accessibility of live digital arrest scam, CDR, banking, and counterfeit currency datasets. The system is designed as a decision-support prototype and not as a legally certified enforcement tool.",
        callout_style
    ))

    # Build Document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[SUCCESS] Detailed technical PDF report generated at: {pdf_path}")

    # Copy to assets as well
    assets_pdf_path = r"D:\Ai Public Safety\assets\detailed_project_report.pdf"
    os.makedirs(os.path.dirname(assets_pdf_path), exist_ok=True)
    with open(pdf_path, 'rb') as f_src:
        with open(assets_pdf_path, 'wb') as f_dst:
            f_dst.write(f_src.read())
    print(f"[SUCCESS] Copied detailed technical PDF report to assets: {assets_pdf_path}")

if __name__ == "__main__":
    create_detailed_pdf()
