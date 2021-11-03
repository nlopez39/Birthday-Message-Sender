import smtplib
import random
import datetime as dt
my_email = "angelasmithapple35@gmail.com"
password="Angelarules"



#how to tap into datetime
now = dt.datetime.now()
week_day = now.weekday()

#if it is Friday then output random quote
if week_day == 4:
    # read the txt file and turn it into a list
    with open("quotes.txt", "r") as quotes:
        read_quote = quotes.readlines()
        quote_list = [quote for quote in read_quote]
        random_quote = random.choice(quote_list)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:  # needs this 587 ?? to work
        connection.starttls()  # secure connection to email server
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs="nlopez53@ucmerced.edu",
                            msg=f"Subject:Hello\n\n {random_quote}")












# #how to create data
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)