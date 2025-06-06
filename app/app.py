import streamlit as st
import streamlit.components.v1 as components
import os

# Set page config
st.set_page_config(page_title="CalculatorX", layout="centered")

# Title
st.title("👇🏻 CalculatorX")

# Read files
def load_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

# Paths
html_path = os.path.join("templates", "calculator.html")
css_path = os.path.join("static", "style.css")
js_path = os.path.join("static", "script.js")

# Load code
html_code = load_file(html_path)
css_code = f"<style>{load_file(css_path)}</style>"
js_code = f"<script>{load_file(js_path)}</script>"

# Display calculator
components.html(css_code + html_code + js_code, height=650)
