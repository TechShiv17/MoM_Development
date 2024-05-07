from faster_whisper import WhisperModel


class AudioTranscriber:
    @staticmethod
    def audio_transcriber(audio_path):
        model_size = "large-v2"
        model = WhisperModel(model_size, device="cpu", compute_type="int8")
        segments, info = model.transcribe(audio_path, beam_size=1)

        transcriptText = ""
        for segment in segments:
            transcriptText += segment.text

        return transcriptText

