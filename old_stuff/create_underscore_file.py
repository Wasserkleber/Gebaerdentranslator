import os


def get_video_names_with_underscore(folder_path):
    # Get the list of files in the specified folder
    files = os.listdir(folder_path)

    # Filter files with underscore in the name
    video_names_with_underscore = [file for file in files if '_' in file]

    return video_names_with_underscore

def write_to_txt(file_names, output_file):
    with open(output_file, 'w') as txt_file:
        for file_name in file_names:
            txt_file.write(file_name + '\n')

if __name__ == "__main__":
    # Replace 'your_folder_path' with the path to the folder containing your videos
    folder_path = r'C:\Users\Schüler\Desktop\Gebaerdenstuff\dgs_woerterbuch_gesamt\Gebaerden\video'

    # Replace 'output.txt' with the desired name of the output text file
    output_file = 'output.txt'

    video_names_with_underscore = get_video_names_with_underscore(folder_path)

    if video_names_with_underscore:
        print("Video names with underscore found:")
        for video_name in video_names_with_underscore:
            print(video_name)
        
        write_to_txt(video_names_with_underscore, output_file)
        print(f"\nNames written to {output_file}")
    else:
        print("No video names with underscore found in the specified folder.")