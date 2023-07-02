import streamlit as sl
import send_email
import pandas


sl.header("Contact Me")

if "visibility" not in sl.session_state:
    sl.session_state.visibility = "visible"
    sl.session_state.disabled = False

form = sl.form(key='email_forms')
df = pandas.read_csv("topics.csv")

with form:
    user_email = sl.text_input(label='Your Email Address', placeholder='Enter your email')
    raw_message = sl.text_area(label='Your message',placeholder='Type the message you want to send')
    select_option = sl.selectbox("What topic do you want to discuss?", df['topic'], label_visibility=sl.session_state.visibility,disabled=sl.session_state.disabled)
    message = f"""\
Subject: Email from App Todo

From: {user_email}
Topic: {select_option}
{raw_message}"""
    button = sl.form_submit_button("Submit")
    if button:
        send_email.send_mail(message=message)
        sl.info("Your email sent successfully")
