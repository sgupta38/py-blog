## This will demonstrate how python is used to send emails.
##
##
## Note: Before you start sending email, you need to complete '2-step verification' procedure with google.
## Once that done, generate 'App Specific Password'[https://support.google.com/accounts/answer/185833?hl=en]
## This will give 16 character password which is further used in this script for login purpose.

import smtplib

# (domainname, port)
conn = smtplib.SMTP('smtp.gmail.com', 587) # pass domain name of smtp server

conn.ehlo() # helo check

conn.starttls() # Starts encryption

#conn.login(username, app_specific_password)
conn.login('username@gmail.com', 'passpasspasspass') # Enter 'App Specific Password'[16-character long]

# conn.sendmail(from, to, body)
conn.sendmail('username@gmail.com', 'another_user@gmail.com', 'Subject: Notifier \n\n Dear Sir, \n\nThis mail is sent to you from the python script.\n\n-Regards,\n Notorious')

# Ends connection
conn.quit()
