import streamlit as st

st.header("Akhil Raghava Kalal")

st.write("writing to streamlit app using st.write()")

st.write("Command to run streamlit")
st.write("streamlit run folder\\filename")

st.write({"Key1": "value1", "Key2": "value2"})

st.write(["l", "i", "s", "t"])

st.write(("t", "u", "p", "l", "e"))

st.write(
    "We can also write to streamlit app without using st.write() and write regularly"
)

"Hello World"

{"Key1": "value1", "Key2": "value2"}

["l", "i", "s", "t"]

("t", "u", "p", "l", "e")

"Mathematical equations as well"

"3 + 4 = ", 3+4
"3 - 4 = ", 3-4
"3 * 4 = ", 3*4
"3 / 4 = ", 3/4

"""Eventhough we can write content in both ways, using st.write() is the best option
cause it can handle complex and robust data types and based on the datatype 
it can automatically handle it in a different way. 
For example, st.write() can handle charts, graphs, dataframes..."""