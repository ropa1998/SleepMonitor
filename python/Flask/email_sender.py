import yagmail
import keyring

# >>> import keyring
# >>> keyring.set_password("system", "username", "password")
# >>> keyring.get_password("system", "username")
# 'password'

receiver = "franz.sotoleal@ing.austral.edu.ar"
body = "Hello there from Yagmail"
username = "sleepmonitorUA@gmail.com"
password = keyring.get_password("gmail", username)

yag = yagmail.SMTP(username, password)


def send_email(to: str, subject: str, body: str, attachments: []):
    yag.send(
        to=to,
        subject=subject,
        contents=body,
        attachments=attachments
    )


send_email(receiver, body, body, ["/home/rodrigo/projects/sleepmonitor/SleepMonitor/python/Flask/templates/home.html"])
