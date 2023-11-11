import pandas as pd
import smtplib
from datetime import datetime
from random import *

PLACEHOLDER = "[NAME]"


def send_mail(letter, email):
    FROM_EMAIL = "eiroltest21@gmail.com"
    PASSWORD = "djadjohinjgrmleq"
    gmail_SMTP = "smtp.gmail.com"
    PORT = 587
    SUBJECT = "HAPPY BIRTHDAY!!!"

    with smtplib.SMTP(gmail_SMTP, PORT) as conn:
        conn.starttls()
        conn.login(user=FROM_EMAIL, password=PASSWORD)
        conn.sendmail(from_addr=FROM_EMAIL,
                      to_addrs=email,
                      msg=f"Subject:{SUBJECT}\n\n{letter}")


now = datetime.now()
month = now.month
day = now.day

bday_file = pd.read_csv("birthdays.csv")

bday_today_list = {data_row["name"]: data_row["email"] for (data_index, data_row) in bday_file.iterrows()
              if data_row.month == month and data_row.day == day}

with open(f"letter_templates\\letter_{randint(1,3)}.txt") as file:
    letter = file.read()

    for index, email in bday_today_list.items():
        new_letter = letter.replace(PLACEHOLDER, index)
        send_mail(new_letter, email)








