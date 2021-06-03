#Send and Rcv Email with Gmail api

#setup credentials file from URL :https://developers.google.com/gmail/api/quickstart/python/
#Enabling Gmail api
import ezgmail, os
os.chdir(r'F:\\credentials_json_file')
ezgmail.init()

print(ezgmail.EMAIL_ADDRESS) #prints your email id

#Sending mail
ezgmail.send('hsharshshukla@gmail.com','Subject line','Body of Email',['F:\\test.txt','F:\\newpython.xlsx'],
             cc='hsharshshukla@gmail.com',bcc='otherfriend@example.com,firndls@example1.com')

print(ezgmail.EMAIL_ADDRESS)


#Reading Mail from gmail account
unreadThreads = ezgmail.unread() #list of GmailThread objects

print(ezgmail.summary(unreadThreads))   #prints summary of all unread mails

len(unreadThreads)   #no of unread items
str(unreadThreads[0])  #first item of unreadThread

len(unreadThreads[0].messages)

str(unreadThreads[0].messages[0])

unreadThreads[0].messages[0].subject  #first items subject

unreadThreads[0].messages[0].body

unreadThreads[0].messages[0].timestamp

unreadThreads[0].messages[0].sender

#downloading attachments
unreadThreads[0].messages[0].attachments  # lists all attachments
unreadThreads[0].messages[0].downloadAttachment('test.txt')
unreadThreads[0].messages[0].downloadAllAttachments(downloadFolder='F:\\gmail_download')

#SMTP
#Sending mail
#import smtplib













