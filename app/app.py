import streamlit as st
import streamlit.components.v1 as components
import os

# ✅ Configure Streamlit page
st.set_page_config(page_title="iOS Style Calculator", layout="centered")

# ✅ Title
st.markdown("<h1 style='text-align: center;'>🧮 iOS Style Calculator</h1>", unsafe_allow_html=True)

# ✅ Function to load file content safely
def load_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"<!-- File not found: {path} -->"

# ✅ File paths
html_path = os.path.join("templates", "calculator.html")
css_path = os.path.join("static", "style.css")
js_path = os.path.join("static", "script.js")

# ✅ Load all components
html = load_file(html_path)
css = f"<style>{load_file(css_path)}</style>"
js = f"<script>{load_file(js_path)}</script>"

# ✅ Inject into Streamlit
components.html(css + html + js, height=700)
