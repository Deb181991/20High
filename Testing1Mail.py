import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("debadatta@esspl.com", "Deb@1234#")
print("Login successfull")
# meassage = """\
# Subject: Hi there
#
# Dear Team,
#
#      Kindly find the attached screenshot for the Error.
#
# Thanks & Regards,
# Debadatta Pattanaik
# Senior Tester."""
# server.sendmail("debadatta@esspl.com", "debadatta@esspl.com", meassage)
# print("Eamil has been sent")
server.quit()

# import smtplib
# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# fromaddr = "debadatta@esspl.com"
# # toaddr = ["debadatta@esspl.com", "subratsahoo@esspl.com"]
# toaddr = "debadatta@esspl.com"
# # instance of MIMEMultipart
# msg = MIMEMultipart()
#
# # storing the senders email address
# msg['From'] = fromaddr
#
# # storing the receivers email address
# # Multiple email send
# # msg['To'] = ",".join(toaddr)
# # Single email send
# msg['To'] = toaddr
# # storing the subject
# msg['Subject'] = "Error meassage"
#
# # string to store the body of the mail
# # body = "Body_of_the_mail"
# body = """\
#         Subject: Error Message
#
#         Dear Team,
#
#              Kindly find the attached screenshot for the Error.
#
#         Thanks & Regards,
#         Debadatta Pattanaik
#         Senior Tester."""
# # attach the body with the msg instance
# msg.attach(MIMEText(body, 'plain'))
#
# # open the file to be sent
# filename = "Capture.png"
# attachment = open("E:\\Phoenix_20High\\Fail-ScreenShots\\Capture.png", "rb")
#
# # instance of MIMEBase and named as p
# p = MIMEBase('application', 'octet-stream')
#
# # To change the payload into encoded form
# p.set_payload((attachment).read())
#
# # encode into base64
# encoders.encode_base64(p)
#
# p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#
# # attach the instance 'p' to instance 'msg'
# msg.attach(p)
#
# # creates SMTP session
# s = smtplib.SMTP('smtp.gmail.com', 587)
#
# # start TLS for security
# s.starttls()
#
# # Authentication
# s.login(fromaddr, "Deb@12345")
#
# # Converts the Multipart msg into a string
# text = msg.as_string()
#
# # sending the mail
# s.sendmail(fromaddr, toaddr, text)
#
# # terminating the session
# s.quit()
