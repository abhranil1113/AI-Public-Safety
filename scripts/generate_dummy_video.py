import os
import cv2
import numpy as np

def generate_placeholder_video():
    video_path = r"D:\Ai Public Safety\assets\demo_video.mp4"
    os.makedirs(os.path.dirname(video_path), exist_ok=True)
    
    # 640x480 resolution, 24 fps
    width, height = 640, 480
    fps = 24
    duration_sec = 3
    num_frames = fps * duration_sec
    
    # Define video writer (mp4v codec works on most Windows machines)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))
    
    for i in range(num_frames):
        # Create a changing color transition frame
        img = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Color shifting
        blue_val = int((i / num_frames) * 255)
        green_val = int(((num_frames - i) / num_frames) * 150)
        red_val = 100
        
        img[:] = [blue_val, green_val, red_val]
        
        # Draw some text
        cv2.putText(img, "AI Public Safety Platform Demo", (40, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(img, "Pitch Video Placeholder", (120, 240), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 1)
        cv2.putText(img, f"Frame {i+1}/{num_frames}", (40, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
        
        out.write(img)
        
    out.release()
    print(f"Placeholder pitch demo video generated at {video_path}")

if __name__ == "__main__":
    generate_placeholder_video()
