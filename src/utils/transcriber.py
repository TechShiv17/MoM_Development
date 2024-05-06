from faster_whisper import WhisperModel

model_size = "large-v2"
model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe("1to1mtg.mp3", beam_size=1)

transcriptText = ""
for segment in segments:
    transcriptText += segment.text

print(transcriptText)