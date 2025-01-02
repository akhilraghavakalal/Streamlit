import streamlit as st
import os

st.header("use st.image(), for displaying images. We need to pass path of the image into this")
st.subheader("images must be placed in a folder, which should be in the same directory as our main code")
st.subheader("To pass the path use the os module. Get the cwd and join it with folder and filenames")
st.image(os.path.join(os.getcwd(), "ark", "leopard_predator.jpg"))
st.image(os.path.join(os.getcwd(), "ark", "leopard_predator.jpg"), width= 500)

st.write("There are different options available as well")