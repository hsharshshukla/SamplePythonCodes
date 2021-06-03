#Internet message access protocol
import imapclient
imapobj = imapclient.IMAPClient('imap.example',ssl=True)

imapobj.login('email_addres','password')
#imapobj.list_folders()   - list all folders

imapobj.select_folder('INBOX',readonly=True)

#Search
#ALL
#Before date, ON date, SINCE date
#SUBJECT string, BODY string, TEXT string
#FROM string, TO strng , CC string , BCC string
#SEEN , UNSEEN
#ANSWERED,   UNANSWERED
#DELETED,  UNDELETED
#DRAFT,  UNDRAFT
#FLAGGED, UNFLAGGED
#LARGER N  , SMALLER N - returns all messages LARGER or SMALLER than N bytes
#NOT search-key, OR search-key1 search-key2


UIDs = imapobj.search('SINCE 05-Apr-2021') #list of emails with uids , unique id of email
rawMessages  = imapobj.fetch([400041],['BODY[]','FLAGS'])
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[400041][b'BODY[]'])
message.get_subject() #get_addresses('to'), get_addresses('cc'),get_addresses('bcc')


