# Converts the video to mp3

import os
import subprocess

files = os.listdir("Videos")
for file in files:
    # print(file)
    # tutorial_number = file.split("(")[0].split("#")[1]
    tutorial_number = file.split("_")[0]
    # print(tutorial_number)
    # file_name = file.split("__")[0].replace("_", " ")
    file_name = file.split("_")[1].split("-Sigma")[0].replace("-", " ")
    print(tutorial_number, file_name)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])