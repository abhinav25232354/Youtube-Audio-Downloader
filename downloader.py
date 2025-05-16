import os
import yt_dlp

# Create 'songs' directory if it doesn't exist
output_folder = "songs"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Input YouTube URL
url = input("Enter YouTube video URL: ")

# Set download options
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'noplaylist': True,
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Download complete!")
except Exception as e:
    print("Error:", e)
