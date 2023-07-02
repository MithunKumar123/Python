import streamlit as sl
import send_email


sl.header("Contact Me")

form = sl.form(key='email_forms')

with form:
    user_email = sl.text_input(label='Your Email Address', placeholder='Enter your email')
    raw_message = sl.text_area(label='Your message',placeholder='Type the message you want to send')
    message = f"""\
Subject: Email from App Todo

From: {user_email}
{raw_message}"""
    button = sl.form_submit_button("Submit")
    if button:
        send_email.send_mail(message=message)
        sl.info("Your email sent successfully")