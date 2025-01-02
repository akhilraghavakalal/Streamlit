import streamlit as st

st.title("This is a title")
st.header("This is the header")
st.subheader("This is the subheader")
st.write("There are no h1,h2,....")
st.caption("This is the caption attribute for small text")

st.divider()

st.markdown("We can use **Markdown** as well using markdown(), we can **bold**, *italicize*, <u>underline</u>")

st.divider()

st.write("We can even display code using code()")

st.code('''def function_name:
    print("Test function")
            ''', language="python")

st.write("We can even define functions or code separately and can use it in the code()")

code = """
def codesample:
    print("Code Sample")
"""
st.code(code, language="python")

st.divider()

st.header("If you want to know anything about a particular attribute just write the attribute without a parenthisis and it will display all the information from streamlit along with cool examples")
st.subheader("st.subheader")
# st.subheader
st.divider()
st.subheader("_Streamlit_ is :blue[cool] :heart:")
st.subheader("This is a subheader with a divider", divider="gray")
st.subheader("These subheaders have rotating dividers", divider=True)
st.subheader("One", divider=True)
st.subheader("Two", divider=True)
st.subheader("Three", divider=True)
st.subheader("Four", divider=True)

st.divider()
st.header("https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/")