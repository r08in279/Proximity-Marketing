# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:54:18 2019

@author: robin
"""

import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('robingautamsisauli@gmail.com')
EMAIL_PASSWORD = os.environ.get('robmail#71')

contacts = ['robinsingh_sa@srmuniv.edu.in']

msg = EmailMessage()
msg['Subject'] = 'These Offers may excite you!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts

msg.set_content('Hurry!! 70% off on Shirts !!')



with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)