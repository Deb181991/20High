import win32com.client

OutLook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = OutLook.Folders('debadatta@esspl.com').Folders('Inbox')
messages = inbox.Items

for msg in messages:
    if 'Training Session on JIRA Functionalities and Applicability' in msg.Subject:
        print(msg.Body)
