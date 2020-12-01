import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import shared
from streamlit_cheatsheet import cheatsheet


def tab1():
    st.title("hello from updated repo")


def tab2():
    st.title("hello from tab 2")


def tab3():
    st.title("hello from tab 3")


def tab4():
    st.title("hello from tab 4")


tabs = {"tab1": tab1, "tab2": tab2, "tab3": tab3, "tab4": tab4}
tab = st.sidebar.selectbox("", list(tabs.keys()))


style = """
    .sidebar .sidebar-content {
        width: 26vw;
        padding: 2em;
    }

    .reportview-container .main .block-container {
        padding: 2em;
    }
"""

st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)
tabs[tab]()
cheatsheet(st)
