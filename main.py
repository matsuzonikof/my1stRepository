import numpy as np
import pandas as pd
import streamlit as st
 
df = pd.DataFrame( np.random.randn(10, 4), columns=['a', 'b', 'c','d'] )
 
st.title("Simple Streamlit App")
 
st.write("πγLine-Chart")
st.line_chart(df)
 
if st.checkbox('π Show DataFrame (with highlight_max)'):
 st.table(df.style.highlight_max(axis=0))