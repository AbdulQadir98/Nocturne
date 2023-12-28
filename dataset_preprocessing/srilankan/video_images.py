import cv2
import os
import shutil

def extract_frames(video_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    frame_number = 0
    seconds = 0
    minutes = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_number += 1
        seconds = frame_number // 30  # Assuming 30 FPS, adjust if needed
        minutes = seconds // 60
        seconds %= 60

        if frame_number % 30 == 1:
            frame_number_in_second = 0

        frame_number_in_second += 1

        frame_filename = os.path.join(output_folder, f"{minutes:02d}_{seconds:02d}_{frame_number_in_second:06d}.png")
        cv2.imwrite(frame_filename, frame)

        if minutes % 1 == 0 and frame_number_in_second % 2 != 0:
            # Delete images not divisible by 2
            os.remove(frame_filename)
        
    cap.release()

if __name__ == "__main__":
    input_video = "pedestrian_galle_vid_13.mov"
    output_folder = "frames_output"

    os.makedirs(output_folder, exist_ok=True)

    extract_frames(input_video, output_folder)

    print("Frames extracted and saved.")
