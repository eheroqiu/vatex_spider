import subprocess
import json
from moviepy.editor import *
import glob 
with open("train_id_data.json", 'r')as f:
    a = json.load(f)
    for i in a:
        subprocess.run("youtube-dl https://www.youtube.com/watch?v=" + i['v_id'] + " -o " + i['v_id'] + "."+ "'%(ext)s'",shell=True)
        try:
            for k in glob.glob(i['v_id']+".*"):
                clip1 = VideoFileClip(k).subclip(i['start_ts'],i['end_ts'])
                clip1.write_videofile(i['v_id'] + "_Cut_10s.mp4",fps=60,codec='mpeg4')
                subprocess.run("rm -f " + k , shell=True)
        except:
            for k in glob.glob(i['v_id']+".*"):
                subprocess.run("rm -f " + k , shell=True)
        else:
            print("fine, that's ok!")


