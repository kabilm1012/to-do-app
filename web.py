import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to store the todos")

todos = functions.get_todos()
for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Type a todo...",
              on_change=add_todo, key="new_todo")

st.session_state

print("Hello")