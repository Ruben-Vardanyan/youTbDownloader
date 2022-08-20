from pytube import YouTube
import os
# path here
path = str(input("video path here : "))
#

def audioF(ytb):
    print("processing........")
    video = ytb.streams.filter(only_audio=True).first()
    out_file = video.download(output_path="C:/Users/ruben/Music/my_audios") 

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'

    if os.path.isfile(new_file):
        os.remove(out_file)
        print("failed: the file is already exist")
    else:
        os.rename(out_file, new_file)
        print("success!!!!")
    

def videoF(ytb):
    print("processing........")
    mp4_files = ytb.streams.filter(file_extension="mp4")
    mp4_369p_files = mp4_files.get_highest_resolution() 
    mp4_369p_files.download("C:/Users/ruben/Videos/my_videos")
    print("success!!!!")
    


file_type = ""
while(file_type != "mp3" and file_type != "mp4"):
    file_type = str(input("mp3 or mp4 (default - mp3) : ")) or "mp3"

audio_file_names = []
video_file_names = []
for (dirpath, dirnames, filenames) in os.walk("C:/Users/ruben/Music/my_audios"):
    audio_file_names.extend(filenames)
    break
for (dirpath, dirnames, filenames) in os.walk("C:/Users/ruben/Videos/my_videos"):
    video_file_names.extend(filenames)
    break

yt = YouTube(path)
video_title = yt.title + "." + file_type
print(video_title)
print(audio_file_names)
print(video_file_names)
if video_title in audio_file_names or video_title in video_file_names:
    print("failed: " + video_title + " is already exist")
    if file_type == "mp3": 
        os.startfile("C:/Users/ruben/Music/my_audios")
    else:
        os.startfile("C:/Users/ruben/Videos/my_videos") 
else:
    if file_type == "mp4": 
        os.startfile("C:/Users/ruben/Videos/my_videos")
        videoF(yt) 
    else:
        os.startfile("C:/Users/ruben/Music/my_audios")
        audioF(yt) 















