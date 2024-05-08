import os
import logging
from src.utils.audio_converter import VideoToAudioConverter
from src.utils.transcriber import AudioTranscriber
from src.utils.video_downloader import VideoDownloader
from src.utils.pre_process_data import DataPreProcessing
from src.utils.summarizer import Summarization
from src.utils.pdf_generator import PDFGenerator
from src.utils.email_sender import SMTPEmailSender


class MoMGenerator:
    logging.basicConfig(level=logging.ERROR)

    @staticmethod
    def processVideo(url):
        try:
            tempfile_path = "../static/"
            pdf_path = "../ui/minutes-meeting-ui/src/assets/"
            video_file_name = "demo_video"
            video_ext = ".mp4"
            audio_file_name = "demo_audio.mp3"
            pdf_name = "MoM.pdf"

            if not os.path.isdir(tempfile_path):
                os.mkdir(tempfile_path)

            # To download video from YouTube
            VideoDownloader.download_video_from_url(url, f"{tempfile_path}{video_file_name}")

            # To convert downloaded video to audio
            VideoToAudioConverter.audio_converter_from_video(f"{tempfile_path}{video_file_name}{video_ext}",
                                                             f"{tempfile_path}{audio_file_name}")

            # To transcribe the converted audio
            transcription = AudioTranscriber.audio_transcriber(f"{tempfile_path}{audio_file_name}")

            # To remove the temporary files
            os.remove(f"{tempfile_path}{video_file_name}{video_ext}")
            os.remove(f"{tempfile_path}{audio_file_name}")

            # To perform data preprocessing on transcribed text
            preprocessedData = DataPreProcessing.clean(f"""{transcription}""")

            # To perform summarization of transcribed text
            summary = Summarization.summarization_using_mistral(preprocessedData)

            # To generate summary PDF
            PDFGenerator.generate_transcript_pdf(summary, f"{pdf_path}{pdf_name}")

            # Define email configuration
            subject = "MoM for your Meeting: Demo Meeting"
            body = "This is the automated Minutes of Meeting (MoM) generated from your meeting"
            sender_email = "<sender_email_id>"
            receiver_emails = ["<receiver_email_1, <receiver_email_2>"]
            password = "<user_generated_token>"
            filename = f"{pdf_path}{pdf_name}"

            # Create message
            message = SMTPEmailSender.create_message(sender_email, receiver_emails, subject, body)
            # Attach file
            message = SMTPEmailSender.attach_file(message, filename)
            # Send Email
            SMTPEmailSender.send_email(sender_email, receiver_emails, password, message)

        except Exception as e:
            logging.error(f"\nAn error occurred during MoM generation: {e}")
