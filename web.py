import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+"\n")
    functions.write_todos(todos, )

st.title("My Todo App")
st.subheader("Let us make it better than jira!")
st.write("To improve the productivity, we waste our time to create that app.")

for idx, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(idx)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter a Todo"
              , on_change=add_todo, key="new_todo")

#st.session_state