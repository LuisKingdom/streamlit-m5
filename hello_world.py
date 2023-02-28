import streamlit as st

# Create a list to hold the tasks
tasks = []

# Define a function to add tasks to the list
def add_task(task):
    tasks.append(task)

# Define the Streamlit app
def app():
    st.title("To-Do List App")
    task = st.text_input("Enter a task")
    if st.button("Add Task"):
        add_task(task)
    if len(tasks) > 0:
        st.write("Tasks:")
        for i, task in enumerate(tasks):
            st.write(f"{i+1}. {task}")

if __name__ == '__main__':
    app()
