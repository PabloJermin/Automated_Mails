import random

import pandas
import datetime as dt
import smtplib
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
My_email = "pablojermin@gmail.com"
Password = "pablosokovski1$"

data = pandas.read_csv("birthdays.csv")
# dict_data = dat
# print(data)

# -----CURRENT DAYS-----#
now = dt.datetime.now()
day = now.day
month = now.month
cur_day =(day, month)


new_data = {(row.day,row.month): row for (index, row) in data.iterrows() }

# ----CHECKING FOR THE MATCHING DAY------- #
if cur_day in new_data:
    b_person = new_data["(row.day,row.month)"]
    n = random.randint(1,3)

    # ----OPENING THE DOCUMENT FILE-----#
    with open(f"letter_templates/letter_{n}.txt", mode="r") as b_lett:
        first_line = b_lett.read()
        first_line = first_line.replace("[names]", b_person.name)

    # ------SENDING THE MESSAGE----#
    with smtplib.SMTP("smtp.gmail.com") as m_file:
        m_file.starttls()
        m_file.login(email=My_email, password=Password)
        m_file.sendmail(from_addr=My_email, to_addrs=b_person.mail, msg=f"Subject: Time Aso\n\n{first_line}")




