import streamlit as st

#Take a user input\
name=st.text_input("enter your name")

st.title("take the input")

if st.button("submit"):
 st.write("print the name:(name}")
