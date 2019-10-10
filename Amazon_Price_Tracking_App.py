# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:10:21 2019

@author: Ravi
"""

import requests
from bs4 import BeautifulSoup 
import smtplib


URL = 'https://www.amazon.de/Samsung-Smartphone-interner-Speicher-Charcoal-Black/dp/B07NH3C1KN/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=mobile+phone&qid=1570702677&smid=A3JWKAKR8XB7XF&sr=8-5'
headers = {"User-Agent": 'search my user agent on google and past it here'}


def check_price (): 
    page = requests.get (URL, headers= headers)
    soup = BeautifulSoup (page.content, 'html.parser')
    title = soup.find (id = "productTitle").get_text()
    price = soup.find (id = "priceblock_dealprice").get_text()
    converted_price = price [0:6]
    
    if (converted_price > 170):
        send_mail()
    else:
        print ("price is still high!")
        
    print (converted_price)
    print (price)
    print (title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('sender emil', 'password' )
    subject= "The price is falling!"
    body = "Check this link: https://www.amazon.de/Samsung-Smartphone-interner-Speicher-Charcoal-Black/dp/B07NH3C1KN/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=mobile+phone&qid=1570702677&smid=A3JWKAKR8XB7XF&sr=8-5 "
    msg = ("Subject: {subject}\n\n {body}").format(subject=subject, body=body)
    server.sendmail('sender email', 'reciver email', msg)
    print ("Email has been sent!")
    server.quit()
    
check_price()    