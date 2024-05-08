from faster_whisper import WhisperModel
import logging


class AudioTranscriber:
    @staticmethod
    def audio_transcriber(audio_path):
        logging.info(f"\nFetching the Audio from {audio_path} directory. Transcribing the Audio")
        try:
            model_size = "large-v2"
            model = WhisperModel(model_size, device="cpu", compute_type="int8")
            segments, info = model.transcribe(audio_path, beam_size=1)

            transcript_text = ""
            for segment in segments:
                transcript_text += segment.text

            return transcript_text
        except Exception as e:
            logging.error(f"An error occurred during audio transcription: {e}")

