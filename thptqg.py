import streamlit as st
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=100)
st.header("Bạn còn:", divider='rainbow')

from datetime import datetime
now=datetime.now()
target=datetime(2028, 6, 26, 7, 30, 0)
delta=target-now
total_seconds=delta.total_seconds()
minutes=total_seconds/60
hours=total_seconds/3600
days=total_seconds/86400
months = days/30.436875
years=days/365.25

st.write(f"Năm: {years:,.2f}")
st.write(f"Tháng: {months:,.1f}")
st.write(f"Ngày: {days:,.2f}")
st.write(f"Giờ - phút - giây: {hours:,.0f} : {minutes:,.0f} : {total_seconds:,.1f}")

