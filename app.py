import cv2
import pafy
import os
import time
from googletrans import Translator

def download_video(youtube_url):
    video = pafy.new(youtube_url)
    best = video.getbest(preftype="mp4")
    best.download(filepath="video.mp4")

def process_video():
    cap = cv2.VideoCapture("video.mp4")
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    count = 0
    translator = Translator()

    while cap.isOpened():
        frame_id = cap.get(cv2.CAP_PROP_POS_FRAMES)
        ret, frame = cap.read()

        if not ret:
            break

        if frame_id % int(frame_rate) == 0:
            file_name = f"frame{count}.jpg"
            cv2.imwrite(file_name, frame)
            summary = summarize_frame(file_name)
            translated_summary = translator.translate(summary, dest='en')
            print(f"Frame {count}: {translated_summary.text}")
            count += 1

    cap.release()

def summarize_frame(frame_file):
    # Replace this with your image recognition or frame analysis logic
    return "Something happens in this frame."

if __name__ == "__main__":
    youtube_url = "YOUR_YOUTUBE_VIDEO_URL"
    download_video(youtube_url)
    time.sleep(5)  # Ensure the video is fully downloaded
    process_video()
