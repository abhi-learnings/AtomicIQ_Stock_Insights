# Web Scrapping: AtomicIQ Assignment - Stock Insights

import pandas_datareader as data
import streamlit as st
import smtplib
import os

start = '2022-01-01'
end = '2022-04-30'

st.title('AtomicIQ- Stock Insights')

user_input = st.text_input('Enter Stock Ticker ( For ex, to see SBI Insights type -> SBIN.NS ; WIPRO.NS ; TCS.NS)','DOX')
df=data.DataReader(user_input,'yahoo',start,end)

# Describing data:

st.subheader('Data from Jan-2022 to April-2022')
st.write(df.head(200))
#st.write(df.describer())


# Sending Emails:

#user_email = st.text_input("Enter your email ID to send a copy of the details")

form = st.form(key='my_form')
user_email = form.text_input(label='Enter your email ID to send a copy of the details')
submit = form.form_submit_button(label='Send Email')

EMAIL_ADDRESS='abhi.learnings@gmail.com'
EMAIL_PASSWORD='virxbcdnioseiiow'
#EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
#EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

if submit:
 with smtplib.SMTP('smtp.gmail.com',587) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    subject = 'Stocker Ticker Insights'
    body = 'Below are the Stock Ticker Insights'
    msg = f'Subject: {subject}\n\n{body}'
    server.sendmail(EMAIL_ADDRESS,user_email,msg)
    st.success('Email send successfully')


