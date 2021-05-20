import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from time import sleep
import pathlib
from datetime import datetime
# from utils.writeToExcel import writoToExcel
time = str(datetime.today().strftime('%Y-%m-%d'))
print(time)

pathOfNew = pathlib.Path(__file__).parent / "new.txt"

def readWrite(pathOfFile):

    fileToRead =open(pathOfFile, 'r+')
    data = int(fileToRead.read())
    # print(type(data))

    newData = (data + 1)

    fileToRead.seek(0)
    fileToRead.write(str(newData))
    fileToRead.truncate()
    fileToRead.close()

    fileToReadForNewData = open(pathOfFile, 'r')
    readNewDatanum = fileToReadForNewData.read()
    fileToReadForNewData.close()

    return readNewDatanum


def sendMail():
    sender = 'treser.pirets85@gmail.com'
    receiver = 'nuruddinriaz5@gmail.com'
    username = 'treser.pirets85@gmail.com'
    password = 'nuruddinriazz'



    # Email Subject
    mail_title = 'Subject: Test Report'

    # Read html file content
    htmlPath = pathlib.Path(__file__).parent / f"../ReportHtml/report_{time}_{readNewData}.html"
    f = open(htmlPath, 'rb')
    mail_body = "Hello, Please check this report."
    f.close()


    # Mail content, format, encoding
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')

    message.attach(MIMEText(mail_body))

    # build the attachment
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(open(htmlPath, 'rb').read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(htmlPath))
    message.attach(att)

    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
        server.login(username, password)
        server.sendmail(sender, receiver, message.as_string())
        print("Send email successfully!!!")
        server.quit()
    except:
        print("Failed to send mail!!!")

# writoToExcel()
readNewData = readWrite(pathOfNew)


command = "pytest --alluredir=ReportAllure/"+ time + "_" + readNewData + " --html=ReportHtml/report_"+ time + "_" + readNewData + ".html --self-contained-html" + " " + "TestCase"
# print(command)
os.system(command)

sleep(5)

sendMail()
os.system("allure serve "+"Reports/" + time + "_" + readNewData)



