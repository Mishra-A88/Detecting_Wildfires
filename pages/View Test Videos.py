import streamlit as st #type: ignore
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
        .text {
            text-align: center;
            font-size: 14px;
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
        
st.markdown("<div class='title'>Test videos</div>", unsafe_allow_html=True)


st.caption("<div class='text'>Videos do not have sound.</div>", unsafe_allow_html=True)

videos = glob('result-videos/*')

for video in videos:
    st.video(video)
