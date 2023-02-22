import streamlit as st
import functions
import time
import datetime

# st.columns([2, 1])  # 2 columns, we choose the ratio (the size of the columns inside []

todos = functions.get_todos()


def add_todo():     # this is a callback function
    todo = '\n' + st.session_state['new_todo']
    todos.append(todo)
    functions.write_todos(todos)


st.set_page_config(layout='wide')


st.title('My Todo App')


for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='', placeholder='Add a new todo...',
                on_change=add_todo, key='new_todo')

