import streamlit as st
from glob import glob

st.markdown(
        """
        <style>
        .container {
            max-width: 800px;
        }
        .title {
            text-align: center;
            font-size: 35px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .description {
            margin-bottom: 30px;
        }
        .instructions {
            margin-bottom: 20px;
            padding: 10px;
            background-color: #f5f5f5;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
logos = glob('logos/*.png')
for img in logos:
        st.sidebar.image(img, use_column_width=True)
st.markdown("<div class='title'>Test images</div>", unsafe_allow_html=True)

images = glob('result-images/*.jpeg')

for image in images:
    st.image(image, use_column_width=True)

