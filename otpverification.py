import os
import math
import random
import smtplib

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = "Hello we are ERROR404-GEC." + "Thank you for using our service. Here's your OTP "+ OTP
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("sparkvers@gmail.com", "ylfxeegirdaauiod")
emailid = input("Enter your email: ")
s.sendmail(emailid,emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
    a = input("Enter Your OTP >>: ")
    if a == OTP:
        print("Verified")
    else:
        print("Resend OTP")