import datetime as dt
import smtplib
import random

my_email= "pablojermin@gmail.com"
password= "pablosokovski1$"


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open("quotes.txt", mode= "r") as q_file:
        l_quotes = q_file.readlines()
        d_quote = random.choice(l_quotes)
        print(d_quote)
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(email=my_email, password=password)
    #     connection.sendmail(from_addr=my_email, to_addrs="amarteyjermin@gmail.com", msg=f"Subject: Quote of the week\n"
    #                                                                                     f"\n{d_quote}")











# ----------------SENDING EMAILS-------------------#
#
#
# my_email = "pablojermin@gmail.com"
# password = "pablosokovski1$"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(email=my_email, password=password)
#     connection.sendmail(from_addr=my_email,to_addrs="amarteyjermin@gmail.com",
#                         msg="Subject:Be there\n\n This is the body")



# ---------------DATE TIME-------------------#
# now = dt.datetime.now()
# month = now.month
# day =  now.day
# weekday = now.weekday()
# vacation_day = dt.datetime(year=2000, month=3, day=4)
# print(vacation_day)
