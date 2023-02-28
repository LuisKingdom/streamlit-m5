import streamlit as st

# Define the Streamlit app
def app():
    st.title("Requisitos")
    requirements = st.text_area("Ingrese los requisitos, uno por línea")
    requirements = requirements.split("\n")
    requirements = list(filter(None, requirements))
    
    if len(requirements) > 0:
        st.write("Requisitos:")
        for i, requirement in enumerate(requirements):
            st.write(f"{i+1}. {requirement}")

if __name__ == '__main__':
    app()
