import streamlit as st
import functions




st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to store the todos")

todos = functions.get_todos()
for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Type a todo...")

print("Hello")