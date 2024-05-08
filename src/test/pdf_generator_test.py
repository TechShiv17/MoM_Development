import unittest
from src.utils.pdf_generator import PDFGenerator
import os


class PDFGeneratorTest(unittest.TestCase):

    def test_generate_transcript_pdf(self):
        pdf_path = "../ui/minutes-meeting-ui/src/assets/"
        pdf_name = "MoM_Test.pdf"

        # Test input transcript and output PDF path
        transcript = "This is a test transcript."

        PDFGenerator.generate_transcript_pdf(transcript, f"{pdf_path}{pdf_name}")

        self.assertTrue(os.path.exists(f"{pdf_path}{pdf_name}"))
