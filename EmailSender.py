from email.message import EmailMessage
from password import password
import ssl
import smtplib

email = "Write Your Email Here"
password = password
email_reciever = "Write Reciever Email Here"

subject = "Write Your Subject/Title Here"
body = """
Write Your Program Here
"""

em = EmailMessage()
em["From"] = email
em["To"] = email_reciever
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email, password)
    smtp.sendmail(email, email_reciever, em.as_string())
