import streamlit as st

st.subheader("Intro to forms in Streamlit")

st.write("Key is used to undiquely identify the form simiar to id attribute in HTML")
with st.form(key="simple_form_01"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age")

st.divider()

st.subheader("A form should always have an submit button")
st.write("st.form_submit_button('Button Name')")
with st.form(key="simple_form_02"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age")
    submit = st.form_submit_button("Submit Button")
    print("Name: ", name)
    print("age: ", age)
    print()
st.divider()

st.write(
    "Form fields are supposed to be inside the with attribute so that the fields will be submitted only once"
)
st.write("Whenever code changes in streamlit the code runs from top to bottom")
st.write(
    "So instead of submitting everything everytime, we use 'with st.form()', so that the data will be submitted only once when the submit button is clicked"
)

st.divider()

st.subheader("Simple complex form with warnings for the submit button")

dict_values = {"name": None, "age": None, "gender": None, "dob": None}

with st.form(key = "simple_complex_form"):
    dict_values['name'] = st.text_input("Enter your name")
    dict_values['age'] = st.number_input("Enter your age")
    dict_values['gender'] = st.selectbox("Gender", ["Male", "Female"], placeholder="Select the gender")
    dict_values['dob'] = st.date_input("Enter your Birthdate")
    
    button_clicked = st.form_submit_button("Submit the complex form")
    # once the button is clicked, check if all the values are changed or not if no print a warning
    if button_clicked:
        if not all(dict_values.values()):
            st.info("Please fill all the values")
            st.warning("Please fill all the values")
        else:
            st.balloons()
            st.write(dict_values)

st.divider()

st.subheader("date_input() will only display 10 years back from the current date")
st.write("To display all the dates more than 10 years, we use mindate & maxdate")

from datetime import datetime as dt

min_date = dt(1990, 1, 1)
max_date = dt.now()
with st.form(key = "simple_complex_form_02"):
    dict_values['name'] = st.text_input("Enter your name")
    dict_values['age'] = st.number_input("Enter your age")
    dict_values['gender'] = st.selectbox("Gender", ["Male", "Female"], placeholder="Select the gender")
    dict_values['dob'] = st.date_input("Enter your Birthdate", min_value=min_date, max_value=max_date)
    
    button_clicked = st.form_submit_button("Submit the complex form")
    # once the button is clicked, check if all the values are changed or not if no print a warning
    if button_clicked:
        if not all(dict_values.values()):
            st.info("Please fill all the values")
            st.warning("Please fill all the values")
        else:
            st.balloons()
            st.write(dict_values)

st.divider()