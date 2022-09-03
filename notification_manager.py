import os
import smtplib
from data_manager import DataManager

SMTP_EMAIL = "smtp.gmail.com"
FROM_EMAIL = os.environ.get("FROM_EMAIL")
TO_EMAIL = os.environ.get("TO_EMAIL")
PASSWORD = os.environ.get("PASSWORD")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.from_email = FROM_EMAIL
        self.to_email = TO_EMAIL
        self.password = PASSWORD

    def send_email(self, message: str, to_address=TO_EMAIL):
        with smtplib.SMTP(SMTP_EMAIL, 587) as connection:
            connection.starttls()
            connection.login(self.from_email, self.password)
            connection.sendmail(from_addr=self.from_email, to_addrs=to_address, msg=message.encode('utf-8'))

    def send_email_to_all(self, message: str):
        data_manager = DataManager()
        user_data = data_manager.get_users_sheet()
        for user in user_data:
            self.send_email(message, user['email'])
