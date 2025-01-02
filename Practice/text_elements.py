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