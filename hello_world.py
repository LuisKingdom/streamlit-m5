import streamlit as st
from datetime import time

st.header("Single Range Time Slider")

# Default start and end time
start_time = time(8, 0)
end_time = time(18, 0)

# User-selectable time range
selected_time_range = st.slider("Select Time Range", value=(start_time, end_time), format="HH:mm")

# Display selected time range
st.write("Selected Time Range: {} - {}".format(selected_time_range[0].strftime("%H:%M"), selected_time_range[1].strftime("%H:%M")))
