import streamlit as st

st.title("데이터과학 실습용 APP")
st.header("1일차")
st.subheader("파이참 설정 및 사용법")
# 파이썬으로 실행하면 의미 없음-> 실행하는 환경을 설정해야

st.sidebar.selectbox("메뉴",['Home','입력','조회'])

