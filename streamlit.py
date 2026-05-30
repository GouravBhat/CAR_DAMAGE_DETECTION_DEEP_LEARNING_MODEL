import streamlit as st
st.title("CAR DAAMGE DETECTION")
from model_helper import predict

uploaded_file=st.file_uploader("upload file here",type=["jpg","png","jpeg"])

if uploaded_file:
    input_file="temp_file.jpg"
    with open(input_file,"wb") as f:
        f.write(uploaded_file.getbuffer())

        st.image(uploaded_file,caption="uploaded file",use_container_width=True)
        prediction=predict(input_file)
        st.info(f"damage prediction : {prediction}")