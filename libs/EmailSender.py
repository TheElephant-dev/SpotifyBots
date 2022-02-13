import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#The mail addresses and password
sender_address = 'SOMEEMAIL@DOMAIN.com' # < ---------------------------- Enter gmail credentials here to have an account send you emails once a bot is detected by spotify.
sender_pass = 'PASSWORD'# < ----------------------------
receiver_address = 'ADIFFERENTEMAIL@DOMAIN.com' # < ---------------------------- Enter your email address here to get notifications


def Send(Title: str = 'Bot Error:', MailContent: str = 'Missing Content'):
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = Title  # The subject line

	# The body and the attachments for the mail
	message.attach(MIMEText(MailContent, 'plain'))


	# Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
	session.starttls()  # enable security
	session.login(sender_address, sender_pass)  # login with mail_id and password
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()
	print(f'\n### Mail Sent to "{receiver_address}", with Title: "{Title}", and content:\n### """\n### {MailContent}\n###\n"""')
