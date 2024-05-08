import os
import re
import unittest
from email.mime.multipart import MIMEMultipart
import smtplib
from src.utils.email_sender import SMTPEmailSender
from src.utils.pdf_generator import PDFGenerator


class SMTPEmailSenderTest(unittest.TestCase):

    def test_create_email_message(self):
        subject = "MoM for your Meeting: Demo Meeting"
        body = "This is the automated Minutes of Meeting (MoM) generated from your meeting"
        sender_email = "test@gmail.com"
        receiver_emails = ["test@gmail.com"]

        email_message = SMTPEmailSender.create_message(sender_email, receiver_emails, subject, body).as_string()

        from_pattern = re.search(r"From: (.+)", email_message).group(1)
        to_pattern = re.search(r"To: (.+)", email_message).group(1)
        subject_pattern = re.search(r"Subject: (.+)", email_message).group(1)
        bcc_pattern = re.search(r"Bcc: (.+)", email_message).group(1)

        assert (from_pattern.strip() == f"{sender_email}")
        assert (to_pattern.strip() == f"{receiver_emails[0]}")
        assert (subject_pattern.strip() == f"{subject}")
        assert (bcc_pattern.strip() == f"{receiver_emails[0]}")

    def test_create_email_message_not_match_with_other_email(self):
        subject = "MoM for your Meeting: Demo Meeting"
        body = "This is the automated Minutes of Meeting (MoM) generated from your meeting"
        sender_email = "test@gmail.com"
        receiver_emails = ["test@gmail.com"]

        email_message = SMTPEmailSender.create_message(sender_email, receiver_emails, subject, body).as_string()

        from_pattern = re.search(r"From: (.+)", email_message).group(1)
        to_pattern = re.search(r"To: (.+)", email_message).group(1)
        subject_pattern = re.search(r"Subject: (.+)", email_message).group(1)
        bcc_pattern = re.search(r"Bcc: (.+)", email_message).group(1)

        assert (from_pattern.strip() != "wrongemail@gmail.com")
        assert (to_pattern.strip() != "wrongemail@gmail.com")
        assert (subject_pattern.strip() != "Wrong Subject")
        assert (bcc_pattern.strip() != "wrongemail@gmail.com")

    def test_attach_file_match_with_return_type(self):
        pdf_path = "../ui/minutes-meeting-ui/src/assets/"
        pdf_name = "MoM_Test.pdf"

        subject = "MoM for your Meeting: Demo Meeting"
        body = "This is the automated Minutes of Meeting (MoM) generated from your meeting"
        sender_email = "test@gmail.com"
        receiver_emails = ["test@gmail.com"]
        filename = f"{pdf_path}{pdf_name}"

        if os.path.exists(f"{pdf_path}{pdf_name}"):
            pass
        else:
            PDFGenerator.generate_transcript_pdf("Generating Basic Text For PDF", f"{pdf_path}{pdf_name}")

        message = SMTPEmailSender.create_message(sender_email, receiver_emails, subject, body)

        res = SMTPEmailSender.attach_file(message, filename)

        self.assertIsInstance(res, MIMEMultipart)

