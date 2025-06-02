import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "lat" : np.random.randn(1000) / 50 + 37.76,
    "lon" : np.random.randn(1000) / 50 - 122.74,
    "size" : np.random.randn(1000) * 100,
    "color" : np.random.randn(1000,4).tolist(),

})

st.title(":sparkles: 탭  :sparkles:")
st.map(df)