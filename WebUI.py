import streamlit as st
import function

todos = function.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    function.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my web todo app")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new Todo...", on_change=add_todo, key='new_todo')
