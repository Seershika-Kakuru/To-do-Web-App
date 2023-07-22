import streamlit as st
import todoListProgram_functions

todos_list = todoListProgram_functions.get_todos()


def add_todo():
    # get the todo entered
    todo_entered = st.session_state["todo_input"] + "\n"
    todos_list.append(todo_entered)
    todoListProgram_functions.write_todos(todos_list)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos_list.pop(index)
        todoListProgram_functions.write_todos(todos_list)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",placeholder="Add a todo...", key="todo_input", on_change=add_todo)