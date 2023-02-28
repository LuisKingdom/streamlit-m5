import streamlit as st
from datetime import time

st.header("Range Time Slider")

# Default start and end time
start_time = time(8, 0)
end_time = time(18, 0)

# User-selectable start and end time
start_time = st.slider("Start Time", value=start_time, format="HH:mm")
end_time = st.slider("End Time", value=end_time, format="HH:mm")

# Display selected start and end time
st.write("Selected Time Range: {} - {}".format(start_time.strftime("%H:%M"), end_time.strftime("%H:%M")))
