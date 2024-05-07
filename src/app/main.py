import os
from src.utils.audio_converter import VideoToAudioConverter
from src.utils.transcriber import AudioTranscriber
from src.utils.video_downloader import VideoDownloader
from src.utils.pre_process_data import DataPreProcessing
from src.utils.summarizer import Summarization
from src.utils.pdf_generator import PDFGenerator


class VideoToAudioTranscriber:
    url = "https://www.youtube.com/watch?v=sRvLj4D5TuQ"
    
    input_output_path = "../static/"
    video_file_name = "demo_video"
    video_ext = ".mp4"
    audio_file_name = "demo_audio.mp3"

    if not os.path.isdir(input_output_path):
        os.mkdir(input_output_path)

    # To download video from YouTube
    VideoDownloader.download_video_from_url(url, f"{input_output_path}{video_file_name}")

    # To convert downloaded video to audio
    VideoToAudioConverter.audio_converter_from_video(f"{input_output_path}{video_file_name}{video_ext}",
                                                     f"{input_output_path}{audio_file_name}")

    # To transcribe the converted audio
    transcription = AudioTranscriber.audio_transcriber(f"{input_output_path}{audio_file_name}")

    # To remove the temporary files
    os.remove(f"{input_output_path}{video_file_name}{video_ext}")
    os.remove(f"{input_output_path}{audio_file_name}")

    # To perform data preprocessing on transcribed text
    preprocessedData = DataPreProcessing.clean(f"""{transcription}""")

    # To perform summarization of transcribed text
    summary = Summarization.summarization_using_mistral(preprocessedData)

    PDFGenerator.generate_transcript_pdf(summary, f"{input_output_path}/MoM.pdf")
