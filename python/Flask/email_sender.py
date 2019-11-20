## @package email_sender
#  This module takes care of sending emails.


import yagmail
import keyring

# >>> import keyring
# >>> keyring.set_password("system", "username", "password")
# >>> keyring.get_password("system", "username")
# 'password'

SUBJECT = "Your SleepMonitor daily report is ready!"
BODY = "Take a look at the values for your last sleep session!"
USERNAME = "sleepmonitorUA@gmail.com"
PASSWORD = keyring.get_password("gmail", USERNAME)

yag = yagmail.SMTP(USERNAME, PASSWORD)


##  This method sends emails with the paramaters that are passed.
# @param to The receiver of the email
# @param subject The subject of the email
# @param body The body of the email
# @param attachments The attachments for the emails, passed as a list with their absolute paths.
def send_email(to: str, subject: str, body: str, attachments: []):
    yag.send(
        to=to,
        subject=subject,
        contents=body,
        attachments=attachments
    )


# send_email("franz.sotoleal@ing.austral.edu.ar", SUBJECT, BODY,
#            ["/home/rodrigo/projects/sleepmonitor/SleepMonitor/python/Flask/images/report/hum_graph.png",
#             "/home/rodrigo/projects/sleepmonitor/SleepMonitor/python/Flask/images/report/light_graph.png",
#             "/home/rodrigo/projects/sleepmonitor/SleepMonitor/python/Flask/images/report/temp_graph.png"])
