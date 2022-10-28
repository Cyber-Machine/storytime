from asyncore import read
from copyreg import pickle
import streamlit as st
import pandas as pd
import numpy as np
import re
import string
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random

# Setting Homepage title & icon
st.set_page_config(page_title='Home')


st.markdown('''
    # Story Generator using Markov Chains
    - A simple story generator using Markov Chains and NLP.
''')

with st.sidebar.header('About'):
    st.markdown('''
    - This is a simple demonstration of application of Markov Chains in text generation.
    - [Link of Dataset](https://www.kaggle.com/datasets/jannesklaas/scifi-stories-text-corpus?resource=download)
    ''')



dbfile = open('MobyDick', 'rb') 
markov_model = pickle.load(dbfile)
def generate_story(markov_model, limit=10, start='my god'):
    n = 0
    curr_state = start
    next_state = None
    story = ""
    story+=curr_state+" "
    while n<limit:
        next_state = random.choices(list(markov_model[curr_state].keys()),
                                    list(markov_model[curr_state].values()))
        
        curr_state = next_state[0]
        story+=curr_state+" "
        n+=1
    return story

# print(generate_story(markov_model , start="all stories" , limit = 12))
# col1 , col2 = st.columns(2)
# st.write(markov_model)
# input_text = ""
# with col1:
input_text = st.text_input(
    "Enter Text to generate",
    "guess what",
    key="placeholder"
)
option = st.selectbox(
        "Length of words to be generated ..",
        (8, 10, 12)
    )
times = st.text_input(
    "Times you want to generate string",
    1,
    key = "ABCD"
)
# with col2:
if input_text:
    for i in range(int(times)):
        st.write("\n"+generate_story(markov_model, start=' '.join(input_text.lower().split(' ')[:2]), limit=option).title())


# st.write("\n" + generate_story(markov_model , start = "guess what" , limit = 10))
