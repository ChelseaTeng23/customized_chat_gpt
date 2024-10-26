import streamlit as st
import pandas as pd
st.write("### G Morning!")

"hello"

a=3
a
[11,22,33]

{"a":1,"b":2,"c":3}

st.image("iShot_2024-10-26_06.24.30.png",width=200)

df = pd.DataFrame({"学号": ["01", "02", "03", "04", "05"],
              "班级": ["二班", "一班", "二班", "三班", "一班"],
              "成绩": [92, 67, 70, 88, 76]})
st.dataframe(df)
st.divider()
st.table(df)