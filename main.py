##################### Extra Hard Starting Project ######################
import datetime as dt
# 1. Update the birthdays.csv(check)
import pandas as pd
import random
import smtplib

file_path= f"letter_templates/letter_{random.randint(1,3)}.txt"


my_email= "angelasmithapple35@gmail.com"
password = "Angelarules"
now =dt.datetime.today()
day = now.day
month = now.month
birthday_data= pd.read_csv("birthdays.csv")


# 2. Check if today matches a birthday in the birthdays.csv
#btter to make a dictionary===less lines of code
for row in birthday_data.index:
        birth_month = birthday_data["month"][row]
        birth_day = birthday_data["day"][row]
        birth_name= birthday_data["name"][row]
        birth_address = birthday_data["email"][row]
 # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays
        if day == birth_day and month == birth_month:
            with open(file_path, "r") as letter:
                r_letter =letter.read()
                bday_letter= r_letter.replace("[NAME]", birth_name)

# 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:  # needs this 587 ?? to work
                connection.starttls()  # secure connection to email server
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=f"{birth_address}",
                                    msg=f"Subject: Happy Birthday!\n\n {bday_letter}")



