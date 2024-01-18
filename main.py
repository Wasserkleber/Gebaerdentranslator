import cv2
from speech_to_text import speech_to_text
from set_the_words_to_default import lemmatize_sogularize_words
from Test_for_underscore import test
import tkinter as tk

filepath = r"C:\Gebaerdenstuff\dgs_woerterbuch_gesamt\Gebaerden\video"
filepathrecording = r"C:\Gebaerdenstuff\Recording.txt"


def play_multiple_videos(video_paths):
    for video_path in video_paths:
        cap = cv2.VideoCapture(video_path)
        cap.set(cv2.CAP_PROP_FPS, 25)   

        if not cap.isOpened():
            print(f"Error opening video file: {video_path}")
            continue

        cv2.namedWindow('Video Player', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Video Player', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        while cap.isOpened():
            ret, frame = cap.read()

            if ret:
                cv2.imshow('Video Player', frame)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()

    cv2.destroyAllWindows()
    

def main(wordlist_from_ui = None):
    print(wordlist_from_ui)
    while True:
        if wordlist_from_ui == None:
            wordlist_raw = speech_to_text()
            #print(wordlist_raw)
        else:
            wordlist_raw = wordlist_from_ui
            
        #wordlist_raw = "ab jetzt und zu dann"
        wordlist = wordlist_raw.split()
        print(wordlist)
        wordlist = lemmatize_sogularize_words(wordlist)
        wordlist = test(wordlist)
        print("die list ist:", wordlist)

        file_paths = []
        for word in wordlist:
            file_path = f"{filepath}\\{word}.mp4"
            file_paths.append(file_path)
    
        # Print the file paths
        for path in file_paths:
            print(path)
            
        with open("Recording.txt", "w") as datei:
            for element in file_paths:
                datei.write(element + "\n")
        

        play_multiple_videos(file_paths)
        break


def playRecording():
    

    with open(filepathrecording, "r") as datei:
        recording_paths = datei.readlines()
    recording_paths = [zeile.strip() for zeile in recording_paths]

    
    play_multiple_videos(recording_paths)



