import streamlit as st
from streamlit_lottie import st_lottie
import requests
from datetime import datetime, timedelta

# Page setup
st.set_page_config(
    page_title="Arun G | Content Calendar",
    page_icon="🚀",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
        body { background-color: #f9f9f9; }
        .calendar-card {
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        .footer {
            margin-top: 40px;
            text-align: center;
            font-size: 13px;
            color: #888;
            border-top: 1px solid #eee;
            padding: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Animation helper
def load_lottie(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    return None

# Portfolio link
st.write("""
Welcome!  
This app helps plan my **YouTube uploads** .

👉 [**Check my portfolio here**](https://arun2425.netlify.app/)
""")

# Content Calendar
st.header("📅 YouTube Content Calendar")
st.write("Plan your uploads for the next 4 weeks:")

videos_per_week = st.slider("Videos per week", 1, 7, 2)
start_date = st.date_input("Start date", datetime.today())
content_options = st.multiselect(
    "Content types",
    ["Vlog", "Tech Tips", "Review", "Shorts", "Tutorial", "Behind the Scenes"]
)

if st.button("Generate Calendar"):
    st.subheader("Your 4-Week Schedule")
    for week in range(4):
        st.markdown(f"<div class='calendar-card'><b>Week {week + 1}</b>", unsafe_allow_html=True)
        for i in range(videos_per_week):
            day = start_date + timedelta(days=week*7 + i*(7 // videos_per_week))
            kind = content_options[i % len(content_options)] if content_options else "Content"
            st.markdown(f"✅ {day.strftime('%A, %d %B %Y')} — {kind}", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        © 2025 Arun G • Made with Streamlit
    </div>
""", unsafe_allow_html=True)
