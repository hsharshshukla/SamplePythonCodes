import smtplib
smtpobj = smtplib.SMTP('smtp.gmail.com',587)
print(smtpobj.ehlo())

smtpobj.startttls() #TLS Encryption
smtpobj.login('bob@example.com','password')

smtpobj.sendmail('senderrmail','rcvrmailid','Subject: Holiday \nDear, i am on holiday, Yours Bob')
smtpobj.quit()




