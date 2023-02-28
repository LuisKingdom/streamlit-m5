import streamlit as st

# Define the Streamlit app
def app():
    st.title("List App")
    items = st.text_area("Enter items, one per line")
    items = items.split("\n")
    items = list(filter(None, items))
    
    add_item = st.text_input("Add item")
    if st.button("Add"):
        items.append(add_item)
    
    if st.button("Delete last item") and len(items) > 0:
        items.pop()
    
    if len(items) > 0:
        st.write("Items:")
        for i, item in enumerate(items):
            st.write(f"{i+1}. {item}")

if __name__ == '__main__':
    app()
