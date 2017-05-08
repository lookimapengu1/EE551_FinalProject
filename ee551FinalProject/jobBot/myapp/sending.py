import smtplib 
from myapp.jobsear import Jobsear

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from myapp.models import searchData

def sendMail():
        
    sender = "marthajonakashian@gmail.com"

    allData = searchData.objects.all()
    for row in allData:
	jobresults = Jobsear(row.terms,row.city,row.state)

	recipient = row.address

	msg = MIMEMultipart('alternative')
	msg['Subject'] = "The results of your search"
	msg['From'] = sender
	msg['To'] = recipient

	phrase = "Hi!\nHere are the links to the best jobs for you:\n"
        jobs = ''
        for job in jobresults:
                jobs += 'Title: '+ job[0]+ '\tCompany: '+ job[1]+ '\tLocation: '+ job[2]+ ', '+ job[3]+ '\tLink: '+ job[4]+ '\n'

        body = phrase + jobs
			
	msg.attach(MIMEText(body, 'plain'))

	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login("chronostat.sit@gmail.com","cpe/ee423")
	text = msg.as_string()
	server.sendmail(sender,recipient,text)



