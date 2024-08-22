# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# mail_content = '''Hello,
# This is a test mail.
# In this mail we are sending some attachments.
# The mail is sent using Python SMTP library.
# Thank You
# '''
# # The mail addresses and password
# sender_address = 'debadatta@esspl.com'
# sender_pass = 'Deb@12345'
# receiver_address = 'debadatta@esspl.com'
#
# message = MIMEMultipart()
# message['From'] = sender_address
# message['To'] = receiver_address
# message['Subject'] = 'A test mail sent by Python. It has an attachment.'
# # The subject line
# # The body and the attachments for the mail
# message.attach(MIMEText(mail_content, 'plain'))

import email
import imaplib

FROM_EMAIL = "debadatta@esspl.com"
FROM_PWD = "Deb@12345"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993
mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_EMAIL, FROM_PWD)
print("Login done")


def read_email_from_gmail():
    try:

        mail.select('inbox')

        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id, first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)')
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1], 'utf-8'))

                    email_subject = msg["Subject"]
                    # email_from = msg['from']
                    # print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject)

    except Exception as e:
        # traceback.print_exc()
        print(str(e))


read_email_from_gmail()
