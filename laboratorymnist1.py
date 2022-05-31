#from turtle import width
import streamlit as st
import pandas as pd #Пандас
import matplotlib.pyplot as plt #Отрисовка графиков
import seaborn as sns
import numpy as np #Numpy
from PIL import Image
import time
from datetime import datetime 

def show_image(img):
  plt.imshow(Image.fromarray(img).convert('RGB')) #Отрисовка картинки .convert('RGB')
  plt.show()
            
st.markdown('''<h1 style='text-align: center; color: black;'
            >Лабораторная работа "Распознавание рукописных цифр".</h1>''', 
            unsafe_allow_html=True)

with st.expander('Пункт 1.'):
    st.write('Разверни и прочитай все ячейки.')

with st.expander('Пункт 2.'):
    st.write('Возьми ту из предложенных цифр, которая подписана, что она хорошо распознаётся. '
             'Эта цифра похожа на цифры обучающего набора, в чём можешь убедиться, сравнив её '
             'с цифрами образцового набора на экране.')

col1, col2 = st.columns(2)
with col1:
            with st.expander('Пункт 3.'):
                        st.write('Поднеси цифру к видеокамере так, чтобы она занимала большую часть экрана видео в '
                                 'окошке, располагалась в центре и была хорошо освещена.')

            with st.expander('Пункт 4.'):
                        st.write('Другой рукой возьми мышь и щёлкни на кнопку, чтобы сделать снимок цифры.')

with col2: 
            img_file_buffer = st.camera_input("Take a picture")
            if img_file_buffer is not None:
                        img = Image.open(img_file_buffer)
                        img_array = np.array(img)
                        img_height, img_width = img_array.shape[0], img_array.shape[1]
                        img_center = int(img_width / 2)
                        left_border = int(img_center - img_height / 2)
                        right_border = int(img_center + img_height / 2)
                        img_array1 = img_array[:, left_border:right_border, :]
                        im = Image.fromarray(img_array1)
                        im.save('/app/laboratory1/your_file_image.png')
            
            
with st.expander('Пункт 5.'):
    st.write('Зарисуй полученное изображение чёрно - белой цифры в окошке под снимком цифры в бланк отчёта. '
             'Необходимо на рисунке отобразить возникшие недочёты изображения цифры, например, пропуски. Чтобы'
             ' не зарисовывать всё чёрное пространство, рекомендуется изобразить ручкой цифру на белом фоне '
             'листа бланка отчёта.')

with st.expander('Пункт 6.'):
    st.write('Нажми на кнопку распознавания, запиши результат.')

col3, col4 = st.columns(2)
with col3:
            st.write('Вот что увидела нейронная сеть.')
            if img_file_buffer is not None:
                        image11 = Image.open('/app/laboratory1/your_file_image.png')
                        img11 = image11.resize((28, 28), Image.ANTIALIAS)        
                        img12 = img11.convert("L")
                        imgData = np.asarray(img12)
                        step_lobe = .4
                        mid_img_color = np.sum(imgData) / imgData.size
                        min_img_color = imgData.min()
                        THRESHOLD_VALUE = int(mid_img_color - (mid_img_color - min_img_color) * step_lobe)
                        thresholdedData = (imgData < THRESHOLD_VALUE) * 1.0
                        imgData1 = np.expand_dims(thresholdedData, axis=0)
                        #show_image(imgData1)
                        st.image('/app/laboratory1/your_file_image.png')

                        
with col4:
                st.write('Она распознала это как...')

with st.expander('Пункт 7.'):
    st.write('Включи коррекцию яркости, если она есть, и посмотри, улучшило ли это изображение негатива цифры.'
             ' Зарисуй результат, как указано выше.')

with st.expander('Пункт 8.'):
    st.write('Нажми на кнопку распознавания, запиши результат.')

with st.expander('Пункт 9.'):
    st.write('Включи фильтр Гаусса, если такая кнопка есть, нажми на кнопку распознавания, запиши результат.')

with st.expander('Пункт 10'):
    st.write('Поставь 5 разных значений порога отсечки. Для каждого: посмотри, улучшило ли это изображени'
             'е негатива цифры. Зарисуй результат, как указано выше. Нажми на кнопку распознавания, '
             'запиши результат.')
with st.expander('Пункт 11.'):
    st.write('Сделай выводы, какие именно фильтры и как влияют на результат эксперимента')
