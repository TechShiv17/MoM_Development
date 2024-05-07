from pytube import YouTube
import os
from moviepy.editor import VideoFileClip, AudioClip


class VideoDownloader:
    @staticmethod
    def download_audio_from_url(link, output_path):
        try:
            # Create a YouTube object with the URL
            yt = YouTube(link)
            audio = yt.streams.filter(only_audio=True).order_by('abr').asc().first().download()
            os.rename(audio, output_path)

            # Download the video to the specified path
            print("Download completed!")
        except Exception as e:
            print(f"An error occurred: {e}")
        return True

    @staticmethod
    def download_video_from_url(url, output_path):
        # Get the YouTube video object
        yt = YouTube(url)

        # Get the best available progressive MP4 stream (adjust as needed)
        video_stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().last()

        # Create the full output filename with extension
        full_filename = f"{output_path}.{video_stream.subtype}"  # Use stream subtype for extension

        # Download the video stream with audio included, using the full filename
        video_stream.download(filename=full_filename)
        print(f"Downloaded video with audio to: {full_filename}")

