import smtplib
import time
import datetime
from pydictionary import Dictionary
import csv
import random

def WordsGen():
    inFile=open('Words.csv','r',newline='\n')
    words=list(csv.reader(inFile))[0]
    return random.choices(words,k=5)

def MailGen():
    words=WordsGen()
    mailStr=[]
    for i in words:
        dict = Dictionary(i)
        meaning = dict.meanings()
        synonyms = dict.synonyms()
        mailStr.append(i)
        mailStr.append(meaning[0])
        mailStr.append(', '.join(synonyms))
        mailStr.append('')
    
    return mailStr


gmail_user = '' #address of the mail account goes here
gmail_password = '' #google app password of the account goes here

sent_from = gmail_user

to=[''] #the mail accounts to be mailed come here
subject = 'English Class Words'

def runCode():
    print('Sending mails....')
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    for i in to:
        body = MailGen()

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, i, subject, "\n".join(body))

        try:
            smtp_server.sendmail(sent_from, i, email_text)
            print ("Email sent successfully!")
        except Exception as ex:
            print ("Something went wrong….",ex)
    smtp_server.close()

weekday = []
hour = []
minute = []
#the corresponding times when the mail needs to be sent come here.

while True:
    now = datetime.datetime.today()
    for i in range(len(weekday)):
        if now.weekday() == weekday[i] and now.hour == hour[i] and now.minute == minute[i]:
            runCode()
            break
    else:
        print('Pass')
    time.sleep(60) 