import yagmail

def sendEmail(content):
    yag = yagmail.SMTP('hendryratnam07@gmail.com',oauth2_file='~/oauth2_creds.json')
    yag.send(to='hendryratnam@gmail.com', contents=content)
    print("sent email")