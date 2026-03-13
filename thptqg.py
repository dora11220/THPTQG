import streamlit as st
from streamlit_autorefresh import st_autorefresh
from datetime import datetime, timedelta

# Tự động làm mới giao diện
st_autorefresh(interval=100, key="countdown_timer")

st.header("Tiến độ mục tiêu 2028:", divider='rainbow')

# Thiết lập thời gian (Dùng utcnow + 7 để khớp giờ VN trên server)
now = datetime.utcnow() + timedelta(hours=7)
target = datetime(2028, 6, 26, 7, 30, 0) # Không cần +7 ở đây nếu đây là giờ đích thực tế
start_journey = datetime(2025, 8, 1)    # Giả sử hành trình bắt đầu từ đầu năm 2024

# Tính toán delta
delta = target - now
total_seconds = delta.total_seconds()

# Hiển thị các chỉ số đếm ngược
days = total_seconds / 86400
st.columns(3)[0].metric("Ngày còn lại", f"{days:,.0f}")
st.columns(3)[1].metric("Tháng còn lại", f"{days/30.43:,.1f}")
st.columns(3)[2].metric("Năm còn lại", f"{days/365.25:,.2f}")

st.write(f"⏱️ **Đếm ngược chi tiết:** {total_seconds/3600:,.0f} giờ hoặc {total_seconds:,.0f} giây")

st.divider()

# 1. TIẾN ĐỘ TRONG NGÀY (Day Progress)
day_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
time_passed_today = (now - day_start).total_seconds()
day_percentage = time_passed_today / 86400

st.write(f"🕒 Bây giờ là: **{now.strftime('%H:%M:%S')}**")
st.progress(day_percentage, text=f"Hôm nay đã trôi qua: {day_percentage*100:.1f}%")

# 2. TIẾN ĐỘ ĐẾN KỲ THI (Journey Progress)
# Công thức: (Đã đi được / Tổng thời gian hành trình)
total_journey_duration = (target - start_journey).total_seconds()
elapsed_journey = (now - start_journey).total_seconds()
journey_percentage = min(max(elapsed_journey / total_journey_duration, 0.0), 1.0) # Giới hạn từ 0-1

st.progress(journey_percentage, text=f"Tiến độ đến kỳ thi: {journey_percentage*100:.2f}%")

