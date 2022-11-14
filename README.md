## HTML title scraper

In this project i wil scrap a given website and show its title on the screen.

This project will be used as first example and boilerplate to build more complex projects using Streamlit library as Front End and Python language as backend to buil powerful and state of the art projects.

### Let´s start from the beginning.

`Streamlit` is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time. [streamlit link](https://streamlit.io/)

I will cover the basics of installing Streamlit and scraping/ parsing libraries, to deep into Streamlit i reccomend to read and follow the official docs of Streamlit and make the 30 days of Streamlit challenge to don´t miss any concept about this amazing framework.

[Streamlit docs](https://docs.streamlit.io/library/get-started)

[30 days of Streamlit challenge](https://docs.streamlit.io/library/get-started)

**1.- Installation**

Prerequisites


---------------

Before you get started, you're going to need a few things:

*   Your favorite IDE or text editor
*   [Python 3.7 - Python 3.10](https://www.python.org/downloads/)
*   [PIP](https://pip.pypa.io/en/stable/installation/)

Set up your virtual environment


---------------------------------

Regardless of which package management tool you're using, we recommend running the commands on this page in a virtual environment. This ensures that the dependencies pulled in for Streamlit don't impact any other Python projects you're working on.

Below are a few tools you can use for environment management:

*   [pipenv](https://pipenv-fork.readthedocs.io/en/latest/)
*   [poetry](https://python-poetry.org/)
*   [venv](https://docs.python.org/3/library/venv.html)
*   [virtualenv](https://virtualenv.pypa.io/en/latest/)
*   [conda](https://www.anaconda.com/distribution/)

Install Streamlit on Windows


------------------------------

In the terminal that appears, type:

```
pip install streamlit
```

Test that the installation worked:
```
streamlit hello
```

### Use your new environment

1.  Open a terminal in your environment (see step 2 above).
    
2.  In the terminal that appears, use Streamlit as usual:
    
        streamlit run myfile.py

**NOTE**: To check other Operative Systems, check the related docs.

Create an app


===============

If you've made it this far, chances are you've [installed Streamlit](https://docs.streamlit.io/library/get-started/installation) and run through the basics in our [Main concepts](https://docs.streamlit.io/library/get-started/main-concepts) guide. If not, now is a good time to take a look.

The easiest way to learn how to use Streamlit is to try things out yourself. As you read through this guide, test each method. As long as your app is running, every time you add a new element to your script and save, Streamlit's UI will ask if you'd like to rerun the app and view the changes. This allows you to work in a fast interactive loop: you write some code, save it, review the output, write some more, and so on, until you're happy with the results. The goal is to use Streamlit to create an interactive app for your data or model and along the way to use Streamlit to review, debug, perfect, and share your code.

In this guide, you're going to use Streamlit's core features to create an interactive app; exploring a public Uber dataset for pickups and drop-offs in New York City. When you're finished, you'll know how to fetch and cache data, draw charts, plot information on a map, and use interactive widgets, like a slider, to filter results.

## Let´s get deep on our project!

### 1. Import the dependencies and libraries

````
import base64 (encoding/decoding binary data to printable ASCII characters)

import numpy as np (fundamental package for scientific computing with Python)
import pandas as pd ( fast, powerful, flexible and easy to use open source data analysis and manipulation tool)
import requests ( de facto standard library for making HTTP requests in Python.)
from bs4 import BeautifulSoup (library that makes it easy to scrape information from web pages)

import streamlit as st (Streamlit library)
````

### 2. Define the screen 
```
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
```

### 3.Add widgets and content

```
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
```

As you see is relatively easy to build a Streamlit app, i encourage you to learn this framework and become an amazing Front End Developer!

[If want to cooperate with the process just invite me a coffee and let´s talk about it!](https://www.buymeacoffee.com/Imanolasolo)