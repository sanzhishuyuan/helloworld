import streamlit as st
st.header('文件名：streamlit_app.py')
st.header('30天学会Streamlit')

if st.button('时空传送门'):
     st.write('超级入门教程-点这里')
else:
     st.write('Goodbye') 





name = st.text_input('Enter your name:')
if name:
    st.write(f'Hello, {name}!')

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('nub&sheet')

# 样例 1

st.write('Hello, *World!* :sunglasses:')

# 样例 2

st.write('1=2+3-4')

# 样例 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     
     })
st.write(df)

# 样例 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# 样例 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)