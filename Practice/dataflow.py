import streamlit as st

st.header(
    "Anytime something is updated, Streamlit always runs from top to bottom in the script"
)

st.write(
    "Button attribute returns a boolean value, True if the button is clicked, false if it is untouched "
)
button_Value = st.button("First button in Streamlit")
st.write(button_Value)
st.write(
    "The value will be false initially and True once clicked. No matter how many times it is clicked it will be True only, not converted to false. However if there is a change in the code, then the file will be run from top to bottom again, so the value will be reset to the initial value, which is false and then it will become true when clicked"
)
st.divider()

first_return_value = st.button("First Button")
st.write(first_return_value)
second_return_value = st.button("Second Button")
st.write(second_return_value)

st.write("The interesting thing here is that, no matter whichever button we click, that button will have True value but the others will have false values in it, since everytime something changes, Streamlit runs from the top to bottom")
st.write("This state concept is something interesting and needs to be monitored in Streamlit")
st.divider()
