# Video_to_MP3
Python tool for extracting audio tracks from online video sources. 



A simple Python tool that downloads online videos and extracts their audio track as an MP3 file.  
The script uses `yt-dlp` and FFmpeg to fetch the best available audio and convert it to MP3.

-- Features
- Download video from a provided URL
- Extract audio using FFmpeg
- Save output as MP3 
- Custom output template (`~/Downloads/<title>.mp3`)
- Custom HTTP headers and YouTube extractor arguments

-- Installation

1. Install yt-dlp:
   pip install yt-dlp
   
3. Install FFmpeg:
   /opt/homebrew/bin/ffmpeg
   (Change the path if needed)
   
4. How to use:
   Paste one or more links into "urls" list

All files will be saved in downloads folder

DISCLAIMER
This tool is intended for personal and educational use only.
Users are responsible for ensuring they have the rights to download and convert the content they process.

   


