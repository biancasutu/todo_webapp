import streamlit as st
import functions
import time

# streamlit run to_do_app/web.py
# streamlit = framework for data analytics and machine learning

todos = functions.get_todos()


def add_todo():     # this is a callback function
    todo = '\n' + st.session_state['new_todo']
    todos.append(todo)
    functions.write_todos(todos)


st.title('My Todo App')
st.subheader(time.strftime('%b %d, %Y %H:%M:%S'))

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()  # update in real time withot refreshing the webpage

st.text_input(label='', placeholder='Add a new todo...',
                on_change=add_todo, key='new_todo')
