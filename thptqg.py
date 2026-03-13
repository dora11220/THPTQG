import streamlit as st
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=100)
st.header("Bạn còn bao nhiêu thời gian:", divider='rainbow')

from datetime import datetime, timedelta

now=datetime.now() + timedelta(hours=7)
target=datetime(2028, 6, 26, 7, 30, 0) + timedelta(hours=7)
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
st.write(f"Giờ - phút - giây: {hours:,.0f} - {minutes:,.0f} - {total_seconds:,.1f}")

todayTarget = now.replace(hour=0,minute=0,second=0, microsecond=0) + timedelta(days=1)
st.write(f"Hiện tại là: {now.hour} : {now.minute}")
st.write(f"Bạn còn {int((todayTarget - now).total_seconds()/3600)} tiếng")

dayStart = now.replace(hour=0,minute=0,second=0, microsecond=0)
timePassed = now - dayStart

dayPercentage = int(timePassed.total_seconds()/ 86400 * 100)

st.progress(dayPercentage, "Ngày:")

journeyPercentage = int(now/target * 100)
st.progress(hourneyPercentage, "Thi: ")






