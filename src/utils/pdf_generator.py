from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

class PDFGenerator:
    @staticmethod
    def generate_transcript_pdf(transcript, output_pdf_path):
        """
        Args:
            transcript (str): Transcript text.
            output_pdf_path (str): Path to save the generated PDF document.
        """
        doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)
        styles = getSampleStyleSheet()

        # Define custom styles for different sections
        title_style = ParagraphStyle('Title', parent=styles['Title'])
        title_style.fontName = 'Helvetica-Bold'  # Make the title bold
        heading_style = ParagraphStyle('Heading1', parent=styles['Heading1'])

        # Split transcript into sections
        sections = transcript.split('\n\n')

        # Generate PDF content
        content = []

        # Add the "Minutes of Meeting" heading
        content.append(Paragraph("Minutes of Meeting", title_style))
        content.append(Spacer(1, 12))  # Add space after the heading

        for section in sections:
            if section.strip():  # Skip empty sections
                lines = [line.strip() for line in section.split('-\n') if line.strip()]
                if len(lines) > 1:
                    # Handle sections with title and content
                    for line in lines:
                        if ':' in line:
                            # Handle lines with key-value pairs
                            key, value = map(str.strip, line.split(':', 1))
                            if key and value:
                                if key == 'Notes':
                                    # Handling notes with bullet points
                                    content.append(Paragraph(f"<b>{key}:</b>", heading_style))
                                    for item in value.split('\n'):
                                        if item.strip():  # Skip empty lines
                                            content.append(Paragraph(f"• {item.strip()}", styles['Bullet']))
                                            content.append(Spacer(1, 4))  # Add space after bullet point
                                else:
                                    content.append(Paragraph(f"<b>{key}:</b> {value}", heading_style))
                        else:
                            # Handle regular content lines
                            content.append(Paragraph(line.strip(), styles['BodyText']))
                    content.append(Spacer(1, 12))  # Add space after section
                else:
                    # Handle sections without title (e.g., Additional Info)
                    content.append(Paragraph(section.strip(), styles['BodyText']))
                    content.append(Spacer(1, 12))  # Add space after section

        doc.build(content)
