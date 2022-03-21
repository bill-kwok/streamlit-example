import streamlit as st
import time

st.title("Hello DS4")
st.header("DS4 > DS3 == True")

num1 = st.text_input("First number: ")
num2 = st.text_input("Second number: ")
st.text(int(num1)+int(num2))

click = st.button("Start")
if click:
  with st.spinner('Wait for it...'):
    time.sleep(5)
  st.success('Done!')
