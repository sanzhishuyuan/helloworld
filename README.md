##
code list
##
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




import streamlit as st

# 使用col函数将页面分成两列
col1,col2,col3, col4 = st.columns(4)

# 在第一列中添加一个文本框
with col3:
    st.write("这是第一列")

# 在第二列中添加一个按钮
with col4:
    st.write("这是第二列")

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)

import streamlit as st
import requests

st.title('🏀 Bored API app')

st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)

st.header('Suggested activity')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')

  

# 2. Contents of st.experimental_get_query_params
st.header('2. Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params())


# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Hello **{firstname} {surname}**, how are you?')

import streamlit as st

st.title('st.form')

# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')

    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)

# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')
