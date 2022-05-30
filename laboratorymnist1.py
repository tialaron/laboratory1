import streamlit as st
import pandas as pd #Пандас
import matplotlib.pyplot as plt #Отрисовка графиков
import seaborn as sns
import numpy as np #Numpy
from PIL import Image
import time
from datetime import datetime 

st.markdown('''<h1 style='text-align: center; color: black;'
            >Разведочный анализ данных</h1>''', 
            unsafe_allow_html=True)

st.write("""
Данный сримлит предназначен для наглядной демонтрации студентам простейших способов разведочного анализа данных (EDA - exploratory data analysis) для двух задач машинного обучения: классификация и регрессия.
\nДанные подготовил Абдулвасиев Муминшо.
""")
