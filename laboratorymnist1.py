#from turtle import width
import streamlit as st
import pandas as pd #Пандас
#import matplotlib.pyplot as plt #Отрисовка графиков
#import seaborn as sns
import numpy as np #Numpy
from PIL import Image
import time
from datetime import datetime 


#st.markdown('''<h1 style='text-align: center; color: black;'>Разведочный анализ данных</h1>''', unsafe_allow_html=True)
# img = Image.open('2_RANEPA.png') #1_RANEPA.jpg or 2_RANEPA.png
# st.image(img, use_column_width='auto') #width=400

new_title = '<p style="font-family:serif; color:Black; font-size: 22px;">New image</p>'
st.markdown(new_title, unsafe_allow_html=True)

st.write("""
Данный сримлит предназначен для лабораторной работы задач машинного обучения: классификация.

\nДанные подготовил Абдулвасиев Муминшо.
""")
