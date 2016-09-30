
import smtplib
import sys


#Receiver
to = ''
#Sender
fro = email 


# Google SMTP Server Login Information
email = 'jayf4640@gmail.com'
pswd = 'binarysearchtree'
 
#Email message variable to send
message = 'Hello, my name is Jeremy this is a automate message, to test out a script, please acknowledge that you received it \n Thank you, \n Jeremy Ford'


#Create SMTP Session Object
# SSL port: 465
#TLS port: 587
try:
	smtpobj = smtplib.SMTP('Smtp.gmail.com' 587)
	#Identify myself to  the server(4 way handshake)
	smtobj.ehlo()
	smtpobj.starttls()
	smtpobj.Login(email, pswd)
	smtobj.quit() 
except:
	print "Server could'nt authenticate the client"
	sys.quit

#Put Server in TLS encrypted mode (encrypt all data sent to and received from server)
smtpobj.starttls()

#Login to the SMTP server
smtpobj.Login(email, pswd)

#Send mail to the reciepient
smtobj.sendmail(fro, [email1,email2], message) 

#Close the session and connection
smtobj.quit() 

#Run the program in terminal, if imported don't 
if '__name__' == '__main__':
    raw_input()
