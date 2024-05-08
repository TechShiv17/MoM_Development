import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging


class SMTPEmailSender:
    @staticmethod
    def create_message(sender_email, receiver_emails, subject, body):
        """
              Creates an email message with specified sender, receiver, subject, and body.
              Args:
                  sender_email (str): Sender's email address.
                  receiver_emails (list of str): List of receiver's email addresses.
                  subject (str): Subject of the email.
                  body (str): Body content of the email.
              Returns:
                  MIMEMultipart: Email message object.
              """
        try:
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = ", ".join(receiver_emails)
            message["Subject"] = subject
            message["Bcc"] = ", ".join(receiver_emails)
            message.attach(MIMEText(body, "plain"))
            return message
        except Exception as e:
            logging.error(f"\nAn error occurred while creating email message: {e}")

    @staticmethod
    def attach_file(message, filename):
        """
               Attaches a file to the email message.
               Args:
                   message (MIMEMultipart): Email message object.
                   filename (str): Name of the file to be attached.
               Returns:
                   MIMEMultipart: Email message object with attached file.
               """
        try:
            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )
            message.attach(part)
            return message
        except Exception as e:
            logging.error(f"\nAn error occurred while attaching file to email message: {e}")

    @staticmethod
    def send_email(sender_email, receiver_emails, password, message):
        """
               Sends an email using SMTP.
               Args:
                   sender_email (str): Sender's email address.
                   receiver_emails (list of str): List of receiver's email addresses.
                   password (str): Sender's email password.
                   message (MIMEMultipart): Email message object.
               """
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_emails, message.as_string())
        except Exception as e:
            logging.error(f"\nAn error occurred while sending email: {e}")
