import numpy as np
import pandas as pd
import streamlit as st

st.title('This is First Assignments!!!!!')
st.write('All the Students do it for Cloud Computing!!')

data = pd.DataFrame(
    {'Names':['Hamoud','Ali','Abdullah','Hussain','Ahmed','Salman','Mohammed','Ibrahim'],
     'Age':[21,17,19,23,19,11,21,20]})

st.write("Following is Student Details:")
st.write(data)

chart_data=pd.DataFrame(
    np.random.randn(20,4),
    columns=['A','B','C','D']
)
st.bar_chart(chart_data)