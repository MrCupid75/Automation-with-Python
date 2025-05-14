import smtplib
import imaplib

smtp_server = "smtp.gmail.com"
smtp_port = 587

imap_server = "imap.gmail.com"
imap_port = 993

sender_email = "mjnuvor@gmail.com"
sender_password = "xrnb gdli xiej mjza"

receiver_email = "mensahjoseph100701@gmail.com"

def send_confirmation_email(client_email, client_name):

    message = f"""\
Subject: Hello {client_name}

Sit up bro, ain't no one here doing what you doing
"""

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, client_email, message)
        print("Email sent successfully")
    except Exception as e:
        print("Error sending mail", e)
    finally:
        server.quit()

def check_new_message(client_email, client_name):
    try:
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        mail.login(client_email, sender_password)
        mail.select("Inbox")

        status, messages = mail.search(None, "UNSEEN")

        if status == "OK":
            for num in messages[0].split():
                status, data = mail.fetch(num, "(RFC822)")

                if status == "OK":
                    unread_email = data[0][1]
                    print("Fetched an unread email", unread_email)
        else:
            print("Error search for unread email")

    except Exception as e:
        print("Error fetching emails", e)


# send_confirmation_email(receiver_email, "Beast")

check_new_message(sender_email, "Beast")