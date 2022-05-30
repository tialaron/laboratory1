import matplotlib.pyplot as plt #Отрисовка графиков
import seaborn as sns
import numpy as np #Numpy
from PIL import Image
import time
from datetime import datetime

st.set_page_config(layout="wide")
st.title('Лабораторная работа "Распознавание рукописных цифр". ')

st.markdown('''<h1 style='text-align: center; color: black;'
            >Цифры MNIST</h1>''',
            unsafe_allow_html=True)
with st.expander('Пункт 1.'):
    st.write('Разверни и прочитай все ячейки.')

with st.expander('Пункт 2.'):
    st.write('Возьми ту из предложенных цифр, которая подписана, что она хорошо распознаётся. '
             'Эта цифра похожа на цифры обучающего набора, в чём можешь убедиться, сравнив её '
             'с цифрами образцового набора на экране.')

with st.expander('Пункт 3.'):
    st.write('Поднеси цифру к видеокамере так, чтобы она занимала большую часть экрана видео в '
             'окошке, располагалась в центре и была хорошо освещена.')

with st.expander('Пункт 4.'):
    st.write('Другой рукой возьми мышь и щёлкни на кнопку, чтобы сделать снимок цифры.')

with st.expander('Пункт 5.'):
    st.write('Зарисуй полученное изображение чёрно - белой цифры в окошке под снимком цифры в бланк отчёта. '
             'Необходимо на рисунке отобразить возникшие недочёты изображения цифры, например, пропуски. Чтобы'
             'не зарисовывать всё чёрное пространство, рекомендуется изобразить ручкой цифру на белом фоне '
             'листа бланка отчёта.')

img_file_buffer = st.camera_input("Take a picture")



if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))
