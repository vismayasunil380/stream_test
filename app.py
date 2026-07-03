import streamlit as st

#Take a user imput\
name=st.text_input("enter your name")

st.title("take the input")

if st.button("submit"):
  st.write(f"print the name: {name}")
