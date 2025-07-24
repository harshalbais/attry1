import streamlit as st
import requests

st.set_page_config(page_title="📋 Attendance", layout="centered")

st.title("📡 ESP8266 Attendance System")

ip = st.text_input("Enter ESP IP Address (Default: 192.168.4.1)", "192.168.4.1")

if st.button("🔍 Fetch Attendance"):
    try:
        url = f"http://{ip}/"
        response = requests.get(url)
        if response.status_code == 200:
            raw_data = response.text.strip().split('\n')
            st.success("Attendance data fetched successfully!")
            st.write("### ✅ Present Students")
            for i, entry in enumerate(raw_data, 1):
                st.write(f"{i}. {entry}")
        else:
            st.error("Failed to fetch data from ESP")
    except Exception as e:
        st.error(f"Error: {e}")
