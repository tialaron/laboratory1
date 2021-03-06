#from turtle import width
import streamlit as st
import pandas as pd #Пандас
#import matplotlib.pyplot as plt #Отрисовка графиков
#import seaborn as sns
import numpy as np #Numpy
from PIL import Image, ImageEnhance, ImageFilter
import time
from datetime import datetime
from tensorflow.keras.models import load_model

def show_image(img):
    plt.imshow(Image.fromarray(img).convert('RGB')) #Отрисовка картинки .convert('RGB')
    plt.show()

model_2d = load_model('/app/laboratory1/mnist_2d.h5')    
file_path = '/app/laboratory1/your_file_image.png'
picture_all = '/app/laboratory1/realtrack1.jpg'

st.markdown('''<h1 style='text-align: center; color: black;'
            >Лабораторная работа "Распознавание рукописных цифр".</h1>''', 
            unsafe_allow_html=True)

with st.expander('Общая схема создания нейронной сети.'):
    st.image(picture_all)
    
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
                        im.save(file_path)
            
            
with st.expander('Пункт 5.'):
    st.write('Зарисуй полученное изображение чёрно-белой цифры из окошка в бланк отчёта. '
             'Необходимо на рисунке отобразить возникшие недочёты изображения цифры, например, пропуски. Чтобы'
             ' не зарисовывать всё чёрное пространство, рекомендуется изобразить ручкой цифру на белом фоне '
             'листа бланка отчёта.')

with st.expander('Пункт 6.'):
    st.write('Нажми на кнопку распознавания, запиши результат.')
    isbutton1 = st.button('Распознать')
    col3, col4 = st.columns(2)
    with col3:      
              st.write('Вот что увидела нейронная сеть.')
              if isbutton1:
                          image11 = Image.open(file_path)
                          st.image(file_path) 
                          img11 = image11.resize((28, 28), Image.LANCZOS)   
                          img11.save(file_path) 
                          
                          #img12 = img11.convert("L")
                          #imgData = np.asarray(img12)
                          #step_lobe = .4
                          #mid_img_color = np.sum(imgData) / imgData.size
                          #min_img_color = imgData.min()
                          
                          
                          #THRESHOLD_VALUE = int(mid_img_color - (mid_img_color - min_img_color) * step_lobe)
                          #thresholdedData = (imgData < THRESHOLD_VALUE) * 1.0
                          imgData1 = np.expand_dims(np.asarray(img11.convert("L")), axis=0)

                        
    with col4:
              st.write('Она распознала это как...')
              if isbutton1:
                          y_predict1 = model_2d.predict(imgData1) 
                          y_maxarg = np.argmax(y_predict1, axis=1)
                          st.subheader(int(y_maxarg))

with st.expander('Пункт 7.'):
    st.write('Включи коррекцию яркости. Посмотри, улучшило ли это изображение негатива цифры.'
             ' Зарисуй результат, как указано выше.')
    col5,col6 = st.columns(2)
    with col5:
              value_sli = st.slider('Коррекция яркости', 0.0, 100.0, 50.0)
    with col6:
              st.write('Яркость',value_sli)
              image111 = Image.open(file_path)
              enhancer = ImageEnhance.Brightness(image111)
            
              factor = 2*value_sli / 100 #фактор изменения
                
              im_output = enhancer.enhance(factor)
              im_output.save(file_path)
              #img111 = image111.resize((28, 28), Image.LANCZOS)     
              #img121 = img111.convert("L")
              #imgData = np.asarray(img121)
              #step_lobe = value_sli / 100
              #mid_img_color = np.sum(imgData) / imgData.size
              #min_img_color = imgData.min()
              #THRESHOLD_VALUE = (mid_img_color - (mid_img_color - min_img_color) * step_lobe)
              #thresholdedData = (imgData < THRESHOLD_VALUE) * 1.0
              #imgData1 = np.expand_dims(thresholdedData, axis=0)
              #st.write(imgData1.shape)
              #tgt1 = np.squeeze(imgData1)
              #st.write(tgt1.shape)
              #im111 = Image.fromarray(tgt1)
              #st.write(imgData1)
              #im111.save(file_path)
              st.image(file_path)
              #y_predict1 = model_2d.predict(imgData1) 
              #y_maxarg = np.argmax(y_predict1, axis=1)
              #st.subheader(int(y_maxarg))

with st.expander('Пункт 8.'):
    st.write('Нажми на кнопку распознавания, запиши результат.')
    isbutton2 = st.button('Распознать еще картнку')
    col7,col8 = st.columns(2)
    with col7:
             if isbutton2:
                   st.image(file_path)
    with col8:
             if isbutton2:
                   image112 = Image.open(file_path)
                   img111 = image112.resize((28, 28), Image.LANCZOS)  
                   img121 = img111.convert("L")
                   imgData = np.asarray(img121)
                   step_lobe = value_sli / 100
                   mid_img_color = np.sum(imgData) / imgData.size
                   min_img_color = imgData.min()
                   THRESHOLD_VALUE = (mid_img_color - (mid_img_color - min_img_color) * step_lobe)
                   thresholdedData = (imgData < THRESHOLD_VALUE) * 1.0
                   imgData1 = np.expand_dims(thresholdedData, axis=0)
                   y_predict1 = model_2d.predict(imgData1)
                   y_maxarg = np.argmax(y_predict1, axis=1)
                   st.subheader(int(y_maxarg))
                   
              

with st.expander('Пункт 9.'):
    st.write('Включи фильтр Гаусса, если такая кнопка есть, нажми на кнопку распознавания, запиши результат.')
    col9,col10 = st.columns(2)
    with col9:
            value_gaus = st.slider('Фильтр Гаусса', 0, 10, 0)
    with col10:
            st.write('Фильтр Гаусса',value_gaus)
            image222 = Image.open(file_path)
            im2 = image222.filter(ImageFilter.GaussianBlur(radius = value_gaus))
            im2.save(file_path)
            st.image(file_path)
with st.expander('Пункт 10'):
    st.write('Попробуем теперь еще раз распознать картинку.')
    isbutton3 = st.button('Распознать картнку еще раз')
    col11,col12 = st.columns(2)
    with col11:
            if isbutton3:
                   st.image(file_path)
    with col12:
            if isbutton3:
                   image333 = Image.open(file_path)
                   img333 = image333.resize((28, 28), Image.LANCZOS) 
                   img334 = img333.convert("L")
                   imgData4 = np.asarray(img334) 
                   step_lobe = value_sli / 100
                   mid_img_color = np.sum(imgData4) / imgData4.size
                   min_img_color = imgData4.min()
                   THRESHOLD_VALUE = (mid_img_color - (mid_img_color - min_img_color) * step_lobe)
                   thresholdedData = (imgData4 < THRESHOLD_VALUE) * 1.0
                   imgData5 = np.expand_dims(thresholdedData, axis=0)
                   y_predict2 = model_2d.predict(imgData5)
                   y_maxarg2 = np.argmax(y_predict2, axis=1)
                   st.subheader(int(y_maxarg2)) 
                    
with st.expander('Пункт 11.'):
    st.write('Сделай выводы, какие именно фильтры и как влияют на результат эксперимента')
with st.expander('Пункт 12.'):
    st.write('Посмотрим как "видит" картинку нейронная сеть')
    col13,col14 = st.columns(2)
    with col13:
            value_thres = st.slider('Порог отсечки', 0, 100, 50)
    with col14:
            st.write('Порог отсечки',value_thres)
            image444 = Image.open(file_path)
            #i1 = image444.resize((28, 28), Image.LANCZOS) 
            i2 = image444.convert("L")
            i3 = np.asarray(i2)
            step_lobe = value_thres / 100
            mid_img_color = np.sum(i3) / i3.size
            min_img_color = i3.min()
            THRESHOLD_VALUE = (mid_img_color - (mid_img_color - min_img_color) * step_lobe)
            thresholdedData = (i3 < THRESHOLD_VALUE) * 255.0
            imm1 = Image.fromarray(thresholdedData)
            imm1 = imm1.convert("L")
            imm1.save(file_path)
            st.write(imm1) 
            st.image(file_path)
            #i4 = np.expand_dims(thresholdedData, axis=0)
            #imm1 = Image.fromarray(i4) 
            #imm1.save(file_path)
            #st.image(file_path)
            
with st.expander('Пожелания и замечания'):                
    st.write('https://docs.google.com/spreadsheets/d/1TuGgZsT2cwAIlNr80LdVn4UFPHyEePEiBE-JG6IQUT0/edit?usp=sharing')
