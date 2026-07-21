import os
import cv2
import numpy as np

def draw_card(img, pt1, pt2, bg_color, border_color=None, border_thickness=1):
    cv2.rectangle(img, pt1, pt2, bg_color, -1)
    if border_color is not None:
        cv2.rectangle(img, pt1, pt2, border_color, border_thickness)

def generate_demo_video():
    video_path = r"D:\Ai Public Safety\assets\demo_video.mp4"
    os.makedirs(os.path.dirname(video_path), exist_ok=True)
    
    width, height = 1280, 720
    fps = 30
    duration_per_scene = 3.5  # seconds per slide
    num_scenes = 6
    total_duration = duration_per_scene * num_scenes  # 21 seconds total
    num_frames = int(fps * total_duration)
    frames_per_scene = int(fps * duration_per_scene)
    
    # mp4v video writer for standard MP4 playback on Windows/Linux/Mac
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))
    
    # Color palette (BGR format for OpenCV)
    BG_DARK = (26, 20, 15)        # Dark Indigo Navy
    CARD_BG = (42, 33, 22)        # Deep card background
    TEXT_WHITE = (255, 255, 255)
    TEXT_MUTED = (203, 213, 225)
    CRIMSON = (94, 63, 244)       # Neon Crimson/Red
    CYAN = (212, 182, 6)          # Cyan
    GREEN = (129, 185, 16)        # Emerald Green
    GOLD = (11, 158, 245)         # Gold
    BORDER_BLUE = (100, 70, 40)

    for i in range(num_frames):
        scene_idx = min(int(i / frames_per_scene), num_scenes - 1)
        frame_in_scene = i % frames_per_scene
        scene_progress = frame_in_scene / frames_per_scene
        
        # Base canvas frame
        img = np.zeros((height, width, 3), dtype=np.uint8)
        img[:] = BG_DARK
        
        # Top Header Bar
        cv2.rectangle(img, (0, 0), (width, 70), (35, 25, 18), -1)
        cv2.line(img, (0, 70), (width, 70), CYAN, 2)
        cv2.putText(img, "AI FOR DIGITAL PUBLIC SAFETY PLATFORM", (30, 45),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, TEXT_WHITE, 2)
        cv2.putText(img, "MULTI-AGENT INTELLIGENCE PIPELINE DEMO", (820, 45),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, CYAN, 1)

        # Bottom Status Bar
        cv2.rectangle(img, (0, height - 40), (width, height), (35, 25, 18), -1)
        cv2.line(img, (0, height - 40), (width, height - 40), BORDER_BLUE, 1)
        
        # Progress Bar
        bar_w = int((i / num_frames) * (width - 60))
        cv2.rectangle(img, (30, height - 20), (30 + bar_w, height - 10), CYAN, -1)
        cv2.putText(img, f"SLIDE {scene_idx + 1}/{num_scenes} | FRAME {i+1}/{num_frames} | SECTION 65B-ALIGNED FORENSICS", (30, height - 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, TEXT_MUTED, 1)
        
        # Render scene content
        if scene_idx == 0:
            # SCENE 1: Title & Platform Overview
            draw_card(img, (100, 110), (1180, 640), CARD_BG, CRIMSON, 2)
            cv2.putText(img, "AI DIGITAL PUBLIC SAFETY INTELLIGENCE PLATFORM", (140, 165),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.95, CRIMSON, 3)
            cv2.putText(img, "Detecting Digital Arrest Scams, Voice Deepfakes, Counterfeit Currency & Fraud Networks", (140, 205),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, TEXT_MUTED, 1)
            
            # Agent grid
            agents = [
                "1. ScamShield Agent (NLP/LLM)", "2. VoiceGuard Agent (Speech AI)",
                "3. CitizenShield Agent (Chatbot)", "4. NoteGuard Agent (Rupee CV)",
                "5. FraudGraph Agent (Mule Rings)", "6. GeoWatch Agent (GIS Hotspots)",
                "7. Orchestrator Agent (Risk Fusion)", "8. Audit Logger (SHA-256 Ledger)"
            ]
            for idx, a_name in enumerate(agents):
                row = idx // 2
                col = idx % 2
                x = 140 + col * 490
                y = 250 + row * 85
                draw_card(img, (x, y), (x + 460, y + 65), (50, 40, 28), CYAN, 1)
                cv2.putText(img, a_name, (x + 20, y + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, TEXT_WHITE, 2)

        elif scene_idx == 1:
            # SCENE 2: ScamShield Agent (Digital Arrest NLP)
            draw_card(img, (50, 95), (1230, 650), CARD_BG, CYAN, 2)
            cv2.putText(img, "MODULE 1: ScamShield Agent — Digital Arrest NLP Classifier", (80, 135),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.85, CYAN, 2)
            
            # Left panel: Transcript Audit
            draw_card(img, (80, 165), (620, 520), (30, 22, 16), BORDER_BLUE, 1)
            cv2.putText(img, "INCOMING CALL TRANSCRIPT AUDIT", (100, 195), cv2.FONT_HERSHEY_SIMPLEX, 0.55, GOLD, 2)
            lines = [
                "\"I am calling from CBI Delhi HQ.",
                "Your Aadhaar is linked to money laundering.",
                "Stay on video call in isolation room.",
                "Transfer Rs 50,000 to safe RBI account",
                "or police will arrive immediately.\""
            ]
            for ly_idx, line in enumerate(lines):
                cv2.putText(img, line, (100, 240 + ly_idx * 35), cv2.FONT_HERSHEY_SIMPLEX, 0.52, TEXT_WHITE, 1)
            
            # Right panel: Explainable Coercion Indicators
            draw_card(img, (650, 165), (1200, 520), (30, 22, 16), BORDER_BLUE, 1)
            cv2.putText(img, "EXPLAINABLE COERCION INDICATORS", (670, 195), cv2.FONT_HERSHEY_SIMPLEX, 0.55, CRIMSON, 2)
            
            indicators = [
                ("Authority Impersonation (CBI/ED)", 0.98),
                ("Psychological Hostage Threat", 0.94),
                ("Mandatory Video Isolation", 0.91),
                ("Coerced Account Transfer Prompt", 0.96)
            ]
            for ind_idx, (ind_name, score) in enumerate(indicators):
                y = 245 + ind_idx * 55
                cv2.putText(img, ind_name, (670, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, TEXT_WHITE, 1)
                bw = int(score * 180 * min(1.0, scene_progress * 1.5))
                cv2.rectangle(img, (970, y - 18), (970 + bw, y - 2), CRIMSON, -1)
                cv2.putText(img, f"{int(score*100)}%", (1160, y), cv2.FONT_HERSHEY_SIMPLEX, 0.48, CRIMSON, 1)

            # Timeline bar at bottom
            cv2.putText(img, "THREAT PROGRESSION: Greeting -> Authority -> Isolation [ACTIVE] -> Payment Demand", (80, 575),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.58, GOLD, 2)

        elif scene_idx == 2:
            # SCENE 3: VoiceGuard & NoteGuard Forensics
            draw_card(img, (50, 95), (1230, 650), CARD_BG, GREEN, 2)
            cv2.putText(img, "MODULE 2 & 3: VoiceGuard & NoteGuard Forensics", (80, 135),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.85, GREEN, 2)
            
            # Left: VoiceGuard
            draw_card(img, (80, 165), (620, 620), (30, 22, 16), BORDER_BLUE, 1)
            cv2.putText(img, "VOICEGUARD (SPEECH AI BIOMETRICS)", (100, 205), cv2.FONT_HERSHEY_SIMPLEX, 0.6, CYAN, 2)
            cv2.putText(img, "Vocal Jitter: 0.02% (Synthetic Low)", (100, 255), cv2.FONT_HERSHEY_SIMPLEX, 0.52, TEXT_WHITE, 1)
            cv2.putText(img, "Vocal Shimmer: 0.11% (Flat Envelope)", (100, 295), cv2.FONT_HERSHEY_SIMPLEX, 0.52, TEXT_WHITE, 1)
            cv2.putText(img, "Pitch Std Dev: 4.2 Hz (Monotone Cloned)", (100, 335), cv2.FONT_HERSHEY_SIMPLEX, 0.52, TEXT_WHITE, 1)
            
            # Waveform graphic
            for w in range(450):
                val = int(25 * np.sin((w + i * 6) * 0.1) * np.exp(-((w-225)**2)/20000))
                cv2.circle(img, (110 + w, 440 + val), 1, CYAN, -1)
            draw_card(img, (100, 520), (600, 585), CRIMSON, -1)
            cv2.putText(img, "VERDICT: SYNTHETIC VOICE CLONE (DEEPFAKE)", (115, 560), cv2.FONT_HERSHEY_SIMPLEX, 0.52, TEXT_WHITE, 2)

            # Right: NoteGuard
            draw_card(img, (650, 165), (1200, 620), (30, 22, 16), BORDER_BLUE, 1)
            cv2.putText(img, "NOTEGUARD (CURRENCY CHECKSHEET)", (670, 205), cv2.FONT_HERSHEY_SIMPLEX, 0.6, GOLD, 2)
            checks = [
                ("Security Thread Continuity", "FAIL (Discontinuous)"),
                ("Watermark Sharpness (Laplacian)", "FAIL (Blurry Print)"),
                ("UV Balance (Green/Blue Ratio)", "FAIL (Non-standard)"),
                ("Serial Prefix Regex Format", "PASS (Valid Format)")
            ]
            for chk_idx, (chk_title, status) in enumerate(checks):
                y = 255 + chk_idx * 55
                cv2.putText(img, chk_title, (670, y), cv2.FONT_HERSHEY_SIMPLEX, 0.48, TEXT_WHITE, 1)
                color = CRIMSON if "FAIL" in status else GREEN
                cv2.putText(img, status, (970, y), cv2.FONT_HERSHEY_SIMPLEX, 0.48, color, 2)
            
            draw_card(img, (670, 520), (1180, 585), CRIMSON, -1)
            cv2.putText(img, "VERDICT: COUNTERFEIT RUPEE NOTE (FAILED)", (690, 560), cv2.FONT_HERSHEY_SIMPLEX, 0.52, TEXT_WHITE, 2)

        elif scene_idx == 3:
            # SCENE 4: FraudGraph & GeoWatch GIS
            draw_card(img, (50, 95), (1230, 650), CARD_BG, GOLD, 2)
            cv2.putText(img, "MODULE 4 & 5: FraudGraph & GeoWatch GIS Routing", (80, 135),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.85, GOLD, 2)
            
            # Left: FraudGraph Ring
            draw_card(img, (80, 165), (620, 620), (30, 22, 16), BORDER_BLUE, 1)
            cv2.putText(img, "FRAUDGRAPH MULE NETWORK RING", (100, 205), cv2.FONT_HERSHEY_SIMPLEX, 0.6, CYAN, 2)
            cv2.putText(img, "Hub Mule Account: MULE_41588", (100, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.52, TEXT_WHITE, 1)
            cv2.putText(img, "Connected Accounts: 14 Nodes", (100, 285), cv2.FONT_HERSHEY_SIMPLEX, 0.52, TEXT_WHITE, 1)
            cv2.putText(img, "Total Laundering Volume: Rs 42.5 Lakhs", (100, 320), cv2.FONT_HERSHEY_SIMPLEX, 0.52, CRIMSON, 2)
            
            # Graph visualization node animation
            center = (350, 440)
            cv2.circle(img, center, 24, CRIMSON, -1)
            cv2.putText(img, "MULE", (327, 446), cv2.FONT_HERSHEY_SIMPLEX, 0.45, TEXT_WHITE, 2)
            for n_idx in range(6):
                ang = n_idx * (2 * np.pi / 6) + scene_progress * 0.5
                nx_pos = int(center[0] + 120 * np.cos(ang))
                ny_pos = int(center[1] + 75 * np.sin(ang))
                cv2.line(img, center, (nx_pos, ny_pos), CYAN, 2)
                cv2.circle(img, (nx_pos, ny_pos), 14, CYAN, -1)

            draw_card(img, (100, 530), (600, 595), CRIMSON, -1)
            cv2.putText(img, "STATUS: FRAUD MULE RING ISOLATED", (140, 570), cv2.FONT_HERSHEY_SIMPLEX, 0.52, TEXT_WHITE, 2)

            # Right: GeoWatch GIS Hotspots
            draw_card(img, (650, 165), (1200, 620), (30, 22, 16), BORDER_BLUE, 1)
            cv2.putText(img, "GEOWATCH CRIME HOTSPOT RANKING", (670, 205), cv2.FONT_HERSHEY_SIMPLEX, 0.6, GOLD, 2)
            
            districts = [
                ("1. New Delhi District", "CRITICAL", "Rs 1.2 Crore Loss"),
                ("2. Mumbai Suburban", "HIGH", "Rs 85 Lakhs Loss"),
                ("3. Bengaluru Urban", "HIGH", "Rs 72 Lakhs Loss"),
                ("4. Hyderabad District", "MEDIUM", "Rs 45 Lakhs Loss")
            ]
            for dist_idx, (d_name, level, loss) in enumerate(districts):
                y = 255 + dist_idx * 55
                cv2.putText(img, d_name, (670, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, TEXT_WHITE, 1)
                color = CRIMSON if level == "CRITICAL" else GOLD if level == "HIGH" else GREEN
                cv2.putText(img, level, (950, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                cv2.putText(img, loss, (1050, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, TEXT_MUTED, 1)

            draw_card(img, (670, 530), (1180, 595), GREEN, -1)
            cv2.putText(img, "PATROL DISPATCH: LEA ROUTING GENERATED", (690, 570), cv2.FONT_HERSHEY_SIMPLEX, 0.52, TEXT_WHITE, 2)

        elif scene_idx == 4:
            # SCENE 5: Orchestrator & Cryptographic Audit Ledger
            draw_card(img, (50, 95), (1230, 650), CARD_BG, CRIMSON, 2)
            cv2.putText(img, "MODULE 6 & 7: Orchestrator & Cryptographic Audit Ledger", (80, 135),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.85, CRIMSON, 2)
            
            # Risk Fusion Card
            draw_card(img, (80, 165), (1200, 360), (30, 22, 16), BORDER_BLUE, 1)
            cv2.putText(img, "MULTI-SOURCE RISK FUSION FORMULA", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.6, GOLD, 2)
            cv2.putText(img, "FusedScore = 0.40(TextNLP) + 0.20(VoiceAcoustics) + 0.20(GraphMule) + 0.20(GeoHotspot)", (100, 240),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, CYAN, 2)
            
            scores = [("Text 40%", "92%"), ("Voice 20%", "88%"), ("Graph 20%", "85%"), ("Geo 20%", "80%")]
            for s_idx, (lbl, val) in enumerate(scores):
                x = 100 + s_idx * 265
                draw_card(img, (x, 270), (x + 235, 335), (50, 38, 26), BORDER_BLUE, 1)
                cv2.putText(img, f"{lbl}: {val}", (x + 35, 308), cv2.FONT_HERSHEY_SIMPLEX, 0.58, TEXT_WHITE, 2)

            # Cryptographic Audit Ledger Card
            draw_card(img, (80, 380), (1200, 620), (30, 22, 16), BORDER_BLUE, 1)
            cv2.putText(img, "SHA-256 CRYPTOGRAPHIC AUDIT LEDGER (SECTION 65B-ALIGNED)", (100, 420),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, GREEN, 2)
            cv2.putText(img, "Block #142 Hash: 159fb2b08e22c2bc47cdd1aebf825365b1f1c76a05fef485dfb49c194f697b09", (100, 460),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, TEXT_WHITE, 1)
            cv2.putText(img, "Prev Hash: ad61c2a550c62187719f2a1055f054a87bdd79e9e6fab929470d1ed86ebc13fd", (100, 495),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, TEXT_MUTED, 1)
            cv2.putText(img, "Status: SHA-256 Cryptographic Chain Verified & Untampered", (100, 535),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.52, GREEN, 2)
            cv2.putText(img, "Human-in-the-Loop Officer Sign-off: APPROVED & SIGNED", (100, 575),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.52, GOLD, 2)

        elif scene_idx == 5:
            # SCENE 6: Outro & Submission Ready
            draw_card(img, (100, 110), (1180, 640), CARD_BG, GREEN, 3)
            cv2.putText(img, "PLATFORM 100% DEMO-READY & AUDITABLE", (140, 210),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.1, GREEN, 3)
            cv2.putText(img, "AI for Digital Public Safety Intelligence Platform", (140, 270),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, TEXT_WHITE, 2)
            cv2.putText(img, "Built for Law Enforcement Agencies, Cybercrime Cells & Citizen Safety", (140, 320),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.58, TEXT_MUTED, 1)
            
            draw_card(img, (140, 380), (1140, 470), CRIMSON, -1)
            cv2.putText(img, "GO SUBMIT AND WIN THE HACKATHON! 🏆🚀", (220, 437),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, TEXT_WHITE, 2)
            
            cv2.putText(img, "Repository: github.com/abhranil1113/AI-Public-Safety", (140, 540),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, CYAN, 1)

        out.write(img)

    out.release()
    print(f"[SUCCESS] Enhanced 720p HD Pitch Demo Video successfully generated at: {video_path}")

if __name__ == "__main__":
    generate_demo_video()
