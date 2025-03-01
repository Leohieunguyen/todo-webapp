import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app would improve your productivity")

for i, todo in enumerate(todos):
    st.checkbox(todo, key=f"todo_{i}")

st.text_input(label="Enter a todo", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

st.session_state