from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
from Start import speach_to_text

path = r"D:\Dokumente\Schule\Klasse 10\Franzosisch\forschung\dgs_vids\video" #path to the Gebaerdensprachen video files

"""
input:str = speach_to_text()
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
            print(word)


clip_list = []
saved_clips = {}
all_clips_found = True


for word in word_list:                                  #Load clips into memory
    if word in saved_clips:
        clip = clip_list[clip_list.index[word]]
        
    else:
        try:
            clip = VideoFileClip(os.path.join(path, word + ".mp4"))
            saved_clips[word] = clip

        except RuntimeError as e:
            print(e)
            raise RuntimeError(f'One of the words did not exist: {word}')
        

    clip_list.append(clip)                                      


final_clip = concatenate_videoclips(clip_list)
final_clip.write_videofile("output.mp4")
