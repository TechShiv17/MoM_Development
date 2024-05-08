from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
import logging


class PDFGenerator:
    @staticmethod
    def generate_transcript_pdf(transcript, output_pdf_path):
        """
               Args:
                   audio_file_path (str): Path to the audio file containing the meeting recording.
                   output_pdf_path (str): Path to save the generated PDF document.
                   :param output_pdf_path:
                   :param transcript:
               """
        try:
            doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)
            styles = getSampleStyleSheet()

            # Transcript section
            transcript = [Paragraph("Meeting Transcript:", styles['Title']),
                          Paragraph(transcript, styles['BodyText'])]
            doc.build(transcript)
        except Exception as e:
            logging.error(f"\nAn error occurred during PDF generation: {e}")
