# extract the audio from video
# pip install ibm_watson
# brew install ffmpeg
from pydub import AudioSegment 
import subprocess


# ffmpeg -i /Users/dean/data-space/test-audio2Chinese.mp4 -ab 160k -ar 44100 -vn audio.wav
# ffmpeg -i /Users/dean/data-space/test-audio2Chinese.mp4 -ab 160k -ar 44100 -vn audio.mp3

def extracter(video_path):
    """
    extract the audio
    """
    command = f'ffmpeg -i {video_path} -ab 160k -ar 44100 -vn audio.wav'
    subprocess.call(command, shell=True)

def segment(audio_path, begin, end, out_path):
    """
    audio_path: audio path
    n: seconds
    """
    begin = begin * 1000
    end = end * 1000
    song = AudioSegment.from_mp3(audio_path) 
    second_songs = song[begin: end]
    second_songs.export(out_path, format="mp3")
    

if __name__ == "__main__":
    # extracter("test-audio2Chinese.mp4")
    segment("audio.mp3", 5 * 60, 13 * 60, "segment-audio-5_13.mp3")