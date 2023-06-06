import os
from moviepy.editor import VideoFileClip



# This script is used to remove audio from MP4 files in bulk.
# Set the input_path variable to the path of the file where the mp4 files are.
# Set the output_path variable to the path of the folder where you want the new mp4 files with no audio to go.



# path to the directory with the MP4 files you wish to remove audio from
input_path = os.path.join(os.getcwd(), 'videos-with-audio')
output_path = os.path.join(os.getcwd(), 'videos-with-no-audio')
os.makedirs(input_path, exist_ok=True)
os.makedirs(output_path, exist_ok=True) 

mp4_files = []

# Get all mp4 files in the directory and append them to the mp4_files list
for file in os.listdir(input_path):
    if file.endswith('.mp4'):
        mp4_path = os.path.join(input_path, file)
        mp4_files.append(mp4_path)
   
if len(mp4_files) == 0:
    print("You need to put MP4 files into the input_path folder!")   

# Loop over each mp4 file in the mp4_files list
counter = 0
for mp4_file in mp4_files:
    counter = counter + 1

    # Load the mp4 file using the VideoFileClip function
    clip = VideoFileClip(mp4_file)

    # Remove the audio from the clip
    clip = clip.without_audio()

    # Create a new file name with "no-audio" added to it
    new_file_name = os.path.splitext(os.path.basename(mp4_file))[0] + "-no-audio.mp4"

    # Write the new clip with no audio to the new directory with the new file name
    clip.write_videofile(os.path.join(output_path, new_file_name))
    
    # Close the clip to free up resources
    print("\n")
    print("Audio removed from file #" + str(counter) + " of " + str(len(mp4_files)))
    print("\n")
    clip.close()

