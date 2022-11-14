# Web title scraper with Streamlit Front End

# Import modules and dependencies
import base64

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

import streamlit as st

# Define the screen
def _max_width_():
    max_width_str = f"max-width: 1100px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True, 
    )

_max_width_()

# Add widgets and content
#Title
st.title("🌐 HTML title Scraper 🕸️")
# header 1
st.markdown(" A simple HTML title scraper made in Python 🐍 & the amazing [Streamlit!](https://www.streamlit.io/) ")
# header 2
st.markdown('### **1️⃣ Enter a URL to scrape **')

try:
    # Insert text (URL)
    url =  st.text_input("", value='https://stackexchange.com/leagues/1/alltime/stackoverflow', max_chars=None, key=None, type='default')
    # Check if input URL exists
    if url:
        arr = ['https://', 'http://']
        if any(c in url for c in arr):


    #    if "https" in url:

            header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
            }

            # Get the website content
            r = requests.get(url, headers=header)
            soup = BeautifulSoup(r.text, 'html.parser')

            st.text("Title of the website is : ")
            # Check for website title and present it
            for title in soup.find_all('title'):
                st.write(title.get_text())         

except NameError:
    print ('wait')
    
# Credits
st.markdown("---")

st.markdown('*Made with* :heart: * by [@jjusturi ](https://twitter.com/jjusturi) [![this is an image link](https://i.imgur.com/Ltgzb7Y.png)](https://www.buymeacoffee.com/Imanolasolo)')
