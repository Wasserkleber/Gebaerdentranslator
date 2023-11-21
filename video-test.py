from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import Start

path = r"C:\Gebaerdenstuff\dgs_woerterbuch_gesamt\Gebaerden\video" #path to the Gebaerdensprachen video files


input = Start.STT()
print("das ist der input:", input)
word_list_raw = input[3]
word_list = word_list_raw.split()



"""
word_list_raw = "auto bombe"
word_list = word_list_raw.split()
"""


clip_list = []
saved_clips = {}
all_clips_found = True


for word in word_list:                                  #Load clips into memory
    if word in saved_clips:

        clip = clip_list[word]
        
    else:
        try:
            clip = VideoFileClip(os.path.join(path, word + ".mp4"))
            saved_clips[word] = clip
        except:
            all_clips_found = False
        

    clip_list.append(clip)                                      



if all_clips_found == False:
    print("One of the words didn't exist")
else:
    final_clip = concatenate_videoclips(clip_list)
    final_clip.write_videofile("my_concatenation.mp4")



