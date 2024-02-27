import cv2
import numpy as np
import os

def find_significant_change(video_path, threshold):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Fehler beim Öffnen des Videos: {video_path}")
        return None

    
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    if frame_rate <= 0:
        frame_rate = 25  

    ret, previous_frame = cap.read()
    if not ret:
        print("Fehler beim Lesen des ersten Frames.")
        return None

    frame_number = 1
    while ret:
        ret, current_frame = cap.read()
        if not ret:
            break

        frame_diff = cv2.absdiff(current_frame, previous_frame)
        non_zero_count = np.count_nonzero(frame_diff)

        print(f"Frame {frame_number}: {non_zero_count} Pixel geändert (Schwellenwert: {threshold})")

        if non_zero_count > threshold:
            cap.release()
            return frame_number / frame_rate  # Verwenden Sie den festgelegten Frame-Rate-Wert

        previous_frame = current_frame
        frame_number += 1  # Inkrementieren des Framezählers


def cut_video_with_opencv(video_path, cut_time):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Fehler beim Öffnen des Videos: {video_path}")
        return

    file_name, file_extension = os.path.splitext(video_path)
    output_path = f"{file_name}_cut{file_extension}"

    # Videoparameter für den Export
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    codec = cv2.VideoWriter_fourcc(*'mp4v')  # Ändern Sie dies entsprechend Ihrem gewünschten Codec
    out = cv2.VideoWriter(output_path, codec, fps, (width, height))

    current_time = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0  # Zeit in Sekunden
        if current_time >= cut_time:
            out.write(frame)

    cap.release()
    out.release()
    os.replace(output_path, video_path)

def process_all_videos_in_folder(folder_path, threshold):
    for file_name in os.listdir(folder_path):
        # Vollständigen Dateipfad erstellen
        file_path = os.path.join(folder_path, file_name)

        # Überprüfen, ob es sich um eine Videodatei handelt (z.B. durch die Dateierweiterung)
        if os.path.isfile(file_path) and file_path.lower().endswith(('.mp4', '.avi', '.mov')):
            print(f"Verarbeite Video: {file_path}")
            
            cut_time = find_significant_change(file_path, threshold)
            if cut_time is not None:
                cut_video_with_opencv(file_path, cut_time)
                print(f"Video wurde bei {cut_time} Sekunden geschnitten.")
            else:
                print("Keine signifikante Änderung gefunden in " + file_path)

# Verzeichnispfad und Schwellenwert festlegen
directory_path = r"C:\Gebaerdenstuff\Test-cutted\Gebaerden\video"
threshold = 1000000

# Alle Videos im Verzeichnis verarbeiten
process_all_videos_in_folder(directory_path, threshold)

