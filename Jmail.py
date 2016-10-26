
import smtplib
import sys
import base64



#Receiver
to = base64.b64decode('amZvcmQyMDlAeWFob28uY29t')
#Sender
fro = email 


# Google SMTP Server Login Information
email = base64.b64decode('amF5ZjQ2NDBAZ21haWwuY29t')
pswd = base64.b64decode('YmluYXJ5c2VhcmNodHJlZQ==')
 
#Email message variable to send
message = 'Hello, my name is Jeremy this is a automate message, to test out a script, please acknowledge that you received it \n Thank you, \n Jeremy Ford'


#Create SMTP Session Object
# SSL port: 465
#TLS port: 587
try:
	def send_mail():
		#Instantiate smtplib object 
		smtpobj = smtplib.SMTP('Smtp.gmail.com' 587)
		#Identify myself to  the server, return tuple from server
		smtobj.ehlo()
		# Prepare TLS encrypted connection
		smtpobj.starttls()
		#Login to SMTP server
		smtpobj.login(email,pswd)
		#Send mail to the reciepient
		smtobj.sendmail(fro, to, message) 
		# End the connection
		smtobj.quit() 
except:
		print "Server could'nt authenticate the client"
		sys.quit



#Run the program in terminal, if imported don't 
if '__name__' == '__main__':
    send_mail()
