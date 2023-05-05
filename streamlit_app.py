import streamlit as st
import numpy as np
import pandas as pd

st.header('文件名：streamlit_app.py')
st.header('30天学会Streamlit')

url = 'https://30days.streamlit.app/?challenge=Day1'
if st.button('时空传送门'):
     st.write('超级入门教程-点这里')
     st.markdown(f'<a href="{url}" target="_blank">{url}</a>', unsafe_allow_html=True)
else:
     st.write('Goodbye')  
     
st.write('启动命令：streamlit run streamlit_app.py')
st.header('30天学会streamlit')
url = 'https://30days.streamlit.app/?challenge=Day1'
                

st.header('布局应用')

# 使用for循环生成数字序列

# 创建两列
col1, col2,col3 = st.columns(3)

# 在第一列中放置一个HTML标签，并应用CSS样式
with col1:
    st.write("<div style='height: 200px; width: 100%; background-color: Lime;'>Column 1</div>", unsafe_allow_html=True)

# 在第二列中放置一个HTML标签，并应用CSS样式
with col2:
    st.write("<div style='height: 400px; width: 100%; background-color: blue;'>Column 2</div>", unsafe_allow_html=True)
# 在第三列中放置一个HTML标签，并应用CSS样式
with col3:
    st.write("<div style='height: 400px; width: 100%; background-color: green;'> st.write('Aqua - 青色','Black - 黑色' , 'Lime - 酸橙色', 'Olive - 橄榄色','Silver - 银色','White - 白色','Teal - 蓝绿色')</div>", unsafe_allow_html=True)


     
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
