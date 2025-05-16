import os  # os module helps in system fle handling and system management
import yt_dlp # This module helps in dealing with stuffs related to youtube

# This Program helps in downloading youtube video's audios without any API (Application Programming Interface)

# Create 'songs' directory if it doesn't exist
output_folder = "songs" # Songs folder will include all the downloaded tracks
if not os.path.exists(output_folder): # If folder doesn't exists
    os.makedirs(output_folder) # Make new folder named "songs/"

# Set download options
ydl_opts = { # Parameters of the variable ydl_opts
    'format': 'bestaudio/best', # format, beat audio/best (It will select highest qualioty audio avalable for the video)
    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'), # for showing title of the synchronized link of the video
    'postprocessors': [{ # Post processor will convert extracted audio to mp3 for best and efficient compatibility
        'key': 'FFmpegExtractAudio', # It is showing a key value pair which consist of key and the value
        'preferredcodec': 'mp3', # It shows destination format which is mp3
        'preferredquality': '320', # It show prefered quality (This program will search for 320k audio first)
    }],
    'noplaylist': True, # It shows no allowance for playlist download
} # Closing bracket for the function
 
while True: # Always runnign infinite loop
    # Input YouTube URL
    url = input("Enter YouTube video URL (or type 'q' to quit): ").strip() # Input from user for the URL for the youtube
    
    if url.lower() == 'q': # It checks userr input is q or not and then convert that q into lowercase for consistency
        print("Exiting...") # It prints existing whenever user tells to quit with using print function
        break # Break the loop when condition is true (When user wants to exit)

    try: # Try Block for prevention of error occurance
        with yt_dlp.YoutubeDL(ydl_opts) as ydl: # For file handling for downloading and saving songs in directory
            print(f"Downloading: {url}") # Print Downloading when process is occurring
            ydl.download([url]) # Download the Video linked with URL
        print("Download complete!") # Download Complete (Process Done Successfully)
    except Exception as e: # Exception Block where errors are handled
        print(f"Error: {e}")  # Print Error if any
