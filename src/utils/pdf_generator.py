import logging
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from faster_whisper import WhisperModel

# Configure logging
logging.basicConfig(filename='transcript.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_transcript_pdf(audio_file_path, output_pdf_path):
    """
    Generates a PDF containing the transcript of a meeting from an audio file.

    Args:
        audio_file_path (str): Path to the audio file containing the meeting recording.
        output_pdf_path (str): Path to save the generated PDF document.
    """
    # Whisper transcription
    try:
        logging.info("Transcribing audio file...")
        model_size = "large-v2"
        model = WhisperModel(model_size, device="cpu", compute_type="int8")
        segments, info = model.transcribe(audio_file_path, beam_size=1)
        transcript_text = ""
        for segment in segments:
            transcript_text += segment.text + "\n"
        logging.info("Transcription successful.")
    except Exception as e:
        logging.error(f"Transcription failed: {e}")
        return

    # Create PDF document
    try:
        logging.info("Generating PDF...")
        doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)
        styles = getSampleStyleSheet()

        # Transcript section
        transcript = [Paragraph("Meeting Transcript:", styles['Title']), 
                      Paragraph(transcript_text, styles['BodyText'])]
        
        doc.build(transcript)
        logging.info(f"PDF generated successfully: {output_pdf_path}")
    except Exception as e:
        logging.error(f"PDF generation failed: {e}")

# Usage example
generate_transcript_pdf("/home/nashtech/Downloads/Audio_Twitter_Tweets.mp3", "/home/nashtech/Documents/MoM_Development/transcript_pdf/transcript.pdf")
