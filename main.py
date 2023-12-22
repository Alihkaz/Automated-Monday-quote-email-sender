#imports 

import smtplib
import random 
import datetime as dt

with open("quotes.txt") as quotes_file: #reading the qoutes.txt file to extract data from it 
 qoutes_list= quotes_file.readlines()

#extracting and modifying a random quote to be sended ! 
todays_quote=random.choice(qoutes_list) 
strriped_quote=todays_quote.strip() 

#getting the day we are in to check if it's monday !
now=dt.datetime.now()
day_of_week=now.weekday()


if day_of_week==0: #if its monday

  my_email="Your Email" #  sender 
  passwordd="Your Password"# paste the code you get from gmail here 

  with smtplib.SMTP("smtp.gmail.com") as connection :
    
      connection.starttls()
      connection.login(user=my_email,password=passwordd) # receiver + letting me log in to the email that I want to send from 
      connection.sendmail(from_addr=my_email,to_addrs="The reciever email",msg= f"subject:Monday Motivation \n\n {strriped_quote}")
      connection.close()
