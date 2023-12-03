from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
from speech_to_text import speech_to_text
import cv2

path = r"D:\Dokumente\Schule\Klasse 10\Franzosisch\forschung\dgs_vids\video" #path to the Gebaerdensprachen video files



"""
#speech to text
input:str = speech_to_text()
word_list = input.split()
print(f'speach_to_text word_list: {word_list}')
"""
word_list_raw = "auto und reifen"
word_list = word_list_raw.split()



#first check for simple blacklisted words
with open('blacklist_words_dgs.txt') as f:
    blacklist = f.read().split('\n')
    for word in word_list:
        if(word in blacklist):
            word_list.remove(word)



#Load clips into memory
clip_list = []
saved_clips = {}
all_clips_found = True

for word in word_list:
    if word in saved_clips:
        clip = clip_list[clip_list.index[word]]
        
    else:
        try:
            clip = os.path.join(path, word + ".mp4")
            saved_clips[word] = clip

        except RuntimeError as e:
            print(e)
            raise RuntimeError(f'One of the words did not exist: {word}')
        

    clip_list.append(clip)                                      



#play video
cap = cv2.VideoCapture(clip_list[0])
i = 1
if (cap.isOpened() == False):
    print("Error opening video stream or file")
while (cap.isOpened()):
    
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow(f'{word_list}', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        #here, you can add videos to the playback queue
    else:
        try:
            cap = cv2.VideoCapture(clip_list[i])
            i+=1
        except:
            break
cap.release()
cv2.destroyAllWindows()

os.remove('output.mp4')