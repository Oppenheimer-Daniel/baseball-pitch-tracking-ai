import cv2
import os

def extract_frames():
    video_path = os.path.join('data', 'raw_video', 'sample_pitch.mp4')
    output_folder = os.path.join('data', 'training_frames')
    
    # Ensure the folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created folder: {output_folder}")
        
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Could not find video at {video_path}")
        return

    count = 0
    print("Extracting frames... please wait.")
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # Naming convention: project_source_frameNumber
        file_name = f"pitch_A_{count:05d}.jpg"
        file_path = os.path.join(output_folder, file_name)
        
        cv2.imwrite(file_path, frame)
        count += 1
        
    cap.release()
    print(f"Done! {count} images saved to {output_folder}")

if __name__ == "__main__":
    extract_frames()