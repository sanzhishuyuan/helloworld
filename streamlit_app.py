import streamlit as st
import numpy as np
st.header('文件名：streamlit_app.py')
st.header('30天学会Streamlit')

url = 'https://30days.streamlit.app/?challenge=Day1'
if st.button('时空传送门'):
     st.write('超级入门教程-点这里')
     st.markdown(f'<a href="{url}" target="_blank">{url}</a>', unsafe_allow_html=True)
else:
     st.write('Goodbye')  
     
st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)



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
