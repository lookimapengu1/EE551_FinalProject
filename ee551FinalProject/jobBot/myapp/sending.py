import smtplib 

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "marthajonakashian@gmail.com"
recipient = "marthanakashian@gmail.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "The results of your search"
msg['From'] = sender
msg['To'] = recipient

link1 = "www.google.com"

phrase = "Hi!\nHere are the links to the best jobs for you:\n"
body = phrase + link1
			
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("marthajonakashian","15martha15")
text = msg.as_string()
server.sendmail(sender,recipient,text)



