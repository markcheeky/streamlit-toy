import time
import pandas as pd
import numpy as np


def cheatsheet(st):
    st.title("h1")
    st.header("h2")
    st.subheader("h3")

    st.markdown("<br/>", unsafe_allow_html=True)

    slider = st.slider("slider title", 0, 100, (5, 80), 5)

    checkbox = st.checkbox('This is checkbox')

    radio = st.radio("radio title", [1, 2, 3, 4])

    button = st.button("henlo")

    select = st.selectbox("", ["s1", "s2", "s3"])

    st.code("lambda foo: hello(42)", language="python")

    # progressbar
    # latest_iteration = st.empty()
    # bar = st.progress(0)
    # for i in range(10):
    #    latest_iteration.text(f'Iteration {i+1}')
    #    bar.progress(i + 1)
    #    time.sleep(0.1)

    # spinner
    # with st.spinner(text="waiting on magic to happen"):
    #    time.sleep(3)

    # st.balloons()

    df = pd.DataFrame({
        "a": range(10),
        "b": range(15, 5, -1),
        "c": range(10)
    })

    st.write(df)

    st.write(np.arange(20).reshape(2, -1))
