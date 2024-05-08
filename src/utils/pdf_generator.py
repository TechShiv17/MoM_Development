from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


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
        doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)
        styles = getSampleStyleSheet()

        # Transcript section
        transcript = [Paragraph("Meeting Transcript:", styles['Title']),
                      Paragraph(transcript, styles['BodyText'])]
        doc.build(transcript)
