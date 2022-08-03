import os.path

import cv2
import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
from streamlit_drawable_canvas import st_canvas

# 경로 설정
file_path = os.path.dirname(__file__)

# 모델파일 폴더 생성
save_dir = os.path.join(file_path, 'model')

# 학습된 모델 불러오기
model_file = 'minist_model.h5'
#model = load_model(os.path.join(save_dir, model_file))
model = load_model(model_file)

# 헤더 출력
st.subheader('손글씨 숫자 인식')

SIZE = 192

canvas_result = st_canvas(
    fill_color='#000000',
    stroke_width=20,
    stroke_color='#FFFFFF',  # 흰색
    background_color='#000000',  #검정색
    width=SIZE,
    height=SIZE,
    drawing_mode='freedraw',
    update_streamlit=False,  #이벤트가 생길떄마다 리프레시하는 옵션
    key='canvas')

if canvas_result.image_data is not None:
    img = cv2.resize(canvas_result.image_data.astype('uint8'), (28, 28))  # unsignedINT , 예측에 사용할 이미지
    rescaled = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_NEAREST)  #보간법, 확대시 채워넣을 알고리즘
    st.write('모델 입력 형태')
    st.image(rescaled)

if st.button('Predict'):
    test_x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res = model.predict(np.reshape(test_x, (1, 28 * 28))) # test_x: 2차원
    st.success(np.argmax(res[0]))
    st.bar_chart(res[0])