import streamlit as st
from datetime import datetime as dt

st.header("Streamlit Complex Form")

min_date = dt(1998, 1, 1)
max_date = dt.now()

details = {
    "Name": None,
    "Feedback": None,
    "DOB": None,
    "Time": None,
    "Radio": None,
    "Dropdown": None,
    "Slider" : None,
    "Checkbox1" : None,
    "Checkbox2" : None
}
with st.form(key="text_input_form"):
    st.subheader("Text Inputs")
    details["Name"] = st.text_input("Enter your :green[name]")
    details["Feedback"] = st.text_area("Provide your feedback")
    st.divider()

    st.subheader("Date and Time inputs")
    details["DOB"] = st.date_input("Select your date of birth", min_value=min_date, max_value=max_date)
    details["Time"] = st.time_input("Choose a time")
    st.divider()

    st.subheader("Selectors")
    details["Radio"] = st.radio(
        "Choose one of the below :rainbow[radio] options",
        options=[":rainbow[Option 01]", "Option 02", "Option 03"],
    )
    details["Dropdown"] = st.selectbox(
        "Choose one of the below :rainbow[checkbox] options",
        options=["Option 01", ":rainbow[Option 02]", "Option 03"],
    )
    details["Slider"] = st.select_slider("Select rating slider", options=[1, 2, 3, 4, 5])
    st.write("Select the below checkboxes")
    details["Checkbox1"] = st.checkbox("Receive Notification")
    details["Checkbox2"] = st.checkbox("Dark Mode enable :red[?]")
    st.divider()

    button_clicked = st.form_submit_button("Submit")
    
    if button_clicked:
        if not all(details.values()):
            st.warning("Please enter all the values")
            st.info("Please enter all the values")
            st.success("Please enter all the values")
        else:
            st.write(details)
