import streamlit as st

# Define the Streamlit app
def app():
    st.title("Wish List App")
    wishes = st.text_area("Enter your wishes, one per line")
    wishes = wishes.split("\n")
    wishes = list(filter(None, wishes))
    
    add_wish = st.text_input("Add a wish")
    if st.button("Add"):
        wishes.extend(add_wish)
    
    if st.button("Delete last wish") and len(wishes) > 0:
        wishes.pop()
    
    if len(wishes) > 0:
        st.write("Wishes:")
        for i, wish in enumerate(wishes):
            st.write(f"{i+1}. {wish}")

if __name__ == '__main__':
    app()
