from collections import namedtuple
import altair as alt
import math
import streamlit as st
import pandas as pd
import requests
import os
import json
import numpy as np
import time
import datetime
from datetime import datetime, date, time



"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
email = os.environ.get('email')
password = os.environ.get('password')

"""#### Get access token, token will have 24 hour access time."""

token_url = f'http://54.254.86.214:2002/api/users/login/token/?email=nattharut.nat@cpf.co.th&password=nat221NA'
response = requests.post(token_url)
access_token = json.loads(response.content)['access_token']

if access_token:
    with st.echo(code_location='below'):




        total_points = st.slider("Number of points in spiral", 1, 5000, 3000)
        num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

        st.header("Official Date Picker")
        start_time = st.date_input('start date')
        
        end_time = st.date_input('end date')
        
        tags = st.text_input("input tags")
        st.title(tags)
        if tags and start_time and end_time:
       




            data_url = f'http://54.254.86.214:2002/api/klaeng/analytics/shrimp-wonton/ti/?start={start_time}&end={end_time}&tags={tags}'
        
            st.title(data_url)
'''
            headers_api = {
                'Authorization': 'Bearer ' + access_token
            }

            response = requests.get(data_url, headers=headers_api)
            print(response.status_code)

            df = pd.DataFrame.from_dict(response.json()['query_results'])

            pd.set_option('max_colwidth', 400)
            df = df[['timestamp','tag_index','tag_name','value']]


            df.timestamp = pd.to_datetime(df.timestamp)
            df.set_index(df.timestamp,inplace=True)

            df.value = round(df.value.astype(int)/10,2)

            dfCooker = pd.pivot_table(df, values='value', index=df.index, columns=['tag_index','tag_name'])
            dfCooker.columns = ['wonton_cooker_temp1','wonton_cooker_temp3','wonton_cooker_temp2']

            dfCooker = dfCooker.fillna(method='bfill')




            st.line_chart(dfCooker)
   '''
