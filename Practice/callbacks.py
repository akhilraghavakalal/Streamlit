import streamlit as st

st.subheader(
    "Callback is a function that is executed when an event happens (change, click)"
)
st.subheader(
    "Callbacks are executed first and then the app is executed from top to bottom"
)

if "first" not in st.session_state:
    st.session_state.first = 1
    st.session_state.name = ""

if "second" not in st.session_state:
    st.session_state.second = 0

if st.session_state.first == 1:
    st.subheader("First page")
    st.session_state.name = st.text_input("Enter your name: ")
    clicked = st.button("Next")
    if clicked:
        st.session_state.second = 2
        st.session_state.first = 0

elif st.session_state.second == 2:
    st.subheader("Second page")
    st.write(f"Name is : {st.session_state.name}")
    returned = st.button("Back")
    if returned:
        st.session_state.second = 0
        st.session_state.first = 1
st.divider()

st.subheader(
    "Even though the next button is clicked, the code doesnt change to second page since the code runs from top to bottom and the value remains unchanged in it. We need to click the button twice to make sure the changes are reflected."
)

st.write(
    "To handle this we need to use callbacks, since call backs get executed first before the program is executed from top to bottom"
)


def go_to_fourth(name2):
    st.session_state.fourth = 2
    st.session_state.third = 0
    st.session_state.info["name2"] = name2


def go_to_third():
    st.session_state.fourth = 0
    st.session_state.third = 1


if "info" not in st.session_state:
    st.session_state.info = {}

if "third" not in st.session_state:
    st.session_state.third = 1
    # st.session_state.info["name2"] = ""

if "fourth" not in st.session_state:
    st.session_state.fourth = 0

st.subheader("To display the previous value (if any) in a session_state variable, use the get() like value=st.session_state.info.get('name2', '')")
st.divider()

if st.session_state.third == 1:
    st.subheader("Third page")
    name2 = st.text_input(
        "Enter your name 02: ", value=st.session_state.info.get("name2", "")
    )
    # clicked = st.button("Next 02")
    # if clicked:
    #     st.session_state.fourth = 2
    #     st.session_state.third = 0
    clicked = st.button("Next 02", on_click=go_to_fourth, args=(name2,))

elif st.session_state.fourth == 2:
    st.subheader("Fourth page")
    st.write(f"Name is : {st.session_state.info["name2"]}")
    # returned = st.button("Back 02")
    # if returned:
    #     st.session_state.fourth = 0
    #     st.session_state.third = 1
    returned = st.button("Back 02", on_click=go_to_third)
