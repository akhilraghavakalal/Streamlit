import streamlit as st

st.subheader("It matters where you to try to access the variable")
st.write("The counter value is different when reset counter is clicked. It will be reset to 0 at the bottom but not at the top. :red[Understand this]")


if "count" not in st.session_state:
    st.session_state.count = 0

pressed = st.button("Increment Counter")

if pressed:
    st.session_state.count += 1

st.write(f"Counter Value: {st.session_state.count}")

reset = st.button("Reset Counter")

if reset:
    st.session_state.count = 0
    
st.write(f"Counter Value: {st.session_state.count}")