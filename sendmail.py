import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests, datetime
from bs4 import BeautifulSoup #To install: pip3 install beautifulsoup4


pincodes = [331802, 721302]

email_sender_account = "chandancbh123@gmail.com" #your email
email_sender_username = "chandancbh123@gmail.com"  #your email username
email_sender_password = "*Australia1"#your email password
email_smtp_server = "smtp.gmail.com" #change if not gmail.
email_smtp_port = 587 #change if needed.

def SendEmail (pincode):
    
    email_subject = "COVID-19 vaccine available at " + pincode
    email_body = '<html><head></head><body>'
    email_body += '<style type="text/css"></style>' 
    email_body += '<h2>Vaccine available</h2></body></html>'

    server = smtplib.SMTP(email_smtp_server,email_smtp_port) 
    
    print("Logging in to {email_sender_account}")
    
    server.starttls() 
    server.login(email_sender_username, email_sender_password)
    
    if pincode == 737102 or pincode == 331802:
        email_recipients = ["chandancbh@gmail.com"]
    elif pincode == 721302:
        email_recipients = ["atulatj@gmail.com", "chandancbh@gmail.com"]
    else:
        email_recipients = ["chandancbh@gmail.com"]


    for recipient in email_recepients:
        print("Sending email to {recipient}")
        message = MIMEMultipart('alternative') 
        message['From'] = email_sender_account 
        message['To'] = recipient 
        message['Subject'] = email_subject 
        message.attach(MIMEText(email_body, 'html')) 
        server.sendmail(email_sender_account,recipient,message.as_string())
    server.quit()

while (1):
    for pincode in pincodes:
        time = datetime.datetime.today().strftime('%d-%m-%y')

        day = int(time.split("-")[0])
        month = time.split("-")[1]
        year = time.split("-")[2]



        for i in range(0,5):
            
            url = "https://www.cowin.gov.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + str(pincode) + "&date=" + str(day) + "-" + str(month) + "-" + str(year)
            
            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()

                for centres in data:
                    for index in range(0, len(data["centers"])):
                        centre = data['centers'][index]
                        for session in range(0, len(data['centers'][index]['sessions'])):
                            capacity = (data['centers'][index]['sessions'][session]['available_capacity'])
                            print(pincode)
                            if capacity > 0:
                                print("SendEmail")
                                SendEmail(pincode)
                                pincodes = pincodes.remove(pincode)
                            else:
                                print("trying")

                day += 1
            else:
                pass


email_sender_account = "chandancbh123@gmail.com" #your email
email_sender_username = "chandancbh123@gmail.com"  #your email username
email_sender_password = "*Australia1"#your email password
email_smtp_server = "smtp.gmail.com" #change if not gmail.
email_smtp_port = 587 #change if needed.

def SendEmail (pincode):
    
    email_subject = "COVID-19 vaccine available at " + pincode
    email_body = '<html><head></head><body>'
    email_body += '<style type="text/css"></style>' 
    email_body += '<h2>Vaccine available</h2></body></html>'

    server = smtplib.SMTP(email_smtp_server,email_smtp_port) 
    
    print("Logging in to {email_sender_account}")
    
    server.starttls() 
    server.login(email_sender_username, email_sender_password)
    
    if pincode == 737102 or pincode == 331802:
        email_recipients = ["chandancbh@gmail.com"]
    elif pincode == 721302:
        email_recipients = ["atulatj@gmail.com", "chandancbh@gmail.com"]
    else:
        email_recipients = ["chandancbh@gmail.com"]


    for recipient in email_recepients:
        print("Sending email to {recipient}")
        message = MIMEMultipart('alternative') 
        message['From'] = email_sender_account 
        message['To'] = recipient 
        message['Subject'] = email_subject 
        message.attach(MIMEText(email_body, 'html')) 
        server.sendmail(email_sender_account,recipient,message.as_string())
    server.quit()



