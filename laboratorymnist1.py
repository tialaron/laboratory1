#from turtle import width
import streamlit as st
import pandas as pd #Пандас
import matplotlib.pyplot as plt #Отрисовка графиков
import seaborn as sns
import numpy as np #Numpy
from PIL import Image
import time
from datetime import datetime 


st.markdown('''<h1 style='text-align: center; color: black;'>Разведочный анализ данных</h1>''', unsafe_allow_html=True)
# img = Image.open('2_RANEPA.png') #1_RANEPA.jpg or 2_RANEPA.png
# st.image(img, use_column_width='auto') #width=400

st.write("""
Данный сримлит предназначен для наглядной демонтрации студентам простейших способов разведочного анализа данных (EDA - exploratory data analysis) для двух задач машинного обучения: классификация и регрессия.

\nДанные подготовил Абдулвасиев Муминшо.
""")
#-------------------------О проекте-------------------------
expander_bar = st.expander("Перед тем, как начать:")
expander_bar.markdown(
    """
\nЗадача **классификации** - предсказание категории объекта и разделение объектов согласно определенным и заданным заранее признакам. Таким образом можно сортировать данные по нужным категориям: 
одежду – по цветам или сезонам , книги – по жанрам или авторам, соусы – по степени остроты.
\nЗадача **регрессии** - предсказание целевой переменной по заданному набору признаков наблюдаемого объекта.
Таким образом можно прогнозировать цену недвижимости, капитализацию компании или стоимость акций. 
\n**Используемые библиотеки:** [streamlit](https://docs.streamlit.io/library/get-started), [pandas](https://pandas.pydata.org/docs/user_guide/index.html), [matplotlib](https://matplotlib.org/stable/api/index.html), [seaborn](https://seaborn.pydata.org).
\n **Полезно почитать:** [Про разведочный анализ данных](https://ru.wikipedia.org/wiki/Разведочный_анализ_данных), 
[Про классификацию](http://www.machinelearning.ru/wiki/index.php?title=Классификация), [Про регрессию](http://www.machinelearning.ru/wiki/index.php?title=Регрессия)
""")
