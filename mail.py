import smtplib

#Replace port SMTP and PORT
smtpObj = smtplib.SMTP('SMTP', PORT)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.ehlo()
smtpObj.login('MAIL', 'PWD')

smtpObj.quit()