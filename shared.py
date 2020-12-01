import streamlit as st


@st.cache
def data():
    numpyy = np.random.rand(20, 10) * 100

    return pd.DataFrame(data=numpyy, columns=[chr(a + ord('a')) for a in range(10)])


@st.cache(suppress_st_warning=True)
def dataframe(slider):
    a, b = slider
    dat = data()
    # filt = (dat.a > a) & (dat.a < b)
    return dat
