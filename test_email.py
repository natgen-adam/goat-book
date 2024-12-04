import os
import imaplib

password = os.environ["EMAIL_PASSWORD"]
username = os.environ["EMAIL_ACCOUNT"]

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)
mail.select("Inbox")
typ, res = mail.search(None, "FROM", "superlists")
uid = res[0].split()[-1]
_, message = mail.fetch(uid, "(RFC822)")
message_str = message[0][1].decode("utf-8")
mail.close()
mail.logout()
