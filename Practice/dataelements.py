import streamlit as st
import pandas as pd
import numpy as np

map = {1: "Akhil", 2: "Raghava", 3: "Kalal"}
st.subheader("Regular Dictionary")
st.write(map)

st.subheader("Regular Dictionary as a Streamlit Dataframe")
st.dataframe(map)
st.divider()
details = {
    "name": ["person 01", "person 02", "person 03"],
    "age": [25, 26, 27],
    "occupation": ["Software Engineer", "Programmer", "Developer"],
}
st.subheader("Dictionary -> Streamlit Dataframe")
st.dataframe(details)
st.write(
    "If we use st.dataframe(), keys will be shown as column names and values as rows. The columns can be sorted in asc and desc orders. We can use the custom functionalities like download as csv, search and expand functionalities"
)

st.subheader("Dictionary -> Pandas Dataframe -> Streamlit Dataframe")
st.dataframe(pd.DataFrame(details))
st.write(
    "If we convert the dictionary to a pandas dataframe first and then convert it to streamlit dataframe, all the above functionalities will be present and a new column that represents the row indexes will be present in the first column, since pandas adds row numbers automatically"
)
st.header("Dataframes are not editable")
st.divider()

st.subheader(
    "If we want for some reason, to make the dataframes :red[editable] then we use data_editor() for editable dataframes :ghost:"
)
st.write(
    "We can even catch the newly modified dataframe, since the return type for st.data_editor() is the newly modified data frame :red[*]"
)
st.write("Any change will not impact the original dataframe")
new_df = st.data_editor(details)
st.dataframe(new_df)

st.divider()

st.subheader(
    "If you feel that all of this is :red[too much :upside_down_face:] then simply use a table() for regular static table"
)
st.table(details)
st.divider()

st.subheader("Metrics")
st.write("Metrics are some useful info about the data")
st.metric("Average Age ", np.mean(details["age"]))
st.metric("Average Age ", np.mean(details["age"]), delta="10")
st.metric("Average Age ", np.mean(details["age"]), delta="-10")
st.divider()

a, b, c = st.columns(3)
a.metric("Average Age ", np.mean(details["age"]))
b.metric("Average Age ", np.mean(details["age"]), delta="10")
c.metric("Average Age ", np.mean(details["age"]), delta="-10")
st.divider()

d, e, f = st.columns(3)
d.metric("Average Age ", np.mean(details["age"]), border=True)
e.metric("Average Age ", np.mean(details["age"]), delta="10", border=True)
f.metric("Average Age ", np.mean(details["age"]), delta="-10", border=True)
st.divider()

st.write("We can reverse the colors of delta as well using delta_color = 'inverse'")
h, i, j = st.columns(3)
h.metric("Average Age ", np.mean(details["age"]), border=True)
i.metric(
    "Average Age ",
    np.mean(details["age"]),
    delta="10",
    delta_color="inverse",
    border=True,
)
j.metric(
    "Average Age ",
    np.mean(details["age"]),
    delta="-10",
    delta_color="inverse",
    border=True,
)
st.divider()

st.write("We can mute the color as well using delta_color = 'Off'")

st.metric(
    "Average Age ",
    np.mean(details["age"]),
    delta="-10",
    delta_color="off",
    border=True,
)
st.write(" Look at the docs for more details :red[https://docs.streamlit.io/develop/api-reference/data/st.metric]")