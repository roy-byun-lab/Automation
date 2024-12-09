"""
simple e-mail cleaner that will weed out promo emails from Gmail
Ever feel your inbox blow up with unread newsletters, promotion emails, and spam? What if I told you it was possible to automate all of this with Python?
Instead of doing all that by hand, why not let Python do the job?

What You’ll Need:
    Google Gmail API (To access your inbox)
    Regular expressions (To filter out junk)
"""

import re
import imaplib
import email
from email.header import decode_header

# Connect to the Gmail server
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("your_email@gmail.com", "your_password")
mail.select("inbox")

# Search for all emails
status, messages = mail.search(None, "ALL")
email_ids = messages[0].split()

# Loop through all emails and filter out unwanted ones
for email_id in email_ids:
    status, msg_data = mail.fetch(email_id, "(RFC822)")
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            # convert to message from byte data
            msg = email.message_from_bytes(response_part[1]) # response_part[1] contains the email's byte data
            # get subject header from msg
            subject, encoding = decode_header(msg["Subject"])[0]
            
            # Check if the subject contains a promotional keyword
            if re.search(r"(sale|promotion|offer|newsletter)", subject, re.IGNORECASE):
                mail.store(email_id, '+FLAGS', '\\Deleted')  # Mark as deleted
                print(f"Deleted: {subject}")

# Expunge deleted messages
mail.expunge()
mail.logout()