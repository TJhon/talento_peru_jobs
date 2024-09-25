import streamlit as st
import pandas as pd
import time
from TalentPeru import last_scrapper


@st.cache_data
def load_data():
    df = last_scrapper()
    df["payment"] = (
        df["payment"].str.replace("S/. ", "").str.replace(",", "").astype(float)
    )

    return df


data = load_data()

departamentos = data["dep"].unique()


st.title("Trabajos ")

st.write(departamentos)


def update_input_state():
    st.session_state.input_changed = True
