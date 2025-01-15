import streamlit as st

st.subheader("Counter does not increase eventhough the button is clicked multiple times, since when the button is clicked, the code re runs from the top. So the value of counter will be atmost 1")
counter = 0

st.write(f"Counter value: {counter}")

button_clicked = st.button("Counter incrementor")

if button_clicked:
    counter += 1
    st.write(f"Counter incremented: {counter}")
else:
    st.write(f"Counter remains the same: {counter}")

st.divider()

st.subheader("To store the values, eventhough the code re runs from the start, we need to use something called as session_state")

if "count" not in st.session_state:
    st.session_state.count = 0
st.write(f"Counter value: {st.session_state.count}")

button_clicked2 = st.button("Counter incrementor 02 ")

if button_clicked2:
    st.session_state.count += 1
    st.write(f"Counter incremented: {st.session_state.count}")
else:
    st.write(f"Counter remains the same: {st.session_state.count}")
