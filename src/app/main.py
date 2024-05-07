import os
from src.utils.audio_converter import VideoToAudioConverter
from src.utils.transcriber import AudioTranscriber
from src.utils.video_downloader import VideoDownloader


class VideoToAudioTranscriber:
    url = "https://www.youtube.com/watch?v=sRvLj4D5TuQ"
    input_output_path = "../static/sample_rec/"
    video_file_name = "demo_video"
    video_ext = ".mp4"
    audio_file_name = "demo_audio.mp3"

    # To download video from YouTube
    VideoDownloader.download_video_from_url(url, f"{input_output_path}{video_file_name}")

    # To convert downloaded video to audio
    VideoToAudioConverter.audio_converter_from_video(f"{input_output_path}{video_file_name}{video_ext}",
                                                     f"{input_output_path}{audio_file_name}")

    # To transcribe the converted audio
    AudioTranscriber.audio_transcriber(f"{input_output_path}{audio_file_name}")

    # To remove the temporary files
    os.remove(f"{input_output_path}{video_file_name}{video_ext}")
    os.remove(f"{input_output_path}{audio_file_name}")
