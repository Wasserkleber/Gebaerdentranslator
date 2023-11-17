from moviepy.editor import VideoFileClip, concatenate_videoclips
import time  
path = "" #path to the Gebärdensprachen video files

input = "World Hello"
word_list = input.split()
print(word_list)
word_list = [item.lower() for item in word_list]
print(word_list)


clip_list = []
saved_clips = {}
start_time = time.time()



for word in word_list:
    if word in saved_clips:
        clip = clip_list[word]
    else:
        clip = VideoFileClip("" + word + ".mp4")
        saved_clips[word] = clip

    clip_list.append(clip)




final_clip = concatenate_videoclips(clip_list)
final_clip.write_videofile("my_concatenation.mp4")



# print(f"initialise clips: {cliped_time - start_time}    cocatenate clips: {final_clip_time - cliped_time} last one: {final_final_clip_time - final_clip_time}")
